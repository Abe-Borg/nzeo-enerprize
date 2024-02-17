import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from school_management.models import School, ServiceAgreement, Meter
from django.db.models import Max

# Function to generate unique meter IDs
def generate_unique_meter_id():
    base_id = 1009487683
    last_meter = Meter.objects.all().order_by('-meter_id').first()
    if last_meter:
        # Extract the numeric part if the meter_id has a specific format and increment
        last_id = int(last_meter.meter_id)
        return last_id + 1
    else:
        # Start from the base_id if no meters exist yet
        return base_id

# Function to create meters for a school
def create_meters_for_school(school):
    utility_types = ['Natural Gas', 'Electric']
    meter_types = utility_types + ['Solar'] * 2  # 5 each for Gas and Electric, 2 for Solar

    for utility_type in utility_types:
        # Retrieve the service agreement for the utility type
        service_agreement = ServiceAgreement.objects.filter(school=school, utility_type=utility_type).first()

        # Generate 5 meters for Gas and Electric
        for _ in range(5):
            Meter.objects.create(
                meter_id=generate_unique_meter_id(),
                meter_type=utility_type,
                meter_school=school,
                meter_service_agreement_id=service_agreement
            )

    # Generate 2 Solar meters (not linked to a service agreement)
    for _ in range(2):
        Meter.objects.create(
            meter_id=generate_unique_meter_id(),
            meter_type='Solar',
            meter_school=school
        )

# Main function to generate meters for all schools
def generate_meters_for_all_schools():
    for school in School.objects.all():
        create_meters_for_school(school)

# Run the main function
if __name__ == '__main__':
    generate_meters_for_all_schools()
