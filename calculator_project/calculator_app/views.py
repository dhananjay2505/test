from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import re
import json

history = []

def calculate(expression):
    try:
        cleaned_expression = re.sub(r'[^0-9+\-*/^().]', '', expression)
        result = eval(cleaned_expression)
        return result
    except Exception as e:
        return f"Error: {e}"

@csrf_exempt
def calculate_api(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        expression = data.get('expression', '')
        result = calculate(expression)
        history.append({'expression': expression, 'result': result})
        return JsonResponse({'result': result})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def history_api(request):
    return JsonResponse({'history': history})

def index(request):
    return render(request, '../templates/index.html')
