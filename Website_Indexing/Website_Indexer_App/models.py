from django.db import models


class ParentPage(models.Model):
    id          = models.AutoField(primary_key=True)
    search_word = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default= '')

    def __str__(self):
        return self.search_word


class ChildPage(models.Model):
    page_name   = models.ForeignKey(ParentPage, on_delete=models.CASCADE)
    url         = models.CharField(max_length=255, default='')
    title       = models.CharField(max_length=100)
    keywords    = models.CharField(max_length=255, blank = True, null = True)
    media       = models.CharField(max_length=255, blank=True, null = True)

    def __str__(self):
        return self.title


