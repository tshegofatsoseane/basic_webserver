from django.http import JsonResponse

def greet_visitor(request):
    client_ip = request.META.get('REMOTE_ADDR')
    name = request.GET.get('visitorname', 'Guest')

    data = {
        'clientip': client_ip,
        'greeting': f'Hello, {name}!'
    }

    return JsonResponse(data)
