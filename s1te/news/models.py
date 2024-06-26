from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='')
    anons = models.CharField('Anons', max_length=250, default='')
    full_text = models.TextField('Text')
    date = models.DateTimeField('Date: ')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


