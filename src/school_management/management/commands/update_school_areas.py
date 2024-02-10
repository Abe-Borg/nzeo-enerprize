from django.core.management.base import BaseCommand
from django.db.models import Sum
from school_management.models import School, Building

class Command(BaseCommand):
    help = 'Recalculates the total area of each school'

    def handle(self, *args, **options):
        for school in School.objects.all():
            total_area = Building.objects.filter(
                building_school=school
            ).aggregate(total_area_sqft=Sum('building_area_sqft'))['total_area_sqft'] or 0

            School.objects.filter(pk=school.pk).update(school_area_sqft=total_area)

            self.stdout.write(self.style.SUCCESS(
                f'Updated school_area_sqft for {school.school_name} to {total_area}'
            ))
