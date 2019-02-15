from django.db import models


class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __unicode__(self):
        return self.name
