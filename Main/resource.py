from import_export import resources
from .models import member, store, salesRecord, product, ingredient, supplier, salesDetail, recipe, stockRecord

class memberResource(resources.ModelResource):
    class Meta:
        model = member

class storeResource(resources.ModelResource):
    class Meta:
        model = store

class salesRecordResource(resources.ModelResource):
    class Meta:
        model = salesRecord
		
class productResource(resources.ModelResource):
    class Meta:
        model = product
		
class ingredientResource(resources.ModelResource):
    class Meta:
        model = ingredient
		
class supplierResource(resources.ModelResource):
    class Meta:
        model = supplier
		
class salesDetailResource(resources.ModelResource):
    class Meta:
        model = salesDetail

class recipeResource(resources.ModelResource):
    class Meta:
        model = recipe

class stockRecordResource(resources.ModelResource):
    class Meta:
        model = stockRecord