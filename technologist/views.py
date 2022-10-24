from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Operation
import json
@csrf_exempt
def get_operations(request: HttpRequest):
    body_text = request.body.decode('utf-8')
    body = json.loads(body_text)
    id = body.get('id')
    if id == '':
        return JsonResponse({})
    id = int(id)
    operations = Operation.objects.filter(pk=id).first()
    operations = {"id": operations.id, "name": operations.name, "time": operations.time}
    return JsonResponse(operations, safe=False)
