from .models import (HomeCarusel, HomeCaruselActive, 
                    Category, Sub_Category, Product, Panel,
                    HomeLogo, Contact, Cart)
from django.shortcuts import render, redirect
from .forms import NewUserForm, ContactForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    home_carusel_active = HomeCaruselActive.objects.all().first()
    home_carusel = HomeCarusel.objects.all()
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    brands = Sub_Category.objects.all()
    panel_list = Panel.objects.all()
    panel_list_active = Panel.objects.all().first()
    home_logo = HomeLogo.objects.all().first()
    return render(request, 'main/index.html', context={
        'home_carusel_active':home_carusel_active,
        'home_carusel':home_carusel,
        'category_list':category_list,
        'product_list':product_list,
        'brands':brands,
        'panel_list':panel_list,
        'panel_list_active':panel_list_active,
        'home_logo':home_logo,
        'link':'index'

    })


def index_detail(request, id):
    home_carusel_active = HomeCaruselActive.objects.all().first()
    home_carusel = HomeCarusel.objects.all()
    category_list = Category.objects.all()
    products = Sub_Category.objects.filter(pk=id)
    brands = Sub_Category.objects.all()
    product_list = Product.objects.all()
    panel_list = Panel.objects.all()
    panel_list_active = Panel.objects.all().first()
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/index_detail.html', context={
        'home_carusel_active':home_carusel_active,
        'home_carusel':home_carusel,
        'category_list':category_list,
        'products':products,
        'brands':brands,
        'product_list':product_list,
        'panel_list':panel_list,
        'panel_list_active':panel_list_active,
        'home_logo':home_logo,
        'link':'index_detail'




    })


def error_404(request):
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/404.html', context={
        'home_logo':home_logo,
        'link':'error_404'

        
    })

def blog(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    brands = Sub_Category.objects.all()
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/blog.html', context={
        'category_list':category_list,
        'product_list':product_list,
        'brands':brands,
        'home_logo':home_logo,
        'link':'blog'


    })

def blog_single(request):
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/blog-single.html', context={
        'home_logo':home_logo,
        'link':'blog_single'

        
    })


quantity_list = {i.id:1 for i in Cart.objects.all()}


def cart(request):
    global quantity_list
    summ = 0
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        mymodel = Product.objects.get(id=prod_id)
        Cart.objects.create(prod=mymodel)
        quantity_list[int(prod_id)] = 1 
        return redirect('index')
    cart_list = Cart.objects.all()
    for i in cart_list:
        cart_list.single_price = i.prod.price * quantity_list[i.id]
        summ += i.prod.price
        # summ *= quantity_list[i.id]
        print(summ)
    return render(request, 'main/cart.html', context={
        'cart_list':cart_list,
        'summ':summ,
        'rast':int(summ * 15 / 100),
        'total':summ - int(summ * 15 / 100),
        'mydict':quantity_list
    })


def delete_prod(request):
    global quantity_list
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        Cart.objects.filter(id=prod_id).delete()
        quantity_list.pop(int(prod_id))
        return redirect('cart')



def update_cart(request):
    global quantity_list
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        quantity_list[int(prod_id)] += 1
        print(quantity_list)
        return redirect('cart')



def checkout(request):
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/checkout.html', context={
        'home_logo':home_logo
        
    })

def product_details(request):

    category_list = Category.objects.all()
    product_list = Product.objects.all()
    brands = Sub_Category.objects.all()
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/product-details.html', context={
        'category_list':category_list,
        'product_list':product_list,
        'brands':brands,
        'home_logo':home_logo

    })

def shop(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    brands = Sub_Category.objects.all()
    home_logo = HomeLogo.objects.all().first()

    return render(request, 'main/shop.html', context={
        'category_list':category_list,
        'product_list':product_list,
        'brands':brands,
        'home_logo':home_logo,
        'link':'shop'

        
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("--------------------VALID-------------")
            Contact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactForm()
    home_logo = HomeLogo.objects.all().first()
    return render(request, 'main/contact-us.html', context={
        'home_logo':home_logo,
        'form':form,
        'link':'contact'

    })


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")
    
