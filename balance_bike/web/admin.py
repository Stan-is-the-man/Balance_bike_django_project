from django.contrib import admin
from balance_bike.web.models import BalanceBike, Customer, Address, Order, Cart


# •	The application must have a customized admin site (accessible only by admins):
#  - add at least 5 custom options (in total) to the admin interface:
#  filters, list display, ordering, search fields, list per page,  list_editable  etc.).

@admin.register(BalanceBike)
class BalanceBikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'color', 'price', 'quantity_available', 'model', 'image')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_active',
    )
    ordering = ('pk',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'street', 'first_name', 'last_name', 'phone', 'name_for_engraving')
    list_filter = ('user', 'city', 'street', 'first_name', 'last_name', 'name_for_engraving')
    list_per_page = 10
    search_fields = ('city', 'street')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'product', 'quantity','address','ordered_date', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'ordered_date')
    list_per_page = 15
    search_fields = ('user', 'product')



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated_at', 'product', 'quantity', 'created_at',)
    ordering = ('created_at',)
