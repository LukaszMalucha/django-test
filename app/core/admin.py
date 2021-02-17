from django.contrib import admin
from core import models


class MessageModelAdmin(admin.ModelAdmin):

    ordering = ["year", "month", "author"]
    list_display = ["year", "month", "day", "author"]
    search_fields = ["year", "month", "day", "author"]
    list_filter = ("author", "year")

    class Meta:
        model = models.MessageModel


admin.site.register(models.MessageModel, MessageModelAdmin)