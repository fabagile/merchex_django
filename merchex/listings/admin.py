from django.contrib import admin
from listings.models import Band, Listing

# admin.site.register(Band)


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'active')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
