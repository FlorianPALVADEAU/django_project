from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import Image
from .form import createForm

 
# create
def create_view(request):

    context ={}
    form = createForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

         
    context['form']= form
    return render(request, "CRUD/createImage.html", context)


# update
def update_view(request, id):

    context ={}
    obj = get_object_or_404(Image, id = id)
    form = createForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
 
    context["form"] = form
 
    return render(request, "CRUD/updateImage.html", context)


# get all images
def all_images(request):

    context ={}
    context["dataset"] = Image.objects.all()
         
    return render(request, "CRUD/images.html", context)


# single
def show_single(request, id):

    context ={}
    context["data"] = Image.objects.get(id = id)
         
    return render(request, "CRUD/show_single.html", context)


# delete
def delete(request, id):
    obj = get_object_or_404(Image, id = id)
    obj.delete()
    
    return HttpResponseRedirect("/")