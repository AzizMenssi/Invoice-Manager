from django.contrib import admin
from main.models import UserProfile,CompteBancaires,Produits,Clients,FacturesProforma,FacturesEdex,FacturesUnpa,List_ProduitsProforma,List_ProduitsEdex,List_ProduitsUnpa

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Clients)
admin.site.register(CompteBancaires)
admin.site.register(FacturesProforma)
admin.site.register(FacturesEdex)
admin.site.register(FacturesUnpa)
admin.site.register(Produits)
admin.site.register(List_ProduitsProforma)
admin.site.register(List_ProduitsEdex)
admin.site.register(List_ProduitsUnpa)
