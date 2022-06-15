from unicodedata import name
from weakref import KeyedRef
from django.shortcuts import render

import json
import re


from django.http  import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View):
    def post(self, request) :
        try:
            data          = json.loads(request.body)
            last_name     = data["last_name"]
            first_name    = data["first_name"]
            email         = data["email"]
            password      = data["password"]
            line          = data["line"]

            EMAIL_CHECK = "^[a-zA-z0-9+_.]+@[a-zA-z0-9-.]+\.[a-zA-z0-9-.]+$"
            PW_CHECK    = "^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{8,}$"
            
            if not re.match(EMAIL_CHECK, email) :
                return JsonResponse({"Message": "INVALID_EMAIL"}, status=400)
            
            if not re.match(PW_CHECK, password) :
                return JsonResponse({"Message": "INVALID_PASSWORD"}, status=400)
                
            if User.objects.filter(email = email).exists() :
                return JsonResponse({"Message": "EMAIL_ALREADY_EXIST"}, status=400)

            User.objects.create(
                last_name     = last_name,
                first_name    = first_name,
                email         = email,
                password      = password,
                line          = line  
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LogInView(View):
    def post(self, request) :
        try:
            data          = json.loads(request.body)
            email         = data['email']
            password      = data['password']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"Message": "EMAIL_ERROR"}, status=400)
            if not User.objects.filter(password=password).exists():
                return JsonResponse({"Message": "PASSWORD_ERROR"}, status=400)

            return JsonResponse({"message": "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"Message": "KEY_ERROR"}, status=400)

