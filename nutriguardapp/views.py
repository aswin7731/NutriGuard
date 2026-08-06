from django.shortcuts import render
from django.views import View
# Create your views here.

class loginview(View):
    def  get(self,request):
        return render(request,"login.html")
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
        return render(request,"viewuser.html")