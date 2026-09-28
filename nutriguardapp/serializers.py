from rest_framework import serializers
from.models import *




   

class Loginserializers(serializers.ModelSerializer):
   class Meta:
       model=logintable
       fields=['username','password','user_type']

class Userseralizers(serializers.ModelSerializer):
    class Meta:
        model=usertable
        fields=['name','age','gender','email','height','weight','bmi','health_condition','food_allergies']


class Packetfoodseializers(serializers.ModelSerializer):
    class Meta:
        model=packetfoodtable
        fields=['product_name','brand','category','barcode','ingredient','image_url']


class Complaintserializers(serializers.ModelSerializer):
    class Meta:
        model:complaintstable
        fields=['user_id','complaint','reply','send_date','reply_date']


class Ratingserializers(serializers.ModelSerializer):
    class Meta:
        model=ratingtable
        fields=['user_id','rating','send_date']

class Memberserializers(serializers.ModelSerializer):
    class Meta:
        model=memberstable
        fields=['user_id','name','age','gender','height','weight','bmi','health','allergies','is_pregnant','relation','created_time']



class Bmiserializers(serializers.ModelSerializer):
    class Meta:
        model=bmitable
        fields=['user_id','height','weight','bmi','recorded_time']

class Histroyserializers(serializers.ModelSerializer):
    class Meta:
        model=historytable
        fields=['user_id','product_id','health_score','scanned_date']

