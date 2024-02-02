from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from school_management.models import School


@login_required
def school_home(request):
    '''This view is used to render the school home page for school staff
    '''
    school_info = School.objects.get(school_name = request.user.profile.user_school)
    context = {
        'school_name': school_info.school_name,
        'school_district': school_info.school_district,
    }

    return render(request, 'school_management/school_home.html', context)


