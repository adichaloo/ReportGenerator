from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from django.views import View
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db import IntegrityError
#import pandas as pd
#from openpyxl import Workbook


"""def Excel(request):
    profile=Profile.objects.get(user=request.user)
    conf=Conferences.objects.filter(profile=profile)
    df=pd.DataFrame({'Activity','Title','State','Organizer'})
    df.to_excel('NamesAndAges.xlsx')
    return 0;"""
# Create your views here.
class Register(View):
    template2='Run/register.html'
    template1 = 'Run/login.html'
    def get(self,request):
        return render(request,self.template2,{})
    def post(self,request):
        try:
            user=User.objects.create_user(username=request.POST["username"],password=request.POST["password"])
            user.save()
            profile=Profile.objects.create(user=user)
            profile.save()
            return render(request,self.template2,{"reg":"Registered"})
        except IntegrityError:
            return render(request,self.template2,{"err":"Invalid registration"})

class Login(View):
    template='Run/login.html'
    template1='Run/postlogin.html'
    def get(self,request):
        return render(request,self.template,{})

    def post(self,request):
        user=authenticate(username=request.POST["username"],password=request.POST["password"])
       # p= Profile.objects.get(user=request.user)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('Run:postlogin')
        else:
            return render(request,self.template,{"err":"Invalid Login"})

def logoff(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('Run:login')

class Postlog(View):
    template1 = 'Run/postlogin.html'
    def get(self,request):
        args={'user':request.user}
        return render (request, self.template1,args)

class Student(View):
    template='Run/student.html'
    def get(self,request):
        return render(request,self.template,{})

class Faculty(View):
    template='Run/faculty.html'
    def get(self,request):
        return render(request,self.template,{})
class Conf(View):
    template='Run/conf.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            conference=Conferences.objects.filter(profile1=profile)
            return render(request,self.template,{"confo":conference})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):

        #confi=Conferences.objects.create(profile=Profile.objects.get(user=request.user),activity=request.POST["activity"],title=request.POST["title"],state=request.POST["state"],sponsor=request.POST["sponsor"],organizer=request.POST["organizer"])
        #confi.save()
        profile=Profile.objects.get(user=request.user)
        confi=Conferences(profile1=Profile.objects.get(user=request.user),activity=request.POST["activity"],title=request.POST["title"],state=request.POST["state"],sponsor=request.POST["sponsor"],organizer=request.POST["organizer"],date=request.POST["date"])
        confi.save()
        profile.conferences.add(confi)
        #conference=Conferences.objects.filter(profile=profile)
        #conference1=Conferences.objects.all()
        confer=profile.conferences.all()

        context={"confo":confer}
        return render(request,self.template,context)

def conf_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        conference=Profile.objects.filter(conferences__profile1=profile)
        return render(request,'Run/conf.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Conferences,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        conference=Profile.objects.filter(conferences__profile1=profile)
        return redirect('../conf')

class Web(View):
    template1='Run/web.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            #conference1=Profile.objects.filter(webinars__profile1=profile)
            conference1=profile.webinars.all()
            return render(request,self.template1,{"confo":conference1})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):
        profile=Profile.objects.get(user=request.user)
        confi1=Webinars(profile1=Profile.objects.get(user=request.user),activity=request.POST["activity"],title=request.POST["title"],speaker=request.POST["speaker"],number=request.POST["number"],date=request.POST["date"],remark=request.POST["remark"],file=request.FILES["file"])
        fs=FileSystemStorage()
        fs.save(file.name,file)
        confi1.save()
        profile.webinars.add(confi1)
        confer=profile.webinars.all()

        context={"confo":confer}
        return render(request,self.template1,context)


def web_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        #conference=Profile.objects.filter(webinars__profile1=profile)
        conference=profile.webinars.all()
        return render(request,'Run/web.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Webinars,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        #conference=Profile.objects.filter(webinars__profile1=profile)
        profile.webinars.all()
        return redirect('../web')


class Collaboration(View):
    template='Run/collab.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            #conference=Profile.objects.filter(collab__profile1=profile)
            conference=profile.collab.all()
            return render(request,self.template,{"confo":conference})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):

        confi=Collab(profile1=Profile.objects.get(user=request.user),activity=request.POST["activity"],title=request.POST["title"],period=request.POST["period"],coordinator=request.POST["coordinator"],remark=request.POST["remark"])
        confi.save()
        profile=Profile.objects.get(user=request.user)
        profile.collab.add(confi)
        conference=profile.collab.all()
        context={"confo":conference}
        return render(request,self.template,context)



