import csv
from django.core.management import BaseCommand
from nivagation.models import road_construction

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                road = road_construction.objects.create(
                    rwe_type = row[0],
                    rwe_closure_type=row[1],
                    rwe_status = row[2],
                    rwe_start_dt = row[3],
                    rwe_end_dt = row[4],
                    rwe_publish_text = row[5],
                    subject_pref_rdname = row[6],
                    traffic_delay = row[7],
                    speed_limit = row[8],
                    lanes_affected = row[9])
