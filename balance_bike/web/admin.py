from django.contrib import admin

from balance_bike.web.models import BalanceBike


@admin.register(BalanceBike)
class BalanceBikeAdmin(admin.ModelAdmin):
    list_display = ('pk','color', 'model', 'image', 'price', 'custom_tag')
