from django.conf import settings
from rest_framework import serializers

from nivagation.models import road_construction


# serailizer file
class RoadSerializer(serializers.ModelSerializer):
    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    class Meta:
        model = road_construction
        fields = '__all__'
        #fields = ('id', 'rwe_type', 'rwe_closure_type', 'rwe_status', 'rwe_start_dt', 'rwe_end_dt', 'rwe_publish_text', 'subject_pref_rdname', 'traffic_delay', 'speed_limit', 'lanes_affected')
