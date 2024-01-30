import os
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



@login_required
def download_document(request):
    # Simulating file download logic
    file_path = request.GET.get('file_path')
    
    if file_path:
        try:
            file = open(file_path, 'rb')
            messages.success(request, 'File downloaded successfully.')
            return FileResponse(file)
        except IOError:
            messages.error(request, 'File not found.')
            return render(request, 'documents/download_file.html')
    else:
        messages.error(request, 'No file specified.')
        return render(request, 'documents/download_file.html')


@login_required
def upload_document(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        file_path = 'path/to/save/file'  # Define where you want to save the file

        try:
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            messages.success(request, 'File uploaded successfully.')
            return redirect('some_view')  # Redirect to a relevant view after upload
        except Exception as e:
            messages.error(request, f'File upload failed: {str(e)}')
    
    return render(request, 'documents/upload_file.html')


@login_required
def upload_green_button_data(request):
    context = {}
    return render(request, 'documents/upload_green_button_data.html', context)


@login_required
def upload_utility_bill(request):
    context = {}
    return render(request, 'documents/upload_utility_bill.html', context)


