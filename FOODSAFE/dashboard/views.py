from django.shortcuts import render, redirect
from .forms import NeuAddForm, SeedRequestForm
from .forms import *
# from .models import NeutritionProfile, SeedRequest, Product, Seller
from .models import *
# Create your views here.

def home_func(response):
    title = "FOODSAFE"
    return render(response, "dashboard/home.html",{"title":title,})


def neutritionist_func(request):
    if request.method == 'POST':
        form = NeuAddForm(request.POST)
        if form.is_valid():
            neu_id = form.cleaned_data['neu_id']
            if NeutritionProfile.objects.filter(neu_id=neu_id).exists():
                form.add_error('neu_id', 'This ID already exists. Please use a unique ID.')
            else:
                nutrition_data = NeutritionProfile(
                    neu_f_name=form.cleaned_data['neu_f_name'],
                    neu_l_name=form.cleaned_data['neu_l_name'],
                    neu_id=neu_id,
                    location=form.cleaned_data['location'],
                    produce=form.cleaned_data['produce'],
                    applicable_temperature=form.cleaned_data['applicable_temperature'],
                    applicable_humidity=form.cleaned_data['applicable_humidity']
                )
                nutrition_data.save()

    nutrition_records = NeutritionProfile.objects.all()

    form = NeuAddForm() 
    return render(request, 'dashboard/neutritionist.html', {'NeuAddForm': form, 'nutrition_records': nutrition_records})



def seed_request_func(request):
    form = SeedRequestForm()
    if request.method == 'POST':
        form = SeedRequestForm(request.POST)
        if form.is_valid():
            seed_request = SeedRequest(
                        farmer_full_name=form.cleaned_data['farmer_full_name'],
                        farmer_id=form.cleaned_data['farmer_id'],
                        seed_variety=form.cleaned_data['seed_variety'],
                        other_seed_name=form.cleaned_data['other_seed_name']
                )
            seed_request.save()

    
    previous_requests = SeedRequest.objects.all()

    return render(request, 'dashboard/ao.html', {
        'form': form,
        'previous_requests': previous_requests  
    })
    
    



def seller_func(request):
    seller = Seller.objects.first()  
    products = Product.objects.filter(seller=seller)  
    
    form = ProductAddForm()
    
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                seller=seller,
                product_name=form.cleaned_data['product_name'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                description=form.cleaned_data['description'],
                required_temperature=form.cleaned_data['required_temperature'],
                required_humidity=form.cleaned_data['required_humidity'],
                warehouse_location=form.cleaned_data['warehouse_location'],
                available_quantity=form.cleaned_data['available_quantity'],
            )
    return render(request, 'dashboard/seller_page.html', {
        'seller': seller,
        'products': products,
        'form': form,
    })

# def seller_func(request):
#     seller = Seller.objects.first()
#     products = Product.objects.filter(seller=seller)
#     form = ProductAddForm()

#     if request.method == "POST":
#         form = ProductAddForm(request.POST)
#         if form.is_valid():
#             product = Product(
#                 seller=seller,
#                 product_name=form.cleaned_data["product_name"],
#                 price=form.cleaned_data["price"],
#                 quantity=form.cleaned_data["quantity"],
#                 description=form.cleaned_data["description"],
#                 required_temperature=form.cleaned_data["required_temperature"],
#                 required_humidity=form.cleaned_data["required_humidity"],
#                 warehouse_location=form.cleaned_data["warehouse_location"],
#                 available_quantity=form.cleaned_data["available_quantity"],
#             )
#             product.save()
#             return redirect("seller_page")  # Redirect after adding product

#     return render(request, "dashboard/seller_page.html", {
#         "seller": seller,
#         "products": products,
#         "form": form,
#     })
