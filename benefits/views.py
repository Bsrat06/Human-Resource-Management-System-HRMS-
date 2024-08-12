from django.shortcuts import render , redirect 
from django.db.models import Count ,Sum
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from employees.models import *
import datetime
from datetime import timedelta

@login_required(login_url="emp_login")
def index(request):
    return render (request , 'benefit/benefit.html' )


def login_user(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pk']
        user = authenticate(request,username=username , password=password)
        if user is not None and user.is_staff :
            login(request, user)
            messages.success(request,("Sign in  succesfull!"))
            return redirect('benefit')
        else :
            # message not implmented to the inside html 
            messages.success(request,("Sign in not succesfull!"))
            return redirect('login')
    return render (request , 'benefit/login.html' )    


def emp_login(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pk']
        user = authenticate(request,username=username , password=password)
        if user is not None :
            login(request, user)
            messages.success(request,("Sign in  succesfull!"))
            return redirect('emp_benefit')
        else :
            # message not implmented to the inside html 
            messages.success(request,("Sign in not succesfull!"))
            return redirect('emp_login')
    return render(request,'benefit/emp_login.html')
     
def logout_user(request):
    logout(request)
    messages.success(request,("logged out "))
    return redirect('/')

@login_required(login_url="login")
def notif(request):
    enroll = Notifications.objects.filter(state="admin").all().order_by('-date')
    if request.method == "POST" :
        submit = request.POST['submit']
        Notifications.objects.filter(id = submit).delete()      
    return render (request , 'benefit/notif.html',{'enrol':enroll} )

@login_required(login_url="login")
def hr(request):
    now = datetime.date.today()
    thirty_day_from_now = now + timedelta(days=30)
    enroll = Enrollement.objects.all()[:5]
    req  = Enrollement.objects.filter(state="pending").all()[:5:]
    benefits = Benefit.objects.all()[:5]
    type = Enrollement.objects.values('type').annotate(count=Count('id'))
    state_count = Enrollement.objects.values('state').annotate(count=Count('id'))
    tt= Enrollement.objects.values('type').annotate(cost=Sum('cost'))
    total_price =[item['cost'] for item in tt]
    types = [item['count'] for item in type]
    labels = [item['type'] for item in type]
    state = [item['state'] for item in state_count]
    state_num = [item['count'] for item in state_count]
  
    benefit = []
    if request.method == "POST":
        if 'submits' in request.POST:
            BId = request.POST['submits']
            date = request.POST['date']
            Benefit.objects.filter(id = BId).update(expiration_date=date)
    for t in benefits :
        if  t.expiration_date < thirty_day_from_now :
            benefit.append(t)
    for e in Enrollement.objects.all() :
        if e.type not in types :
            count  = Enrollement.objects.filter(type=e.type).count()
    return render (request , 'benefit/HRbenefit.html',{'enroll':enroll,'state':state,'state_num':state_num,'price':total_price,'benefit':benefit,'now':now,'req':req,'type':types,'label':labels,'ran':range (0,len(types))} )

@login_required(login_url="login")
def request(request):
    now = datetime.date.today()
    enroll = Enrollement.objects.all().order_by('-Request_date')
    benefit = Benefit.objects.all()
    if request.method == "POST":
        if 'approve' in request.POST:
            if 'cost' in request.POST:
                 cost = request.POST['cost']
                 approve = request.POST['approve']
                 Enrollement.objects.filter(id = approve).update(cost = cost ,enrollement_date=now,Request = 'no request',state="active")
            else:
                approve = request.POST['approve']
                Enrollement.objects.filter(id = approve).update(enrollement_date=now,Request = 'no request',state="active")
        if 'reject' in request.POST:
            reject = request.POST['reject']
            Enrollement.objects.filter(id = reject).update(enrollement_date=now,Request = 'no request',state="rejected")
    return render (request , 'benefit/request.html',{'enroll':enroll,'benefit':benefit} )

@login_required(login_url="emp_login")
def plans(request,eid):
    now = datetime.date.today()
    plan = Benefit.objects.all()
    em = CustomUser.objects.filter(email=eid).first()
    if request.method == "POST" :
       detail = request.POST['detail']
       cover = request.POST['cover']
       submit = request.POST['sub']
       ben = Benefit.objects.filter(name=submit).first()
       pname= em.firstname +" "+ em.last_name
       plans = Enrollement(user=eid , ename=pname,cost = ben.cost ,type = ben.type, bid = ben.id ,name = cover,expiration_date = ben.expiration_date , Request_date = now,state = "pending" ,Request = "Enrollement", detail = detail)
       plans.save() 
       notf = Notifications(user=em.email ,bid = ben.id, ename=pname, Request = "Enrollement",state = "admin",date = now , detail =detail)
       notf.save()       
    return render (request , 'benefit/plans.html',{'plans':plan,'time':now , 'eid':em.email} )

@login_required(login_url="emp_login")
def myenroll(request,eid):
    now = datetime.date.today()
    plan = Enrollement.objects.all()
    em = CustomUser.objects.filter(email=eid).first()
    if request.method == "POST" :
       if 'submit' in request.POST :
           date = request.POST['date']
           enrollId = request.POST['submit']
           Enrollement.objects.filter(id = enrollId).update(expiration_date=date,Request = 'date Expiration update',state="pending")             
       if 'submits' in request.POST :
           enrollId = request.POST['submits']
           Enrollement.objects.filter(id = enrollId).update(state = 'deactive')         
    return render (request , 'benefit/myenrol.html',{'plans':plan,'time':now , 'eid':em.email} )

@login_required(login_url="login")
def plan(request):
    now = datetime.date.today()
    plans = Benefit.objects.all()
    enroll = Enrollement.objects.all()
    if request.method == "POST" :
        if 'submit' in request.POST:
            enrollId = request.POST['submit']
            date = request.POST['date']
            elligible = request.POST['elligible']
            description  = request.POST['description']
            Benefit.objects.filter(id = enrollId).update(expiration_date = date , elligible = elligible , description = description)
        if 'submits' in request.POST:
            enrollIds = request.POST['submits']
            obj = get_object_or_404(Benefit, id = enrollIds)
            obj.delete()
        if 'search' in request.POST:
            search = request.POST['search']
            plans = Benefit.objects.filter(name = search).all()    
    return render (request , 'benefit/plan.html',{'plans':plans,'enroll':enroll,'time':now} )

@login_required(login_url="login")
def add(request): 
    if request.method == "POST" :
       name = request.POST['name']
       type = request.POST['type']
       description = request.POST['description']
       effective_date = request.POST['effective_date']
       expiration_date = request.POST['expiration_date']
       elligible = request.POST['elligible']
       cost = abs(int(request.POST['cost']))
       plans = Benefit(name=name ,cost = cost, type=type, description = description , effective_date = effective_date,expiration_date = expiration_date , elligible = elligible)
       plans.save()    
    return render (request , 'benefit/add.html' )

@login_required(login_url="emp_login")
def enroll(request, eid):
    now = datetime.date.today()
    user = CustomUser.objects.filter(email=eid).first()
    if request.method == "POST":
       user_name = eid
       ename = user.firstname +" "+ user.last_name
       name = request.POST['name']
       description = request.POST['detail']
       enrol_date = request.POST['enrol']
       expiration_date = request.POST['exp']
       types= request.POST['plan']
       plans = Enrollement(user = user_name , ename=ename, bid = 0 ,type = types ,Request_date=now, name = name,expiration_date = expiration_date , enrollement_date = enrol_date,state = "pending" ,Request = 'Other Enrollement', detail = description)
       plans.save()
       notf = Notifications(user=user_name,bid = 0, ename=ename, Request = "Other Enrollement",state = "admin",date = now , detail =description)
       notf.save()      
    
    return render (request , 'benefit/enroll.html',{ "user":user  }  )
        
@login_required(login_url="login")
def sum(request):
    now = datetime.date.today()
    plans = Enrollement.objects.all()
    if request.method == "POST" :
        if 'search' in request.POST:
            search = request.POST['search']
            plans = Enrollement.objects.filter(name = search).all() 

    return render (request , 'benefit/sum.html',{"plans":plans,"time":now} )
