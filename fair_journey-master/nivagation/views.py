from django.shortcuts import render
from nivagation.models import road_construction
from nivagation.serializers import RoadSerializer
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.template.response import TemplateResponse
from django.http.response import HttpResponse
from nivagation.models import query_road_by_args

from django.contrib.auth.decorators import login_required


# Create your views here.
# return page

def index(request):
    html = TemplateResponse(request, 'new_index.html')
    return HttpResponse(html.render())

# return map page
def map(request):
    html = TemplateResponse(request, 'new_map.html')
    return HttpResponse(html.render())

# return service page
def service(request):
    html = TemplateResponse(request, 'map.html')
    return HttpResponse(html.render())

# return surface page
def surface(request):
    html = TemplateResponse(request, 'nearby_toilets.html')
    return HttpResponse(html.render())

# return contact page
def contact(request):
    html = TemplateResponse(request, 'contact.html')
    return HttpResponse(html.render())

# return about page
def about(request):
    html = TemplateResponse(request, 'about.html')
    return HttpResponse(html.render())

# return project page
def project(request):
    html = TemplateResponse(request, 'project.html')
    return HttpResponse(html.render())

# return about page
def new_index(request):
    html = TemplateResponse(request, 'new_index.html')
    return HttpResponse(html.render())

# return about page
def small_map(request):
    html = TemplateResponse(request, 'small_map.html')
    return HttpResponse(html.render())

# return about page
def surface(request):
    html = TemplateResponse(request, 'surface.html')
    return HttpResponse(html.render())

def d3_map(request):
    html = TemplateResponse(request, '3d_map.html')
    return HttpResponse(html.render())


#create a roadviewset class to process serializer road constuction information and pass it through ajax
class RoadViewSet(viewsets.ModelViewSet):
    queryset = road_construction.objects.all()
    serializer_class = RoadSerializer

    #override list function
    def list(self, request, **kwargs):
        try:
            road = query_road_by_args(**request.query_params)
            print(road)
            serializer = RoadSerializer(road['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = road['draw']
            result['recordsTotal'] = road['total']
            result['recordsFiltered'] = road['count']
            print(result)
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)