from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def srm_post(request):
    data = request.data.get('data', [])
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_alphabet = max(alphabets, key=str.lower) if alphabets else None

    response_data = {
        "is_success": True,
        "user_id": "your_name_ddmmyyyy",
        "email": "your_email@example.com",
        "roll_number": "your_roll_number",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }

    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def srm_get(request):
    return Response({"operation_code": 1}, status=status.HTTP_200_OK)
