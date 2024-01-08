from django.shortcuts import render

# Create your views here. Views manages the presentation of DATA to the user. 
# Views are responsible for presenting data, how data is selected, processed
# and passed to the templates

# these can be:
# 1. Function-Based Views (FBVs): These are simple Python functions that take a web 
# request and return a web response. For example, a view function can query a database for 
# data, process it, and pass it to a template for rendering an HTML page.
#
# 2. Class-Based Views (CBVs): Django also supports views defined as Python classes. 
# They are particularly useful for creating reusable views and for handling more complex view 
# logic. CBVs provide built-in generic views for common tasks like displaying a list of objects 
# or handling a form submission.
#
# 3. Request Handling: Views receive HttpRequest objects and must return HttpResponse objects. 
# They handle the request data and decide what to do with it.
# 
# 4. Querying the model: Views often interact with the database through Django's ORM (Object-Relational Mapping). 
# This involves querying models to retrieve, create, update, or delete data.
#
# 5. Business Logic: Any necessary business logic is implemented within views. 
# This could be calculations, data processing, or any other form of decision-making 
# logic relevant to the application's functionality
#
# 6. Context Data for Templates: Views often prepare the data that needs to be displayed on a webpage. 
# This data is then passed to templates in the form of a context dictionary.
# 
# 7. Redirects and Error Handling: Views can redirect the user to different pages or handle 
# different types of exceptions and errors that might occur during the request/response cycle.
# 
# 8. API responses: Veiws can serve as an endpoint for an API. 
#
# 9. Redirects and Error Handling: Views can redirect the user to different pages or handle
#
# 10. Serving static files: Views can serve static files like images, CSS, and JavaScript.
# 
# 11. Streaming or Real-time data: views can stream data or handle real-time updates. 

def index(request, *args, **kwargs):
    return render(request, 'maps/index.html')