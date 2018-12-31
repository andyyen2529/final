# -*- coding: utf-8 -*-

from django.db import models
#一般的實體
class member(models.Model): #會員
	#id primarykey 自已會幫你設
	name = models.CharField(max_length = 10) #名稱
	gender = models.CharField(max_length = 10) #性別 (0 = 空值；1 = 男性；2 = 女性；3 = 第三性)
	dateOfBirth = models.DateField() #生日
	phone = models.CharField(max_length = 10) #電話/手機號碼
	address = models.CharField(max_length = 100) #住址
	#score = mmodels.IntegerField() #顧客分數(越高代表顧客貢獻度越高)

class store(models.Model): #分店
	name = models.CharField(max_length = 10) #名稱
	phone = models.CharField(max_length = 10) #電話/手機號碼
	address = models.CharField(max_length = 100) #住址

class salesRecord(models.Model): #銷售紀錄
	totolPrice =  models.IntegerField() #消費總額
	paymentMethod = models.CharField(max_length = 20) #付款方式
	date = models.DateField() #消費日期  
	storeID = models.ForeignKey(store) #用餐分店
	#tableNumber = models.IntegerField() #桌號
	memberID = models.ForeignKey(member) #如果是會員就顯示該會員名稱；不是則為空值

class product(models.Model): #產品
	name = models.CharField(max_length = 20) #產品名稱
	price = models.IntegerField() #產品單價

class ingredient(models.Model): #原料
	name = models.CharField(max_length = 20) #原料名稱
	stock = models.IntegerField() #原料庫存

class supplier(models.Model):
	name = models.CharField(max_length = 20) #名稱
	phone = models.CharField(max_length = 10) #電話/手機號碼
	address = models.CharField(max_length = 100) #住址

#因實體和實體的關聯產生出來的新實體

class salesDetail(models.Model): #交易明細 (銷售紀錄 & 產品)
	salesRecordID = models.ForeignKey(salesRecord)
	productID = models.ForeignKey(product)
	amount = models.IntegerField() #數量 (例如有一桌的客人點了2份美式牛肉堡，那這裡的數字就是2)

class recipe(models.Model): #食譜 (產品 & 原料)
	productID = models.ForeignKey(product) #產品
	ingredientID = models.ForeignKey(ingredient) #原料
	amount = models.IntegerField() #所需的原料數量

class stockRecord(models.Model): #進貨紀錄 (原料 & 供應商)
	ingredientID = models.ForeignKey(ingredient) #進貨原料的名稱 
	amount = models.IntegerField() #進貨原料的數量
	#unit = models.IntegerField() #進貨原料的單位 (箱、盒)
	price = models.IntegerField() #進貨原料的單價
	date = models.DateField() #進貨日期
	supplierID = models.ForeignKey(supplier) #供應商
