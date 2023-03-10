from django.db import models

# Create your models here.


class Setting(models.Model):
    title = models.CharField(max_length=255)
    discriptions = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    tel = models.CharField(max_length=255)
    emal = models.EmailField()
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"