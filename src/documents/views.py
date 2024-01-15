import os
from django.http import FileResponse
from django.shortcuts import render

# Create view for download file request
def download_file(request):
    # get the file path from the request
    file_path = request.GET.get('file_path')
    # open the file
    file = open(file_path, 'rb')
    # return the file
    return FileResponse(file)

# Create view for upload file request
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

# Create view for delete file request
def delete_file(request):
    # get the file path from the request
    file_path = request.GET.get('file_path')
    # delete the file
    os.remove(file_path)
    # return the file
    return render(request, 'documents/delete.html')

