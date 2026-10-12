# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views import View

# from .models import *
# # Create your views here.

# class loginview(View):
#     def  get(self,request):
#         return render(request,"login.html")
#     def post(self,request):
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         try:
#             obj=logintable.objects.get(username=username, password=password)
#             request.session['user_id']=obj.id
#             if obj.user_type=='admin':
#                 return HttpResponse('''<script>alert("Login successful");window.location='/home'</script>''')
#             else:
#                 return HttpResponse('''<script>alert("Invalid User");window.location='/'</script>''')
#         except logintable.DoesNotExist:
#             return HttpResponse('''<script>alert("Invalid Credentials");window.location='/'</script>''')
# class homepageview(View):
#     def get(self,request):
#         return render(request,"homepage.html")
# class complaintview(View):
#     def get(self,request):
#         return render(request,"viewcomplaints&reply.html")
# class membersview(View):
#     def get(self,request):
#         return render(request,"viewmembers.html")
# class ratingview(View):
#     def get(self,request):
#         return render(request,"viewrating.html")
# class usersview(View):
#     def get(self,request):
#         c=usertable.objects.all()
#         return render(request,"viewuser.html",{'user':c})







#     # API



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class RegisterView(APIView):
#     def post(self,request):
#         name=request.data.get("name")
#         email=request.data.get("email")
#         password=request.data.get("password")

#         if not name or not email or not password:
#             return Response({"error":"name,email,and password are required"},status=status.HTTP_400_BAD_REQUEST)
#         # check if email already registered
#         if logintable.objects.filter(username=email).exists():
#             return Response({"error":"Email already registered"},status=status.HTTP_409_CONFLICT)
#         login_obj=logintable.objects.create(
#             username=email,
#             password=password,
#             user_type="user"
#         )
#         user_obj=usertable.objects.create(
#             name=name,
#             email=email,
#             login_id=login_obj
#         )
#         return Response({
#         "message":"registration successful",
#         "user_id":user_obj.id,
#         "name":name,
#         "email":email,
#         "is_profile_completed":False
#         }, status=status.HTTP_201_CREATED)



# class LoginView(APIView):
#     def post(self,request):
#         email=request.data.get('email')
#         password=request.data.get("password")
#         print(email)
#         print(password)
#         if not  email or not password:
#             return Response({"error":"name,email,and password are required"},status=status.HTTP_400_BAD_REQUEST)

#         try:
#             login_obj=logintable.objects.get(username=email, password=password)
#         except logintable.DoesNotExist:
#             return Response({"error":"Invalid email or password"},status=status.HTTP_401_UNAUTHORIZED)

#         #Get the linked user profile 
#         try:
#             user_obj=usertable.objects.get(login_id=login_obj)
#         except usertable.DoesNotExist:
#             return Response({"error":"  User profile is not found "},status=status.HTTP_404_NOT_FOUND)
#         is_profile_completed = bool(
#             user_obj.height and user_obj.weight and user_obj.age
#         )

#         return Response({
#             "message":"Login successful",
#             "user_id":user_obj.id,
#             "name":user_obj.name,
#             "email":user_obj.email,
#             "user_type":login_obj.user_type,
#             "is_profile_completed":is_profile_completed
#         },status=status.HTTP_200_OK)



# class ProfileView(APIView):
     
#     def get(self,request,user_id):
#             try:
#                 user_obj=usertable.objects.get(id=user_id)
#             except usertable.DoesNotExist:
#                 return Response({"error":"User not found"},status=status.HTTP_404_NOT_FOUND)

#             return Response({
#                 "user_id":user_obj.login_id,
#                 "name":user_obj.name,
#                 'email':user_obj.email,
#                 'age':user_obj.age,
#                 'gender':user_obj.gender,
#                 'height':user_obj.height,
#                 'weight':user_obj.weight,
#                 'bmi':user_obj.bmi,
#                 },status=status.HTTP_200_OK)
#     def post(self,request,user_id):

#                 try:
#                     print(request.data)
#                     user_obj=usertable.objects.get(id=user_id)
#                     print(user_obj)
#                 except usertable.DoesNotExist:
#                     return Response({"error":"User not found"},status=status.HTTP_404_NOT_FOUND)

#                 user_obj.name =request.data.get("name",user_obj.name)
#                 user_obj.age =request.data.get("age",user_obj.name)
#                 user_obj.gender =request.data.get("gender",user_obj.name)
#                 user_obj.height =request.data.get("height",user_obj.name)
#                 user_obj.weight =request.data.get("weight",user_obj.name)
#                 user_obj.bmi =request.data.get("bmi",user_obj.name)
#                 user_obj.save()
#                 return Response({
#                     "message":"Profile Updated Successfully ",
#                     "user_id":user_obj.login_id,
#                     "name":user_obj.name,
#                     "email":user_obj.email,
#                     "age":user_obj.age,
#                     "gender":user_obj.gender,
#                     "height":user_obj.height,
#                     "weight":user_obj.weight,
#                     "bmi":user_obj.bmi,
#                 },status=status.HTTP_200_OK)
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

