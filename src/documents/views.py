import os
from django.http import FileResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required
def download_file(request):
    # get the file path from the request
    # file_path = request.GET.get('file_path')
    # open the file
    # file = open(file_path, 'rb')
    # return the file
    # return FileResponse(file)
    context = {}
    return render(request, 'documents/download_file.html', context)

# @login_required
def upload_file(request):
    # # get the file from the request
    # file = request.FILES['file']
    # # get the file path from the request
    # file_path = request.POST.get('file_path')
    # # open the file
    # with open(file_path, 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)
    # return the file
    context = {}
    return render(request, 'documents/upload_file.html', context)

# @login_required
def delete_file(request):
    # # get the file path from the request
    # file_path = request.GET.get('file_path')
    # # delete the file
    # os.remove(file_path)
    # # return the file
    # return render(request, 'documents/delete.html')
    context = {}
    return render(request, 'documents/delete_file.html', context)

