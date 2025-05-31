from django.db import models

# Create your models here.


class Module(models.Model):
    id = models.AutoField(primary_key=True)
    is_installed = models.BooleanField(default=False)


class CustomField(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class ProductCustomField(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=20, db_index=True)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE, default=0)
    field_id = models.ForeignKey(CustomField, on_delete=models.CASCADE, default=0)
    value = models.TextField()
