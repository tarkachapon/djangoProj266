from django.shortcuts import render, redirect

from ProfileApp.forms import ProductForm
from ProfileApp.models import Product


# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def education(request):
    return render(request, 'education.html')

def interest(request):
    return render(request, 'interest.html')

def career(request):
    return render(request, 'career.html')

def idol(request):
    return render(request, 'idol.html')

def showData(request):
    id = '65342310266-8'
    name = 'คชาพล พูนพล'
    gender = 'ชาย'
    height = 180
    weight = 80
    food = 'ต้มยำกุ้งน้ำข้น'
    color = 'ฟ้า, น้ำเงิน'
    address = 'ศรีสะเกษ'
    car = 'BMW M5'
    pet = 'สุนัข'
    product = [
        ['BMW01','/static/images/bmw-m8.jpg','BMW M8',17999000],
        ['BMW02', '/static/images/bmw-m7.jpg', 'BMW M760Li', 13539000],
        ['BMW03', '/static/images/bmw-m5.jpg', 'BMW M5', 13399000],
        ['BMW04', '/static/images/bmw-x6.jpg', 'BMW X6', 7299000],
        ['BMW05', '/static/images/bmw-x5.jpg', 'BMW X5', 4799000],
        ['BMW06', '/static/images/bmw-x4.jpg', 'BMW X4', 4099000],
        ['BMW07', '/static/images/bmw-x3.jpg', 'BMW X3', 3659000],
        ['BMW08', '/static/images/bmw-serie-4.jpg', 'BMW Serie 4', 3969000],
        ['BMW09', '/static/images/bmw-serie-3.jpg', 'BMW Serie 3', 3359000],
        ['BMW10', '/static/images/bmw-serie-2.jpg', 'BMW Serie 2', 2169000],
    ]
    context = {'id':id,'name':name,'gender':gender,'height':height,'weight':weight,
               'food':food,'color':color,'address':address,'car':car,'pet':pet,'product':product}
    return render(request,'myShowData.html',context)

lstOurProduct = []

def listProduct(request):
    context = {'product':lstOurProduct}
    return render(request, 'listProduct.html',context)

def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            series = form.get('series')
            bodyTypes = form.get('bodyTypes')
            color = form.get('color')
            system = form.get('system')
            net = form.get('net')

            ProductList = Product(id,series,bodyTypes,color,system,net)
            lstOurProduct.append(ProductList)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'inputProduct.html',context)