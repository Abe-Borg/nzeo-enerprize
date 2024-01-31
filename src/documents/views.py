import os
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from documents.forms import DocumentDownloadForm, DocumentUploadForm



@login_required
def download_document(request):    
    if request.method == 'POST':
        form = DocumentDownloadForm(request.POST)
        if form.is_valid():
            results = form.search()
            return render(request, 'documents/download_results.html', {'results': results})
    else:
        form = DocumentDownloadForm()
    
    return render(request, 'documents/download_document.html', {'form': form})


@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.document_owner = request.user  # Automatically set the document owner to the current user
            document.save()
            messages.success(request, 'File uploaded successfully.')
            return redirect('some_view')  # Redirect to a success page or another relevant view
        else:
            # If the form is not valid, display the form again with validation errors
            messages.error(request, 'File upload failed. Please correct the errors below.')
    else:
        form = DocumentUploadForm()
    return render(request, 'documents/upload_document.html', {'form': form})


@login_required
def upload_green_button_data(request):
    context = {}
    return render(request, 'documents/upload_green_button_data.html', context)


@login_required
def upload_utility_bill(request):
    context = {}
    return render(request, 'documents/upload_utility_bill.html', context)


