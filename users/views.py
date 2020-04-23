from django.shortcuts import render
from django.shortcuts import render
# Imports For Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Imports For JSONResponse 
from django.http import JsonResponse, request
import json
# Imports For Database
from django.db import IntegrityError
from django.db import models
from .models import users,users_details

def resgistration(post_info):
    reg_name  = post_info["uname"]
    reg_email = post_info["uemail"]
    reg_pass  = post_info["upass"]
    
    try:
        insert =users(uemail=reg_email, uname=reg_name,upass=reg_pass)
        print(users.objects.all())
        insert.save()

        insert1 = users_details(uemail=reg_email, fname=reg_name, upass=reg_pass)
        insert1.uid = insert
        
        reg_mes = "Registration Success"
        return reg_mes
        
    except IntegrityError as e:
        reg_mes = "Duplicate Email"
        return reg_mes

class RegistrationAPI(APIView):
    def post(self,request,format='json'):
        try:
            post_info=json.loads((request.body).decode('utf-8'))
            reg_mes=resgistration(post_info)
            return JsonResponse(reg_mes,safe=False)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)