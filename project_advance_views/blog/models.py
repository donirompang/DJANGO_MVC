from django.db import models
import datetime

class Blog (models.Model):
    gambar = models.CharField(max_length = 255)
    created_date = models.DateField(default = datetime.date.today)
    jumlah_komen = models.CharField(max_length = 255)
    judul = models.CharField(max_length = 255)
    isi_kontent = models.TextField(max_length = 255)

