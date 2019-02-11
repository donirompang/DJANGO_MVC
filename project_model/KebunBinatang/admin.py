from django.contrib import admin
from .models import Hewan, Kandang, Penjaga, Pengunjung

myModels = [Hewan, Kandang, Penjaga, Pengunjung]
admin.site.register(myModels)

