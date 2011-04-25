from django.db import models

class Sobre(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    link = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='about',null=True, blank=True)

    def __unicode__(self):
        return self.title
        return self.text
        return self.link

