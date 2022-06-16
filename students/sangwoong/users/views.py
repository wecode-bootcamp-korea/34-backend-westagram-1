import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from westagram.settings import ALGORITHM, SECRET_KEY
from users.models import User

class SignUpView(View):
    def post(self, request) :
        try:
            data          = json.loads(request.body)
            last_name     = data["last_name"]
            first_name    = data["first_name"]
            email         = data["email"]
            account       = data["account"]
            password      = data["password"]
            phone_number  = data["phone_number"]
            date_of_birth = data["date_of_birth"]
            
            EMAIL_CHECK   = "^[a-zA-z0-9+_.]+@[a-zA-z0-9-.]+\.[a-zA-z0-9-.]+$"
            PW_CHECK      = "^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{8,}$"
            
            if not re.match(EMAIL_CHECK, email) :
                return JsonResponse({"message": "INVALID_EMAIL"}, status=400)
            
            if not re.match(PW_CHECK, password) :
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=400)
                
            if User.objects.filter(email = email).exists() :
                return JsonResponse({"message": "EMAIL_ALREADY_EXIST"}, status=400)
            
            encoded_password = password.encode("utf-8")
            secret_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            decoded_password = secret_password.decode("utf-8")

            User.objects.create(
                last_name     = last_name,
                first_name    = first_name,
                email         = email,
                account       = account,
                password      = decoded_password,
                phone_number  = phone_number,
                date_of_birth = date_of_birth       
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)

        except KeyError :
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data          = json.loads(request.body)
            user_account  = data["account"]
            user_password = data["password"]
            
            user           = User.objects.get(account = user_account)
            input_password = user_password.encode("utf-8")
            saved_password = user.password.encode("utf-8")
            
            if not bcrypt.checkpw(input_password, saved_password) :
                return JsonResponse({"message" : "INVALID_USER"}, status=401)

            access_token = jwt.encode({"user_id" : user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({"access_token": access_token, "message": "SUCCESS"}, status=200)
        
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)