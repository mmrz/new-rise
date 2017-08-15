from django.contrib import admin
from users.models import User, Artist, ArtistImage, BillingAddress, Subscriptions
from django.contrib.admin.options import StackedInline


class BillAddInline(StackedInline):
    model = BillingAddress
    extra = 1
    max_num = 35


class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'id')
    inlines = [BillAddInline]


class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'users')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('sub_email', )

admin.site.register(User, UsersAdmin)
admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(Artist)
admin.site.register(ArtistImage)
admin.site.register(Subscriptions, SubscriptionAdmin)
# Register your models here.
