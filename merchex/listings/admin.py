from django.contrib import admin
from listings.models import Band, Listing

# admin.site.register(Band)


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'active', 'id')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'type', 'year', 'id')


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
