from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from . models import Categories,Product,Customer,Cart
import os
from django.db.models import Q
# Create your views here.
def home(req):
    cat = Categories.objects.all()
    cat1 = Categories.objects.get(id=1)
    mob = Product.objects.filter(Pro_Cat=cat1)[:4]
    cat2 = Categories.objects.get(id=2)
    lap = Product.objects.filter(Pro_Cat=cat2)[:4]
    return render(req,'home.html',{'cat':cat,'mob':mob,'lap':lap})

def allpro(req,id):
    pro = Product.objects.filter(Pro_Cat=id)
    cat = Categories.objects.get(id=id)
    cat1 = Categories.objects.all()
    return render(req,'allpro.html',{'pro':pro,'c':cat,'cat':cat1})

def adminpage(req):
    return render(req,'admin.html')

def buy(req,id):
    print("cart")
    cust = Customer.objects.get(user=req.user)
    prod = Product.objects.get(id=id)
    if Cart.objects.filter(Q(cust=cust) & Q(prod=prod)).exists():
        buy1 = Cart.objects.get(Q(cust=cust) & Q(prod=prod))
        print(buy1.Quantity)
        buy1.Quantity = buy1.Quantity+1
    else:
        buy1 = Cart(cust=cust,prod=prod,Quantity=1)
    buy1.save()
    return redirect('cart_pro')
def adds(req,id):
    buy1 = Cart.objects.get(id=id)
    buy1.Quantity +=1 
    buy1.save()
    return redirect('cart_pro')

def decr(req,id):
    buy1 = Cart.objects.get(id=id)
    if buy1.Quantity==1:
        return redirect('delete_cart',id=id)
    else:
        buy1.Quantity -=1 
        buy1.save()
        return redirect('cart_pro')
def cart_pro(req):
    cust = Customer.objects.get(user=req.user)
    buys = Cart.objects.filter(cust=cust)
    sub_total = sum(items.total_price() for items in buys)
    return render(req,'cart.html',{'crt':buys,'total':sub_total})
def logout(req):
    auth.logout(req)
    return redirect('home')

def login1(req):
    if req.method == "POST":    
        username = req.POST['uname'] 
        password = req.POST['pass']
        user = auth.authenticate(username=username,password = password)
        if user is not None:
            if user.is_staff:
                auth.login(req,user)
                return redirect('adminpage')
            else:
                auth.login(req,user)
               
                return redirect('home')
        else:
            return redirect('login')
    return render(req,'login.html')

def cat_reg(req):
    if req.method == 'POST':
        cname = req.POST['cname']
        cat = Categories(Cat_Name=cname)
        cat.save()
        return redirect('adminpage')
    return render(req,'cat_reg.html')

def pro_reg(req):
    cat = Categories.objects.all()
    if req.method == 'POST':
        pname = req.POST['pname']
        price = req.POST['price']
        pdesc = req.POST['pdesc']
        pimage = req.FILES['image']
        cid = req.POST['cat']
        category = Categories.objects.get(id = cid)
        pro = Product(Pro_Name=pname,Pro_Price=price,Pro_Desc=pdesc,Pro_Image=pimage,Pro_Cat=category)
        pro.save()    
        return redirect('adminpage')
    return render(req,'pro_reg.html',{'cat':cat})

def products(req):
    pro = Product.objects.all()
    return render(req,'products.html',{'pro':pro})

def pdelete(req,id):
    pro = Product.objects.get(id=id)
    pro.delete()
    return redirect('products')

def register(req):
    if req.method == 'POST':
        fname = req.POST['fname']
        lname = req.POST['lname']
        uname = req.POST['uname']
        email = req.POST['email']
        age = req.POST['age']
        addr = req.POST['addr']
        number = req.POST['number']
        image = req.FILES['image']
        passw = req.POST['password']
        cpass = req.POST['cpassword']
        if passw == cpass:
            auser = User.objects.create_user(first_name = fname,last_name = lname,password = passw,username = uname,email = email)
            auser.save()
            print(auser.username)
            c_user = User.objects.get(username = uname)
            custom = Customer(user = c_user,Age = age,Number = number,Address = addr,Image =image)
            print("saved")    
            custom.save()
        
            return redirect('home')
    return render(req,'register.html')

def users(req):
    cus = Customer.objects.all()
    return render(req,'users.html',{'cus':cus})

def delete(req,id):
    custom = Customer.objects.get(user=id)
    custom.delete()
    auser = User.objects.get(id=id)
    auser.delete()
    return redirect('users')

def delete_cart(req,id):
    buys = Cart.objects.get(id=id)
    buys.delete()
    return redirect('cart_pro')
def checkout(req):
    return render(req,'check.html')