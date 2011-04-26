from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=13)
    link = models.CharField(max_length=255, null=True, blank=True)
    submarino = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='books')

    def __unicode__(self):
        return self.name
        return self.author
        return self.description
        return self.isbn
        return self.link
        return self.submarino

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    synopsis = models.TextField(null=True, blank=True)
    cast = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    submarino = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=10, null=True, blank=True)
    photo = models.ImageField(upload_to='Movies')

    def __unicode__(self):
        return self.name
        return self.director
        return self.synopsis
        return self.cast
        return self.link
        return self.submarino
#        return self.year

