import json
import re

import bcrypt
import jwt
from django.http  import JsonResponse
from django.views import View

from users.models        import User
from westagram.settings  import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data            = json.loads(request.body)
            first_name      = data['first_name']
            last_name       = data['last_name']
            user_name       = data['user_name']
            email           = data['email']
            password        = data['password']
            phone_number    = data['phone_number']
            date_of_birth   = data['date_of_birth']

            EMAIL_VALIDATION    = '^[a-zA-z0-9+_.]+@[a-zA-z0-9-.]+\.[a-zA-z0-9-.]+$'
            PASSWORD_VALIDATION = '^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{8,}$'

            if not re.match(EMAIL_VALIDATION, email):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

            if not re.match(PASSWORD_VALIDATION, password):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)

            if User.objects.filter(user_name = user_name).exists():
                return JsonResponse({'message': 'USER_NAME_ALREADY_IN_USE'}, status=400)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'EMAIL_ALREADY_IN_USE'}, status=400)

            if User.objects.filter(phone_number = phone_number).exists():
                return JsonResponse({'message': 'PHONE_NUMBER_ALREADY_IN_USE'}, status=400)

            hashed_password  = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            decoded_password = hashed_password.decode('utf-8')

            User.objects.create(
                first_name    = first_name,
                last_name     = last_name,
                user_name     = user_name,
                email         = email,
                password      = decoded_password,
                phone_number  = phone_number,
                date_of_birth = date_of_birth
            )
            return JsonResponse({'message': 'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

class SignInView(View):
    def post(self, request):
        try:
            data        = json.loads(request.body)
            email       = data['email']
            password    = data['password']

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            valid_user = User.objects.get(email = email)

            if not bcrypt.checkpw(password.encode('utf-8') , valid_user.password.encode('utf-8')):
                return JsonResponse({'message': 'INVALID_USER'}, status=401)

            token = jwt.encode({'user_id': valid_user.id}, SECRET_KEY, ALGORITHM)

            return JsonResponse({'token': token}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
