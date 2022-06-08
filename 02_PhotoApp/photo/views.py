from django.shortcuts import get_object_or_404, render

from photo.models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, "photo/photo_list.html", {"photos": photos})


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, "photo/photo_detail.html", {"photo": photo})
