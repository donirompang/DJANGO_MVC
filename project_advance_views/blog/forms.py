from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('judul','jumlah_komen','created_date','gambar','isi_kontent',)