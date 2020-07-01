from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import Resource


# Register your models here.
class ResourceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            resource = form.save()
            resource.save()
            content_type = ContentType.objects.get(id=5)
            permission = Permission.objects.create(codename=resource.codename,
                                                   name=resource.codename,
                                                   content_type=content_type)
            permission.save()
        super().save_model(request, obj, form, change)


admin.site.register(Resource, ResourceAdmin)
