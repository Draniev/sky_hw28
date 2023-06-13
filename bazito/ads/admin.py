from django.contrib import admin

from ads.models import SelModel, AdsModel, CatModel


admin.site.register(AdsModel)
admin.site.register(CatModel)
admin.site.register(SelModel)
