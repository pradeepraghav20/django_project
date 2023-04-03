from django.http import HttpResponse


def index_test(request):

    print("this is indexpage")
    return HttpResponse ("this is index page")
