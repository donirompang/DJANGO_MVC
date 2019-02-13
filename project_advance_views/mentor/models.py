from django.db import models

class Mentor (models.Model):
    nama = models.CharField(max_length = 255)
    profesi = models.CharField(max_length = 255)
    pesan = models.CharField(max_length = 255)
    gambar = models.CharField(max_length = 255)
