from django.db import models

class Mentee (models.Model):
    nama = models.CharField(max_length = 255)
    pesan = models.CharField(max_length = 255)
    gambar = models.CharField(max_length = 255)

