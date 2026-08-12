from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *
# Create your views here.

class loginview(View):
    def  get(self,request):
        return render(request,"login.html")
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            obj=logintable.objects.get(username=username, password=password)
            request.session['user_id']=obj.id
            if obj.user_type=='admin':
                return HttpResponse('''<script>alert("Login successful");window.location='/home'</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid User");window.location='/'</script>''')
        except logintable.DoesNotExist:
            return HttpResponse('''<script>alert("Invalid Credentials");window.location='/'</script>''')
class homepageview(View):
    def get(self,request):
        return render(request,"homepage.html")
class complaintview(View):
    def get(self,request):
        return render(request,"viewcomplaints&reply.html")
class membersview(View):
    def get(self,request):
        return render(request,"viewmembers.html")
class ratingview(View):
    def get(self,request):
        return render(request,"viewrating.html")
class usersview(View):
    def get(self,request):
        c=usertable.objects.all()
        return render(request,"viewuser.html",{'user':c})