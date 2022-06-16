<<<<<<< HEAD
=======
from unicodedata import name
from django.shortcuts import render

>>>>>>> ebe34fe2a8e34306b4ee1040199bd91ba52af90f
import json
import re 
import bcrypt
import jwt

from django.http  import JsonResponse
from django.views import View

from westagram.settings import SECRET_KEY
from users.models import User

class SignUpView(View):
    def post(self, request) :
        try:
            data          = json.loads(request.body)
            last_name     = data['last_name']
            first_name    = data['first_name']
            email         = data['email']
            password      = data['password']
            line          = data['line']
          
            EMAIL_CHECK = '^[a-zA-z0-9+_.]+@[a-zA-z0-9-.]+\.[a-zA-z0-9-.]+$'
            PW_CHECK    = '^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{8,}$'
            
            if not re.match(EMAIL_CHECK, email) :
<<<<<<< HEAD
                return JsonResponse({'Message': 'INVALID_EMAIL'}, status=400)
            
            if not re.match(PW_CHECK, password) :
                return JsonResponse({'Message': 'INVALID_PASSWORD'}, status=400)
                
            if User.objects.filter(email = email).exists() :
                return JsonResponse({'Message': 'EMAIL_ALREADY_EXIST'}, status=400)
            
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
=======
                return JsonResponse({"message": "INVALID_EMAIL"}, status=400)
            
            if not re.match(PW_CHECK, password) :
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)
                
            if User.objects.filter(email = email).exists() :
                return JsonResponse({"message": "EMAIL_ALREADY_EXIST"}, status=400)
>>>>>>> ebe34fe2a8e34306b4ee1040199bd91ba52af90f

            User.objects.create(
                last_name     = data['last_name'],
                first_name    = data['first_name'],
                email         = data['email'],
                password      = hashed_password,
                line          = data['line']
                )
            return JsonResponse({'message': 'SUCCESS'}, status=201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class LogInView(View):
    def post(self, request) :
<<<<<<< HEAD
        try :
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
=======
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists():
                return JsonResponse({"message": "INVALIED_USER"}, status=401)

            if not User.objects.filter(email=email, password=password).exists():
                return JsonResponse({"message": "INVALIED_USER"}, status=401)
>>>>>>> ebe34fe2a8e34306b4ee1040199bd91ba52af90f

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401
                )
            if not bcrypt.checkpw(password.encode('utf-8'), User.objects.get(email=data['email']).password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)

            token = jwt.encode({'email':email}, SECRET_KEY, algorithm='HS256')
            return JsonResponse({'access_token' : token}, status=201)
        except KeyError:
<<<<<<< HEAD
            return JsonResponse({'message':'KEY_ERROR'},status=400)
=======
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
>>>>>>> ebe34fe2a8e34306b4ee1040199bd91ba52af90f