def collab_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        #conference=Profile.objects.filter(collab__profile1=profile)
        conference=profile.collab.all()
        return render(request,'Run/collab.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Collab,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        conference=profile.collab.all()
        #conference=Profile.objects.filter(collab__profile1=profile)
        return redirect('../collab')


class Ind(View):
    template='Run/coi.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            conference=profile.COI.all()

            return render(request,self.template,{"confo":conference})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):

        confi=Certify(profile1=Profile.objects.get(user=request.user),activity=request.POST["activity"],title=request.POST["title"],invest=request.POST["invest"],remark=request.POST["remark"])
        confi.save()
        #ball=Bio.objects.create(profile=Profile.objects.get(user=request.user),COI=confi)
        #ball.save()
        profile=Profile.objects.get(user=request.user)
        profile.COI.add(confi)
        conference=profile.COI.all()
        #conference1=Conferences.objects.all()
        #print(conference)
        context={"confo":conference}
        return render(request,self.template,context)

def coi_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        conference=profile.COI.all()
        return render(request,'Run/coi.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Certify,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        conference=profile.COI.all()
        return redirect('../coi')


class Laboratory(View):
    template='Run/isl.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            conference=profile.labo.all()
            return render(request,self.template,{"confo":conference})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):
        confi=Industry(profile1=Profile.objects.get(user=request.user),activity=request.POST["activity"],lab=request.POST["lab"],grant=request.POST["grant"],year=request.POST["year"],scope=request.POST["scope"])
        confi.save()
        profile=Profile.objects.get(user=request.user)
        profile.labo.add(confi)
        conference=profile.labo.all()
        context={"confo":conference}
        return render(request,self.template,context)

def isl_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        conference=profile.labo.all()
        return render(request,'Run/isl.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Industry,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        conference=profile.labo.all()
        return redirect('../isl')



class RG(View):
    template='Run/rgs.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            conference=profile.research1.all()

            return render(request,self.template,{"confo":conference})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):

        confi=Research1(profile1=Profile.objects.get(user=request.user),head=request.POST["head"],title=request.POST["title"],authority=request.POST["authority"],grant=request.POST["grant"],period=request.POST["period"],date=request.POST["date"],order=request.POST["order"])
        confi.save()
        #ball=Bio.objects.create(profile=Profile.objects.get(user=request.user),Research_Grants=confi)
        #ball.save()
        profile=Profile.objects.get(user=request.user)
        profile.research1.add(confi)
        conference=profile.research1.all()
        context={"confo":conference}
        return render(request,self.template,context)

def rgs_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        conference=profile.research1.all()
        return render(request,'Run/rgs.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Research1,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        conference=profile.research1.all()
        return redirect('../rgs')


class RG1(View):
    template='Run/rgd.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            conference=profile.research2.all()

            return render(request,self.template,{"confo":conference})
        else:
            return render(request,'Run/postlogin.html',{})
    def post(self,request):

        confi=Research2(profile1=Profile.objects.get(user=request.user),head=request.POST["head"],title=request.POST["title"],authority=request.POST["authority"],grant=request.POST["grant"],period=request.POST["period"],date=request.POST["date"],order=request.POST["order"])
        confi.save()
        #ball=Bio.objects.create(profile=Profile.objects.get(user=request.user),Research_Industry=confi)
        #ball.save()
        profile=Profile.objects.get(user=request.user)
        profile.research2.add(confi)
        conference=profile.research2.all()
        #conference1=Conferences.objects.all()
        print(conference)
        context={"confo":conference}
        return render(request,self.template,context)


def rgd_delete(request,id=None):
    if id is None:
        profile=Profile.objects.get(user=request.user)
        conference=profile.research2.all()
        return render(request,'Run/rgd.html',{"confo":conference})
    #pro=pro1.profile.user.username
    #if request.method == "POST" and request.user.is_authenticated and request.user.username == pro:
    else:
        pro1=get_object_or_404(Research2,id=id)
        pro1.delete()
        profile=Profile.objects.get(user=request.user)
        conference=profile.research2.all()
        return redirect('../rgd')

class Report(View):
    template='Run/reports.html'
    def get(self,request):
        if request.user.is_authenticated:
            profile=Profile.objects.get(user=request.user)
            conf=profile.conferences.all()
            web=profile.webinars.all()
            return render(request,self.template,{"conf":conf,"web":web})


def is_valid_queryparam(param):
    return param != '' and param is not None

class Sorter(View):
    def get(self,request):
        if request.user.is_superuser:
            return render(request,"Run/sorting.html",{"qs":None})

    def post(self,request):
        print("Hello")
        activity_query = request.POST['title_contains']
        name_query = request.POST['id_exact']
        date_min = request.POST['date_min']
        date_max = request.POST['date_max']
        print(activity_query)
        if is_valid_queryparam(activity_query):
            qs=Profile.objects.filter(Q(conferences__activity__icontains=activity_query)|Q(webinars__activity__icontains=activity_query))
        print(qs)
        return render(request,"Run/sorting.html",{'qs':qs})
    #def post(self,request):"""