#########################APIVIEW#######################################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *


class RegisterView(APIView):

    def post(self, request):
        print("############### REQUEST DATA:", request.data)
        response_dict = {}

        # Map incoming data to each serializer
        login_data = {
            'username': request.data.get('email'),
            'password': request.data.get('password'),
        }
        user_data = {
            'name' : request.data.get('name'),
            'email': request.data.get('email'),
        }

        login_serial = Loginserializers(data=login_data)
        user_serial  = Userseralizers(data=user_data)

        login_valid = login_serial.is_valid()
        user_valid  = user_serial.is_valid()

        print("LOGIN VALID  :", login_valid)
        print("USER VALID   :", user_valid)
        print("LOGIN ERRORS :", login_serial.errors)
        print("USER ERRORS  :", user_serial.errors)

        if login_valid and user_valid:
            # Check if email already registered
            if logintable.objects.filter(username=request.data.get('email')).exists():
                response_dict['message'] = 'failed'
                response_dict['error']   = 'Email already registered'
                return Response(response_dict, status=status.HTTP_409_CONFLICT)

            login_obj = login_serial.save(user_type='user')
            user_obj  = user_serial.save(login_id=login_obj)

            response_dict['message']            = 'success'
            response_dict['login_id']            = login_obj.id
            response_dict['is_profile_completed'] = False
            response_dict['user']               = Userseralizers(user_obj).data
            return Response(response_dict, status=status.HTTP_201_CREATED)

        response_dict['message']     = 'failed'
        response_dict['login_error'] = login_serial.errors if not login_valid else None
        response_dict['user_error']  = user_serial.errors  if not user_valid  else None
        return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        print("############### REQUEST DATA:", request.data)
        response_dict = {}

        email    = request.data.get('email')
        password = request.data.get('password')
        print("EMAIL:", email)

        if not email or not password:
            response_dict['message'] = 'field'
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

        login_obj = logintable.objects.filter(username=email, password=password).first()
        print("LOGIN OBJ:", login_obj)

        if not login_obj:
            response_dict['message'] = 'failed'
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        user_obj = usertable.objects.filter(login_id=login_obj).first()
        if not user_obj:
            response_dict['message'] = 'failed'
            response_dict['error']   = 'User profile not found'
            return Response(response_dict, status=status.HTTP_404_NOT_FOUND)

        is_profile_completed = bool(user_obj.height and user_obj.weight and user_obj.age)

        response_dict['message']              = 'success'
        response_dict['login_id']            = login_obj.id
        response_dict['user_type']            = login_obj.user_type
        response_dict['is_profile_completed'] = is_profile_completed
        response_dict['user']                 = Userseralizers(user_obj).data
        return Response(response_dict, status=status.HTTP_200_OK)


