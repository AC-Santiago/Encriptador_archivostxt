from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html", {"User": request.user})


def about(request):
    return render(request, "about.html")


def dec_cif(request):
    if request.method == "GET":
        return render(request, "dec_cif.html")
    elif request.method == "POST":
        print("hola")
        return render(request, "dec_cif.html")
