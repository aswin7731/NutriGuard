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







    # API



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    def post(self,request):
        name=request.data.get("name")
        email=request.data.get("email")
        password=request.data.get("password")

        if not name or not email or not password:
            return Response({"error":"name,email,and password are required"},status=status.HTTP_400_BAD_REQUEST)
        # check if email already registered
        if logintable.objects.filter(username=email).exists():
            return Response({"error":"Email already registered"},status=status.HTTP_409_CONFLICT)
        login_obj=logintable.objects.create(
            username=email,
            password=password,
            user_type="user"
        )
        user_obj=usertable.objects.create(
            name=name,
            email=email,
            login_id=login_obj
        )
        return Response({
        "message":"registration successful",
        "user_id":user_obj.id,
        "name":name,
        "email":email
        }, status=status.HTTP_201_CREATED)



class LoginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get("password")
        print(email)
        print(password)
        if not  email or not password:
            return Response({"error":"name,email,and password are required"},status=status.HTTP_400_BAD_REQUEST)

        try:
            login_obj=logintable.objects.get(username=email, password=password)
        except logintable.DoesNotExist:
            return Response({"error":"Invalid email or password"},status=status.HTTP_401_UNAUTHORIZED)

        #Get the linked user profile 
        try:
            user_obj=usertable.objects.get(login_id=login_obj)
        except usertable.DoesNotExist:
            return Response({"error":"  User profile is not found "},status=status.HTTP_404_NOT_FOUND)


        return Response({
            "message":"Login successful",
            "user_id":user_obj.id,
            "name":user_obj.name,
            "email":user_obj.email,
            "user_type":login_obj.user_type
        },status=status.HTTP_200_OK)



    class ProfileView(APIView):
        def get(self,request,user_id):
            try:
                user_obj=usertable.objects.get(id=user_id)
            except usertable.DoesNotExist:
                return Response({"error":"User not found"},status=status.HTTP_404_NOT_FOUND)

            return Response({
                "user_id":user_obj.login_id,
                "name":user_obj.name,
                'email':user_obj.email,
                'age':user_obj.age,
                'gender':user_obj.gender,
                'height':user_obj.height,
                'weight':user_obj.weight,
                'bmi':user_obj.bmi,
            },status=status.HTTP_200_OK)


        def put(self,request,user_id):
            try:
                user_obj=usertable.objects.get(id=user_id)
            except usertable.DoesNotExist:
                return Response({"error":"User not found"},status=status.HTTP_404_NOT_FOUND)

            user_obj.name =request.data.get("name",user_obj.name)
            user_obj.age =request.data.get("age",user_obj.name)
            user_obj.gender =request.data.get("gender",user_obj.name)
            user_obj.height =request.data.get("height",user_obj.name)
            user_obj.weight =request.data.get("weight",user_obj.name)
            user_obj.bmi =request.data.get("bmi",user_obj.name)
            user_obj.save()
            return Response({
                "message":"Profile Updated Successfully ",
                "user_id":user_obj.login_id,
                "name":user_obj.name,
                "email":user_obj.email,
                "age":user_obj.age,
                "gender":user_obj.gender,
                "height":user_obj.height,
                "weight":user_obj.weight,
                "bmi":user_obj.bmi,
            },status=status.HTTP_200_OK)


