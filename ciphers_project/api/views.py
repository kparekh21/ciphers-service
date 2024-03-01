from django.http import JsonResponse
from .ciphers import caesar_encode

# Create your views here.
def greetings(request):
    request = {"message":"Welcome to ciphers service!"}
    return JsonResponse(request)

def encode(request, plaintext, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = caesar_encode(plaintext, shift)
    return JsonResponse({"cipher": cipher})

