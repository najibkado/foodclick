from django.contrib import admin
from .models import User, Entity, Listing, Giveaway

# Register your models here.
admin.site.register(User)
admin.site.register(Entity)
admin.site.register(Listing)
admin.site.register(Giveaway)
