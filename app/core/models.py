from django.db import models


class MessageModel(models.Model):
    """Model for Virgin Mary message"""
    year = models.IntegerField(blank=False, default=0)
    month = models.IntegerField(blank=False, default=0)
    day = models.IntegerField(blank=False, default=0)
    author = models.CharField(max_length=254, blank=False)
    text = models.TextField(default="")
    text_en = models.TextField(default="")
    text_pl = models.TextField(default="")
    text_es = models.TextField(default="")
    text_fr = models.TextField(default="")
    month_string = models.CharField(max_length=254, blank=False)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return str(self.year) + "-" + str(self.month) + "-" + str(self.day) + "-" + str(self.author)