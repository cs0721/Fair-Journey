from django.db import models
from django.utils import timezone
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'rwe_type'),
    ('2', 'rwe_closure_type'),
    ('3', 'rwe_status'),
    ('4', 'rwe_start_dt'),
    ('5', 'rwe_end_dt'),
    ('6', 'rwe_publish_text'),
    ('7', 'subject_pref_rdname'),
    ('8', 'traffic_delay'),
    ('9', 'speed_limit'),
    ('10', 'lanes_affected')
)


# create data table for road construction information
class road_construction(models.Model):
    rwe_type = models.TextField(max_length=50, null=True)
    rwe_closure_type = models.TextField(max_length=50, null=True)
    rwe_status = models.TextField(max_length=50, null=True)
    rwe_start_dt = models.TextField(max_length=50, null=True)
    rwe_end_dt = models.TextField(max_length=50, null=True)
    rwe_publish_text = models.TextField(max_length=500, null=True)
    subject_pref_rdname = models.TextField(max_length=50, null=True)
    traffic_delay = models.TextField(max_length=200, null=True)
    speed_limit = models.TextField(max_length=50, null=True)
    lanes_affected = models.TextField(max_length=50, null=True)

    class Meta:
        db_table = "road"

# search and query function to process the kwargs from ajax
def query_road_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = road_construction.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id__icontains=search_value) |
                                        Q(rwe_type__icontains=search_value) |
                                        Q(rwe_closure_type__icontains=search_value) |
                                        Q(rwe_status__icontains=search_value) |
                                        Q(rwe_start_dt__icontains=search_value) |
                                        Q(rwe_end_dt__icontains=search_value)|
                                        Q(rwe_publish_text=search_value) |
                                        Q(subject_pref_rdname__icontains=search_value)|
                                        Q(traffic_delay__icontains=search_value)|
                                        Q(speed_limit__icontains=search_value)|
                                        Q(lanes_affected__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    print(count)
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }