from django.shortcuts import render

# Create your views here.
import json, re

from django.http import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View):
  
  def post(self, request) :
   try:
    data          = json.loads(request.body)
    last_name     = data["last_name"]
    first_name    = data["first_name"]
    email         = data["email"]
    account       = data["account"]
    pw            = data["password"]
    phone_number  = data["phone_number"]
    birth         = data["date_of_birth"]

    EMAIL_CHECK = "^[a-zA-z0-9+_.]+@[a-zA-z0-9-.]+\.[a-zA-z0-9-.]+$"
    PW_CHECK    = "^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[a-zA-Z\d@$!%*#?&]{8,}$"

    if User.objects.filter(email = email).exists() :
      return JsonResponse({"Message": "EMAIL_ALREADY_EXIST"}, status=400)
    
    if not re.match(EMAIL_CHECK, email) :
      return JsonResponse({"Message": "INVALID_EMAIL"}, status=400)
    
    if not re.match(PW_CHECK, pw) :
      return JsonResponse({"Message": "INVALID_PASSWORD"}, status=400)

    User.objects.create(
      last_name     = last_name,
      first_name    = first_name,
      email         = email,
      account       = account,
      password      = pw,
      phone_number  = phone_number,
      date_of_birth = birth       
    )

    return JsonResponse({"message": "SUCCESS"}, status=201)
   
   except:
    return JsonResponse({"message": "KEY_ERROR"}, status=400)