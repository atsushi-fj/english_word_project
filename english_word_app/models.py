from django.db import models


class EnglishWordModel(models.Model):
  english_word = models.CharField(max_length=35)
  japanese_word = models.CharField(max_length=35)
  check_count = models.IntegerField(null=True, blank=True, default=0)


