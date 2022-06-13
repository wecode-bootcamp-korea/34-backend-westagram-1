from pdb import line_prefix
from unicodedata import name
from django.shortcuts import render

import json
import re

from django.http    import JsonResponse
from django.views   import View

from models        import User

class SignUpView(View):  
    def post(self, request):
        try: 
            data= json.loads(request.body)

            name = data['name']
            line = data['line']
            email = data['email']
            password = data['password']

            email_reg     = '@+.'
            password_reg  = '[0-9]+[a-zA-Z]'

            if not re.match(email, email_reg):
                return JsonResponse({"message": "KEY_ERROR"}, status=400)

            if password.count <= 8 :
                return JsonResponse({"message": "KEY_ERROR"}, status=400)

            if not re.match(password, password_reg):
                return JsonResponse({"message": "KEY_ERROR"}, status=400)
            User. objects.create(
                name=name,
                email=email,
                line=line,
                password=password
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)
            
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)      