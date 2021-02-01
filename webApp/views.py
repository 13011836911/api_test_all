from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import render
import json

# Create your views here.

def Login(request):
    # "code": 200,
    # "data": {
    #     "age": 18,
    #     "work": "QA",
    #     "dataList": [
    #     ]
    # }
    result = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['user'] = username
        result['password'] = password
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json', charset='utf8')
    else:
        return render(request, 'login.html')