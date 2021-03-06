from tastypie.serializers import Serializer
from indicator.models import *
from api.v3.resources.helper_resources import *

class CityResource(ModelResource):

    class Meta:
        queryset = City.objects.all()
        resource_name = 'cities'
        include_resource_uri = False
        serializer = Serializer(formats=['xml', 'json'])

class CountryResource(ModelResource):
    capital_city = fields.OneToOneField(CityResource, 'capital_city', full=True, null=True)
    activities = fields.ToManyField(RecipientCountryResource, attribute=lambda bundle: ActivityRecipientCountry.objects.filter(country=bundle.obj), null=True)

    class Meta:
        queryset = Country.objects.all()
        resource_name = 'countries'
        excludes = ['polygon']
        include_resource_uri = False
        serializer = Serializer(formats=['xml', 'json'])

    def dehydrate(self, bundle):
        bundle.data['activities'] = bundle.obj.activity_recipient_country_set.count()
        bundle.data['region_id'] = bundle.obj.region_id
        return bundle


class RegionResource(ModelResource):

    class Meta:
        queryset = Region.objects.all()
        resource_name = 'regions'
        include_resource_uri = False
        serializer = Serializer(formats=['xml', 'json'])


class SectorResource(ModelResource):

    class Meta:
        queryset = Sector.objects.all()
        resource_name = 'sectors'
        include_resource_uri = False
        serializer = Serializer(formats=['xml', 'json'])


class OrganisationResource(ModelResource):
    type = fields.OneToOneField(OrganisationTypeResource, 'type', full=True, null=True)

    class Meta:
        queryset = Organisation.objects.all()
        resource_name = 'organisations'
        serializer = Serializer(formats=['xml', 'json'])
        filtering = {
            # example to allow field specific filtering.
            'name': ALL,
            'abbreviation': ALL
        }
