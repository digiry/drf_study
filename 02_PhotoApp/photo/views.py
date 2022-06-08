from django.shortcuts import render


def photo_list(request):
    return render(request, "photo/photo_list.html", {})
