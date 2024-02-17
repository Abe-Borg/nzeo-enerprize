import os
import django
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from school_management.models import School, UtilityProviderAccountNumber, ServiceAgreement
from district_management.models import SchoolDistrict

def generate_service_agreement_id():
    return str(random.randint(1000000000, 9999999999))

def create_service_agreements():
    utility_types = ['Natural Gas', 'Electric']

    for school in School.objects.all():
        district = school.school_district

        for utility_type in utility_types:
            utility_account = UtilityProviderAccountNumber.objects.filter(
                account_district=district, utility_type=utility_type).first()
            
            if utility_account:
                ServiceAgreement.objects.create(
                    service_agreement_id=generate_service_agreement_id(),
                    utility_type=utility_type,
                    school=school,
                    utility_provider_account_number=utility_account
                )

if __name__ == "__main__":
    create_service_agreements()
