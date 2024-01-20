from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

# Initialize statistics globally
statistics = {
    'most_used_request': None,
    'hits': 0
}

@csrf_exempt
@require_GET
def fizz_buzz(request):
    int1 = int(request.GET.get('int1', 3))
    int2 = int(request.GET.get('int2', 5))
    limit = int(request.GET.get('limit', 100))
    str1 = request.GET.get('str1', 'fizz')
    str2 = request.GET.get('str2', 'buzz')

    result = []
    for i in range(1, limit + 1):
        fizz_buzz_str = ''
        if i % int1 == 0:
            fizz_buzz_str += str1
        if i % int2 == 0:
            fizz_buzz_str += str2
        result.append(fizz_buzz_str or str(i))

    # Update statistics
    update_statistics(request.path)

    return JsonResponse(result, safe=False)

@require_GET
def get_statistics(request):
    global statistics  # statistics declared globally
    return JsonResponse(statistics)

# Update statistics function as before
def update_statistics(request_url):
    global statistics
    if statistics['most_used_request'] == request_url:
        statistics['hits'] += 1
    else:
        statistics = {
            'most_used_request': request_url,
            'hits': 1
        }

def index(request):
    return render(request, 'index.html')