class ProfileView(APIView):

    def get(self, request, user_id):
        print("GET PROFILE user_id:", user_id)
        response_dict = {}

        user_obj = usertable.objects.filter(login_id_id=user_id).first()
        if not user_obj:
            response_dict['message'] = 'failed'
            return Response(response_dict, status=status.HTTP_404_NOT_FOUND)

        response_dict['message'] = 'success'
        response_dict['user']    = Userseralizers(user_obj).data
        return Response(response_dict, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        print(" PUT PROFILE user_id:", user_id)
        response_dict = {}

        user_obj = usertable.objects.filter(login_id__id=user_id).first()
        if not user_obj:
            response_dict['message'] = 'failed'
            return Response(response_dict, status=status.HTTP_404_NOT_FOUND)

        user_serial = Userseralizers(user_obj, data=request.data, partial=True)

        print("USER VALID  :", user_serial.is_valid())
        print("USER ERRORS :", user_serial.errors)

        if user_serial.is_valid():
            user_serial.save()
            response_dict['message'] = 'success'
            response_dict['user']    = user_serial.data
            return Response(response_dict, status=status.HTTP_200_OK)

        response_dict['message'] = 'failed'
        response_dict['error']   = user_serial.errors
        return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

class FamilyMembersView(APIView):
   def get(self, request, user_id):
        print("FAMILY MEMBERS GET METHOD CALLED")
        print("USER ID:", user_id)

        response_dict = {}
        user_obj = usertable.objects.filter(login_id__id=user_id).first()
        if not user_obj:
            return Response({
                'message': 'failed',
                'error': 'User not found'
            }, status=status.HTTP_404_NOT_FOUND)

        members = memberstable.objects.filter(
            user_id=user_obj
        ).order_by('-id')

        serializer = Memberserializers(members, many=True)
        response_dict['message'] = 'success'
        response_dict['members'] = serializer.data

        print("GET RESPONSE:", response_dict)
        return Response(response_dict, status=status.HTTP_200_OK)
   def post(self,request,user_id):
        print("$$$$$$$$$$$$ ADD FAMILY MEMBER user_id :",user_id,"DATA:",request.data)
        response_dict={}

        user_obj=usertable.objects.filter(login_id__id=user_id).first()
        if not user_obj:
            response_dict['message']='Failed'
            response_dict['error']='User not found'
            return Response(response_dict,status=status.HTTP_404_NOT_FOUND)

        data=request.data.copy() if hasattr(request.data,"copy") else dict(request.data)


    #Convert list fields(like health condition into comma sections)
        for list_field in['condition','allergies']:
            val= data.get(list_field)
        if isinstance(val,list):
            data[list_field]=",".join([str(x).strip() for x in val if str(x).strip()])

    #set health summary description if not explicitly provided
        if not data.get('health'):
            health_status=data.get('health_status','Normal')
            if health_status=='patient':
                data['health']=data.get('condition') or 'patient'
            elif health_status=='pregnant':
                data['health']=f"pregnant-{data.get('trimester','')}".strip()
            else:
                data['health']='Healthy/Normal'

        #set is_pregnant boolean based on health_status or parameter
        if data.get('health_status')=='pregnant' or str(data.get('is_pregnant',"")).lower() in ['true','1']:
            data['is_pregnant']=True
        else:
            data['is_pregnant']=False

        serializers=Memberserializers(data=data)
        if serializers.is_valid():
            member_obj=serializers.save(user_id=user_obj)
            response_dict['message']='success'
            response_dict['member']=Memberserializers(member_obj).data
            return Response(response_dict,status=status.HTTP_201_CREATED)

        print("MEMBER ERROR:",serializers.errors)
        response_dict['message']='failed'
        response_dict['error']=serializers.errors
        return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)




class MemberDetailsView(APIView):

    def get(self, request, member_id):
        print("######------------####### GET MEMBER DETAILS member_id:", member_id)

        response_dict = {}
        member = memberstable.objects.filter(user_id__id=member_id).first()
        print('------------', member)

        if not member:
            response_dict['message'] = 'failed'
            response_dict['error'] = 'Member not found'
            return Response(response_dict, status=status.HTTP_404_NOT_FOUND)

        response_dict['message'] = 'success'
        response_dict['member'] = Memberserializers(member).data

        return Response(response_dict, status=status.HTTP_200_OK)

    def put(self, request, member_id):
        print("############# UPDATE MEMBER member_id:", member_id, "DATA", request.data)

        response_dict = {}
        member = memberstable.objects.filter(id=member_id).first()

        if not member:
            response_dict['message'] = 'failed'
            response_dict['error'] = 'Member not found'
            return Response(response_dict, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()

        # Convert list values to comma-separated strings
        for list_field in ['conditions', 'allergies', 'food_allergies']:
            value = data.get(list_field)

            if isinstance(value, list):
                data[list_field] = ', '.join(
                    str(item).strip()
                    for item in value
                    if str(item).strip()
                )

        # Handle pregnancy and health status
        health_status = data.get('health_status', '')

        if health_status.lower() == 'pregnant':
            data['is_pregnant'] = True

            if not data.get('health'):
                data['health'] = f"Pregnant - {data.get('trimester', '')}".strip()

        elif health_status.lower() == 'patient':
            data['is_pregnant'] = False

            if not data.get('health'):
                data['health'] = data.get('conditions') or 'Patient'

        else:
            data['is_pregnant'] = False

            if not data.get('health'):
                data['health'] = 'Healthy / Normal'

        serializer = Memberserializers(
            member,
            data=data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            response_dict['message'] = 'success'
            response_dict['member'] = serializer.data

            return Response(response_dict, status=status.HTTP_200_OK)

        response_dict['message'] = 'failed'
        response_dict['errors'] = serializer.errors

        return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, member_id):
        print("$$$$$$$$$$$$$ DELETE MEMBER member_id:", member_id)

        response_dict = {}
        member = memberstable.objects.filter(id=member_id).first()

        if not member:
            response_dict['message'] = 'failed'
            response_dict['errors'] = 'Member not found'
            return Response(response_dict, status=status.HTTP_404_NOT_FOUND)

        member.delete()

        response_dict['message'] = 'success'

        return Response(response_dict, status=status.HTTP_200_OK)
