from django.contrib import admin
from k2k.models import r_lookupdata, r_k2support, r_district_data, r_farmingassets, d_user_data, r_state_district

# Register your models here.
admin.site.register(r_lookupdata)
admin.site.register(r_k2support)
admin.site.register(r_district_data)
admin.site.register(r_farmingassets)
admin.site.register(d_user_data)
admin.site.register(r_state_district)