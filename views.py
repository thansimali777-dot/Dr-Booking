from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import Doctor_table, Schedule_table, User_table, Booking_table


def Adddrpost(request):
    a=request.POST['name']
    b=request.POST['email']
    c=request.POST['phone']
    d=request.POST['specialization']
    e=Doctor_table()
    e.name=a
    e.email=b
    e.phone=c
    e.specialization=d
    e.save()
    return JsonResponse({'data':'successfully added'})

def Viewdr(request):
    a=Doctor_table.objects.all()
    data=[]
    for i in a:
        data.append(
            {
                'id':i.id,
                'name':i.name,
                'email':i.email,
                'phone':i.phone,
                'specialization':i.specialization,
            }
        )
    return JsonResponse({'data':data})

def Deletedr(request):
    a=request.POST['id']
    b=Doctor_table.objects.get(id=a)
    b.delete()
    return JsonResponse({'data':'successfully deleted'})

def Editdrpost(request):
    a=request.POST['id']
    b=request.POST['name']
    c=request.POST['email']
    d=request.POST['phone']
    e=request.POST['specialization']
    f=Doctor_table.objects.get(id=a)
    f.name=b
    f.email=c
    f.phone=d
    f.specialization=e
    f.save()
    return JsonResponse({'data':'success'})

def Editdr(request):
    a=request.GET['id']
    b=Doctor_table.objects.get(id=a)
    return JsonResponse(({
        'name':b.name,
        'email':b.email,
        'phone':b.phone,
        'specialization':b.specialization,

    }))

def Addschedulepost(request):
    f=request.POST['id']
    a=request.POST['days']
    b=request.POST['fromtime']
    c=request.POST['totime']
    e=Schedule_table()
    e.DOCTOR=Doctor_table.objects.get(id=f)
    e.days=a
    e.fromtime=b
    e.totime=c
    e.status="pending"
    e.save()
    return JsonResponse({'data':'successfully added'})

def Viewschedule(request):
    a=Schedule_table.objects.all()
    data=[]
    for i in a:
        data.append(
            {
                'id':i.id,
                'name':i.DOCTOR.name,
                'specialization':i.DOCTOR.specialization,
                'days':i.days,
                'fromtime':i.fromtime,
                'totime':i.totime,
                'status':i.status,
            }
        )
    return JsonResponse({'data':data})

def Deleteschedule(request):
    a=request.POST['id']
    b=Schedule_table.objects.get(id=a)
    b.delete()
    return JsonResponse({'data':'successfully deleted'})

def Editschedulepost(request):
    a=request.POST['id']
    b=request.POST['days']
    c=request.POST['fromtime']
    d=request.POST['totime']
    f=Schedule_table.objects.get(id=a)
    f.days=b
    f.fromtime=c
    f.totime=d
    f.save()
    return JsonResponse({'data':'success'})

def Editschedule(request):
    a=request.GET['id']
    b=Schedule_table.objects.get(id=a)
    return JsonResponse(({
        'days':b.days,
        'fromtime':b.fromtime,
        'totime':b.totime,

    }))

def Viewuser(request):
    a=User_table.objects.all()
    data=[]
    for i in a:
        data.append(
            {
                'id':i.id,
                'name':i.name,
                'age':i.age,
                'phone':i.phone,
            }
        )
    return JsonResponse({'data':data})

def Adduserpost(request):
    a=request.POST['name']
    b=request.POST['age']
    c=request.POST['phone']
    e=User_table()
    e.name=a
    e.age=b
    e.phone=c
    e.save()
    return JsonResponse({'data':'successfully added'})

def Book(request):
    b=Schedule_table.objects.all()
    data=[]
    for i in b:
        data.append(
            {
                'id':i.id,
                'uid':i.DOCTOR.id,
                'name':i.DOCTOR.name,
                'specialization':i.DOCTOR.specialization,
                'days':i.days,
                'fromtime':i.fromtime,
                'totime':i.totime,
                'status':i.status,
            }
        )
    return JsonResponse({'data':data})

def Appointment(request):
    uid=request.GET['id']

    b=Booking_table.objects.filter(USER_id=uid)

    data=[]

    for i in b:
        data.append({
            'id':i.id,
            'name':i.USER.name,
            'phone':i.USER.phone,
            'doctor':i.SCHEDULE.DOCTOR.name,
            'specialization':i.SCHEDULE.DOCTOR.specialization,
            'days':i.SCHEDULE.days,
            'fromtime':i.SCHEDULE.fromtime,
            'totime':i.SCHEDULE.totime,
            'status':i.status,
        })

    return JsonResponse({'data':data})

def Deleteuser(request):
    a=request.POST['id']
    b=User_table.objects.get(id=a)
    b.delete()
    return JsonResponse({'data':'successfully deleted'})

def Booked(request):
    uid=request.POST['uid']
    sid=request.POST['sid']

    c=User_table.objects.get(id=uid)
    d=Schedule_table.objects.get(id=sid)

    Booking_table.objects.create(
        SCHEDULE=d,
        USER=c,
        date=d.days,
        status='booked'
    )

    d.status='booked'
    d.save()

    return JsonResponse({'data':'successfully Booked'})

def Deleteappointment(request):
    a=request.POST['id']
    b=Booking_table.objects.get(id=a)
    b.delete()
    return JsonResponse({'data':'successfully deleted'})

def Editappointment(request):
    a=request.GET['id']

    b=Booking_table.objects.get(id=a)

    return JsonResponse({
        'date':b.date,
        'status':b.status
    })

def Editappointmentpost(request):
    a=request.POST['id']
    b=request.POST['date']

    d=Booking_table.objects.get(id=a)

    d.date=b
    d.status=c
    d.save()

    return JsonResponse({
        'data':'Successfully updated',
        'uid':d.USER.id
    })