from django.http import HttpResponse, JsonResponse


def foo(request):
    return HttpResponse('Hello World!')


def foo_api(request):
    if request.method == 'GET':
        return JsonResponse({'foo': 'bar'})
    elif request.method == 'POST':
        return HttpResponse(status=204)
