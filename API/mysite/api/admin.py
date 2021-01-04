from django.contrib import admin
from .models import Bird, Network, Results

# Allows admin access so that looking at databases and changing fields is more intuitive
admin.site.register(Bird)
admin.site.register(Results)
admin.site.register(Network)
