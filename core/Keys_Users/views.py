from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def keys_page(request):
    return render(request, "Keys_page.html")
