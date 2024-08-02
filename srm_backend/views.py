from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the SRM API</h1><p>Use /api/srm for API requests.</p>")


def srm_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            data_list = data.get('data', [])
            
            # Process the data
            numbers = [x for x in data_list if x.isdigit()]
            alphabets = [x for x in data_list if x.isalpha()]
            highest_alphabet = [max(alphabets, default='')] if alphabets else []

            response = {
                "is_success": True,
                "user_id": "your_name_ddmmyyyy",
                "email": "your_email@example.com",
                "roll_number": "your_roll_number",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
        except json.JSONDecodeError:
            response = {"is_success": False, "error": "Invalid JSON input"}
        return JsonResponse(response)

    elif request.method == 'GET':
        response = {"operation_code": 1}
        return JsonResponse(response)