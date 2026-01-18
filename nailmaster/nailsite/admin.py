from django.contrib import admin
from .models import ImageWorks, Services, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('owner', 'created')
    fields = ('owner', 'body', 'created')
    readonly_fields = ('created',)


admin.site.register(ImageWorks)
admin.site.register(Services)
admin.site.register(Review, ReviewAdmin)
