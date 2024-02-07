from django import forms

def Upload_XML_Form(request):
    # form function to let user upload an XML file
    # handle file upload
    if request.method == 'POST':
        form = Upload_XML_Form(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = Upload_XML_Form()