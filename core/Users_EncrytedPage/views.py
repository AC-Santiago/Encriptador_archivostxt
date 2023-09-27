from django.shortcuts import render

# Create your views here.
def login(request):
    name_user = "Toby2003"
    return render(request, "Login_U.html", {"name_user": name_user})


def register(request):
    return render(request, "Register_U.html")


# def keys_page(request):
#     # SantiagoA2003
#     # Toby2003
#     user = users.objects.get(username="Toby2003")
#     keys_user = keys.objects.filter(user__pk=user.pk)
#     return render(request, "Keys_page.html", {"keys": keys_user})