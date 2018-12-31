from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import member, store, salesRecord, product, ingredient, supplier, salesDetail, recipe, stockRecord
# Register your models here.
@admin.register(member)
class memberAdmin(ImportExportModelAdmin):
 list_display = ('id', 'name', 'gender', 'dateOfBirth', 'phone', 'address')

@admin.register(store)
class storeAdmin(ImportExportModelAdmin):
 list_display = ('id', 'name', 'phone', 'address')

@admin.register(salesRecord)
class salesRecordAdmin(ImportExportModelAdmin):
 list_display = ('id', 'totolPrice', 'paymentMethod', 'date', 'storeID', 'memberID')

@admin.register(product)
class productAdmin(ImportExportModelAdmin):
 list_display = ('id', 'name', 'price')

@admin.register(ingredient)
class ingredientAdmin(ImportExportModelAdmin):
 list_display = ('id', 'name', 'stock')

@admin.register(supplier)
class supplierAdmin(ImportExportModelAdmin):
 list_display = ('id', 'name', 'phone', 'address')

@admin.register(salesDetail)
class salesDetailAdmin(ImportExportModelAdmin):
 list_display = ('id', 'salesRecordID', 'productID', 'amount')

@admin.register(recipe)
class recipeAdmin(ImportExportModelAdmin):
 list_display = ('id', 'productID', 'ingredientID', 'amount')

@admin.register(stockRecord)
class stockRecordAdmin(ImportExportModelAdmin):
 list_display = ('id', 'ingredientID', 'amount', 'price', 'date', 'supplierID')