from django.shortcuts import HttpResponse

# Create your views here.


def test_view(request):
    return HttpResponse("Well Well")
