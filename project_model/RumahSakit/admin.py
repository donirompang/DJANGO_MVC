from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat

myModels = [Dokter, Pasien, Resep, Obat]
admin.site.register(myModels)
