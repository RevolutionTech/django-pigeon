from django.http import HttpResponse, JsonResponse


def foo(request):
    return HttpResponse('Hello World!')


def foo_api(request):
    return JsonResponse({'foo': 'bar'})
