from django.db import models
import uuid

class products(models.Model):
    product_name= models.CharField(max_length=200, null=True, blank=True)
    date_of_upload= models.DateField(max_length=200)
    uploader_name= models.CharField(max_length=400)

class purchase(models.Model):
    unique_id=models.UUIDField(default=uuid.uuid4, editable=False)
    prchase_quantity=models.IntegerField(max_length=20)
    product_name=models.ForeignKey(products, default=None,on_delete=models.SET_NULL, null=True)

