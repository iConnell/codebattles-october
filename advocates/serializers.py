from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Links

class LinkSerializer(ModelSerializer):
    class Meta:
        model = Links
        fields = [
            'name', 'url'
        ]

class AdvocateSerializer(ModelSerializer):
    links = SerializerMethodField('get_links')

    def get_links(self, object):
        query = object.links_set.all()
        links = LinkSerializer(query, many=True).data
        return links

    class Meta:
        model = Advocate
        fields = [
            'id',
            'name',
            'profile_pic',
            'short_bio',
            'long_bio',
            'advocate_years_exp',
            'company',
            'links',
        ]