import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tech_test.settings')
django.setup()
from product.models import  ProductCustomField

prods = [
    ProductCustomField(product_id='222222', field_id_id=1, value='Vape', module_id_id=1),
    ProductCustomField(product_id='222222', field_id_id=2, value='2142421424', module_id_id=1),
    ProductCustomField(product_id='222222', field_id_id=4, value='10', module_id_id=1),
    ProductCustomField(product_id='222222', field_id_id=3, value='10000', module_id_id=1),

    ProductCustomField(product_id='333333', field_id_id=2, value='42412ss24', module_id_id=1),
    ProductCustomField(product_id='333333', field_id_id=3, value='500', module_id_id=1),
    ProductCustomField(product_id='333333', field_id_id=4, value='5', module_id_id=1),
    ProductCustomField(product_id='333333', field_id_id=1, value='Gelas', module_id_id=1),

]
ProductCustomField.objects.bulk_create(prods)
print("created product custom field")