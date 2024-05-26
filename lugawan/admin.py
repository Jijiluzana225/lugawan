from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(branch)
admin.site.register(Product)
admin.site.register(transaction)
admin.site.register(halin)
admin.site.register(expense)

