from django.contrib import admin
from indicators.models import indicator
from django.conf.urls import patterns
from indicators.admin_tools import IndicatorAdminTools
from django.http import HttpResponse
from indicators.wbi_parser import WBI_Parser


class IndicatorAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super(IndicatorAdmin, self).get_urls()

        my_urls = patterns('',
            (r'^update-indicators/$', self.admin_site.admin_view(self.update_indicators)),
            (r'^update-indicator-data/$', self.admin_site.admin_view(self.update_indicator_data)),
            (r'^update-indicator-city-data/$', self.admin_site.admin_view(self.update_indicator_city_data)),
            (r'^update-wbi-indicators/$', self.admin_site.admin_view(self.update_WBI_indicators))
        )
        return my_urls + urls

    def update_indicator_data(self, request):
        admTools = IndicatorAdminTools()
        admTools.update_indicator_data()
        return HttpResponse('Success')

    def update_indicator_city_data(self, request):
        admTools = IndicatorAdminTools()
        admTools.update_indicator_city_data()
        return HttpResponse('Success')

    def update_indicators(self, request):
        admTools = IndicatorAdminTools()
        admTools.update_indicators()
        return HttpResponse('Success')

    def update_WBI_indicators(self, request):
        wbi_parser = WBI_Parser()
        wbi_parser.import_wbi_indicators()
        return HttpResponse('Success')


admin.site.register(indicator, IndicatorAdmin)