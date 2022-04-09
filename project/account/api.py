from pickle import GET
from .models import profile ,sep_choice,Country,City
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
import django_filters

@api_view(['GET'])
def sep(request):
    all_spe=sep_choice.objects.all().order_by('x')
    data=sep_choiceSerializer(all_spe,many=True).data
    return Response({'data':data})
@api_view(['GET'])
def countrylist(request):
    all_cont=Country.objects.all().order_by('name')
    data=CountrySerializer(all_cont,many=True).data
    return Response({'data':data})
@api_view(['GET'])
def Citylist(request):
    all_cities=City.objects.select_related('country').all().order_by('name')
    data=CitySerializer(all_cities,many=True).data
    return Response({'data':data})


@api_view(['GET'])
def doctordetails(request,id):
    details=profile.objects.get(id=id)
    data=ProfileSerializer(details).data
    return Response({'data':data})


@api_view(['GET'])
def doctorlist(request):
    all_doctor=profile.objects.all().order_by('name')
    data=listSerializer(all_doctor,many=True).data
    return Response({'data':data})


class SearchListView(generics.ListAPIView):
    queryset=profile.objects.all().order_by('name')
    serializer_class = listSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class GameListFilter(django_filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
class Meta:
    model = profile
    fields = ['price']

'''class FilterListView(generics.ListAPIView):
    queryset=profile.objects.all()
    serializer_class = listSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['gender','daywork','features']'''
    
    

class PriceListView(generics.ListAPIView):
    queryset=profile.objects.all()
    serializer_class = listSerializer
    filter_class = GameListFilter
'''class CityListView(generics.ListAPIView):
    queryset=City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['country']'''
class DoctorsListView(generics.ListAPIView):
    queryset=profile.objects.all().order_by("name")
    serializer_class = listSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields=['specialty','country']