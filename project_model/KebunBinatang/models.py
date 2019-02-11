from django.db import models
import datetime

class Hewan(models.Model):
    nama = models.CharField(max_length = 255)
    spesies = models.CharField(max_length = 255)
    berat = models.CharField(max_length = 255)
    umur = models.CharField(max_length = 255)

    def __str__ (self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length = 255)
    isi_kandang = models.CharField(max_length = 255)
    luas_kandang = models.CharField(max_length = 255)

    def __str__ (self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.CharField(max_length = 255)
    jadwal_jaga = models.TextField(max_length = 255)

    def __str__ (self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length = 255)
    nomor_telepon = models.TextField(max_length = 255)
    hari_berkunjung = models.DateField(default=datetime.date.today)

    def __str__ (self):
        return self.nama
