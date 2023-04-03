from django.http import HttpResponse


def index_test(request):

    #print("this is indexpage")
    return HttpResponse ("this is index page")

def index_2(request):
     return HttpResponse ("this is index page 2")
