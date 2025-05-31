import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_test.settings')
django.setup()
from authentication.models import CustomAuth, Role
from product.models import CustomField, ProductCustomField

role_usr = Role.objects.create(name='user')
role_public = Role.objects.create(name='public')
role_mnjr = Role.objects.create(name='manajer')
print("CREATED Role")


# Create an admin user
CustomAuth.objects.create_user( username='manajer',password='hm2025',role_id=role_mnjr)

print("CREATED USER")


custom_fields = [
    CustomField(name='name',code='name',type='char'),
    CustomField(name='barcode', code='barcode', type='char'),
    CustomField(name='price', code='price', type='int'),
    CustomField(name='stock', code='stock', type='int'),
]

CustomField.objects.bulk_create(custom_fields)
print("CREATED CUSTOM FIELDS")

