import traceback
from django.shortcuts import render
from django.shortcuts import redirect
from authentication.models import CustomAuth, Role
from .models import CustomField, Module, ProductCustomField
from django.contrib.auth.decorators import login_required
from tech_test.helper import random_digit_string
from tech_test.decorator import role_required
# Create your views here.


@login_required()
@role_required('manajer')
def create_module(request):
    if request.method == 'POST':
        ##todo check module if exist return fail
        get_user = CustomAuth.objects.get(username=request.user)
        if get_user.module_id != 0:
            return redirect('product')

        module = Module.objects.create(is_installed=True)
        get_user.module_id = module.id
        get_user.save()
        return redirect('product')


@login_required()
@role_required('manajer')
def remove_module(request):
    if request.method == 'POST':
        module_id = request.user.module_id
        try:
            Module.objects.get(id=module_id).delete()
            ProductCustomField.objects.filter(module_id=module_id).delete()
            get_role = Role.objects.filter(name__in=['public', 'user'])
            for role in get_role:
                CustomAuth.objects.filter(module_id=module_id, role_id=role.id).delete()
            CustomAuth.objects.filter(module_id=module_id).update(module_id=0)
        except:
           print(traceback.format_exc())
    return redirect('module')

@login_required()
def list_module(request):
    module_id = request.user.module_id
    try:
        modules = Module.objects.get(id=module_id)
    except Module.DoesNotExist:
        return render(request, "product/list_module.html", {'modules': None})

    data = {'modules': modules}
    return render(request, "product/list_module.html", data)


@login_required()
@role_required('manajer')
def upgrade(request):

    if request.method == 'GET':
        custom_fields = CustomField.objects.all()
        data = {'custom_fields': custom_fields}
        return render(request, "product/custom_field.html", data)


    return render(request, "product/list_product.html")

@login_required()
@role_required('manajer')
def create_field(request):
    if request.method == 'POST':
        ##todo add custom field
        name = request.POST.get('name')
        code = request.POST.get('code')
        type = request.POST.get('type')
        CustomField.objects.create(name=name, code=code, type=type)
        return redirect('module')


    return render(request, "product/create_custom_field.html")

@login_required()
@role_required('manajer')
def remove_field(request, id):
    if request.method == 'POST':
        CustomField.objects.get(id=id).delete()
        ProductCustomField.objects.filter(field_id=id).delete()
        return redirect('upgrade')

@login_required()
def product(request):
    if request.user.module_id == 0:
        ##Todo setup new project
        return redirect('create_module')

    custom_fields = CustomField.objects.all()
    product_values = ProductCustomField.objects.filter(module_id=request.user.module_id)

    table_data = {}
    for product in product_values:
        if product.product_id not in table_data:
            table_data[product.product_id] = {}
        table_data[product.product_id][product.field_id.code] = product.value
        table_data[product.product_id][product.field_id.code] = product.value

    data = {
        'fields': custom_fields,
        'datas': table_data,
    }

    return render(request, "product/list_product.html", data)

@login_required()
@role_required('manajer')
def remove_product(request, id):
    if request.method == 'POST':
        print(id)
        ProductCustomField.objects.filter(product_id=id).delete()
        return redirect('product')

@login_required()
@role_required('manajer', 'user')
def create_product(request):
    if request.method == 'POST':
        req = request.POST.dict()
        del req['csrfmiddlewaretoken']
        product_id = random_digit_string()
        for key, val in req.items():
            id_key = key.split('-')

            module = Module.objects.get(id=request.user.module_id)
            custom_field = CustomField.objects.get(id=id_key[1])
            ProductCustomField.objects.create(
                value=val,
                product_id=product_id,
                module_id=module,
                field_id=custom_field
            )
        return redirect('product')


    custom_field = CustomField.objects.all()
    return render(request, "product/create_product.html",{'custom_fields':custom_field})


@login_required()
@role_required('manajer', 'user')
def update_product(request, id):
    custom_fields = CustomField.objects.all()

    if request.method == 'POST':
        for field in custom_fields:
            field_key = f"{field.code}-{field.id}"
            value = request.POST.get(field_key)

            ProductCustomField.objects.update_or_create(
                product_id=id,
                field_id=field,
                defaults={'value': value, 'module_id_id': request.user.module_id},
            )
        return redirect('product')  # or wherever you want

    existing_values = {
        pc.field_id.id: pc.value
        for pc in ProductCustomField.objects.filter(product_id=id)
    }

    data = {
        'custom_fields': custom_fields,
        'existing_values': existing_values,
    }

    return render(request,"product/edit_product.html", data)
