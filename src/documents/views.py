import os
from django.http import FileResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url = 'login')
def download_file(request):
    # get the file path from the request
    file_path = request.GET.get('file_path')
    # open the file
    file = open(file_path, 'rb')
    # return the file
    return FileResponse(file)

@login_required(login_url = 'login')
def upload_file(request):
    # get the file from the request
    file = request.FILES['file']
    # get the file path from the request
    file_path = request.POST.get('file_path')
    # open the file
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    # return the file
    return render(request, 'documents/upload.html')

@login_required(login_url = 'login')
def delete_file(request):
    # get the file path from the request
    file_path = request.GET.get('file_path')
    # delete the file
    os.remove(file_path)
    # return the file
    return render(request, 'documents/delete.html')

