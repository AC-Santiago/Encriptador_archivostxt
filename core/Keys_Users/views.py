from django.shortcuts import render

# Create your views here.
def Keys_Page(request):
    return render(request, "Keys_page.html")