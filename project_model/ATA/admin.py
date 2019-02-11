from django.contrib import admin
from .models import Mentee, Mentor, MataPelajaran, Direksi, Challenge, LiveCode

myModels = [Mentee, Mentor, MataPelajaran, Direksi, Challenge, LiveCode]
admin.site.register(myModels)

