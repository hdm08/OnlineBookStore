from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import forms
from . import models
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import update_session_auth_hash
from django.contrib import messages






import random
def Home(request):
    object = models.SellBook.objects.all()
    l=list(object)
    # print(l)
    if len(l)>=6:
        n=6
    else:
        n = 3
    x=random.sample(l, n)

    print('you are', request.session.get('user_id'))
    print('you are', request.session.get('username'))

    return render(request, 'home.html',{'x':x})
# ______________________________________________________________________________________________________________________


def Register(request):
    form=forms.CreateUserForm()
    if request.method=='POST':
        form=forms.CreateUserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'invalid register credentials')
            return redirect('register')
    return render(request,'register.html',{'RegisterForm':form})
# ______________________________________________________________________________________________________________________


def Login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            form.username = request.POST.get('username')
            form.password = request.POST.get('password1')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            #here session is requested for each user after login
            request.session['user_id']=user.id
            request.session['username']=user.username

            return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('login')
    return render(request, 'login.html', {'LoginForm':form})
# ______________________________________________________________________________________________________________________


def Logout(request):
    logout(request)
    return redirect('/')
# ______________________________________________________________________________________________________________________


def Dashboard(request):
    return render(request, 'dashboard.html')
# _____________________________________________________________________________________________________________________


def SellBook(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = forms.SellBookForm(request.POST,request.FILES)
        else:
            book = models.SellBook.objects.get(pk=id)
            form = forms.SellBookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('sellbookhistory')

    elif request.method=='GET':
        if id == 0:
            form = forms.SellBookForm()
        else:
            book = models.SellBook.objects.get(pk=id)
            form = forms.SellBookForm(instance=book)
        return render(request, "sellbook.html", {'SellBookForm': form})
# ______________________________________________________________________________________________________________________


def DonateBook(request,id=0):
    if request.method=='POST':
        if id==0:
            form=forms.SellBookForm(request.POST,request.FILES)
        else:
            book=models.SellBook.objects.get(pk=id)
            form = forms.SellBookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('donatebookhistory')
    elif request.method=='GET':
        if id == 0:
            form = forms.SellBookForm()
        else:
            book = models.SellBook.objects.get(pk=id)
            form = forms.SellBookForm(instance=book)
        return render(request,'donatebook.html',{'form':form})


from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.shortcuts import render
from .filter import UserFilter



def list_to_queryset(model_list):
    if len(model_list) > 0:
        return model_list[0].__class__.objects.filter(
                    pk__in=[obj.pk for obj in model_list])
    else:
        return []

def BuyBookView(request):

    book_list = models.SellBook.objects.filter(price=0)
    b = models.SellBook.objects.all()

    p = list(book_list)
    q = list(b)
    print(p, q)
    for i in p:
        for j in q:
            if i == j:
                q.remove(j)

    x=list_to_queryset(q)

    book_filter = UserFilter(request.GET, queryset=x)
    book=models.SellBook.objects.values()
    user_list = book_filter.qs
    print(q)

    paginator = Paginator(user_list, 12)
    page = request.GET.get('page', 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    # request.session.get('cart').clear()
    cart=request.session.get('cart')
    if not cart:
        request.session.clear={}

    if request.method == 'POST':
        #it is key=id in key-value ditionary
        book_id = request.POST.get('b.id')
        remove_cart = request.POST.get('remove')

        # print(book_id)
        #cart object which is in seesion is called
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(book_id)
            if quantity:
                if remove_cart:
                    if quantity<=1:
                        cart.pop(book_id)
                    else:
                        cart[book_id]=quantity-1
                else:
                    cart[book_id]=quantity+1
            else:
                cart[book_id] =1
        else:
            cart={}
            cart[book_id]=1

        request.session['cart']=cart #cart object is assinged
        print('cart:',request.session['cart'])
        return redirect('media')

    return render(request, 'buybook.html',{'book':book,'filter':book_filter,'users':users})


# ______________________________________________________________________________________________________________________











def FreeBookView(request):

    book_list = models.SellBook.objects.filter(price=0)
    book_filter = UserFilter(request.GET, queryset=book_list)
    book=models.SellBook.objects.values()
    user_list = book_filter.qs


    paginator = Paginator(user_list, 12)
    page = request.GET.get('page', 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    # request.session.get('cart').clear()
    cart=request.session.get('cart')
    if not cart:
        request.session.clear={}

    if request.method == 'POST':
        #it is key=id in key-value ditionary
        book_id = request.POST.get('b.id')
        remove_cart = request.POST.get('remove')

        # print(book_id)
        #cart object which is in seesion is called
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(book_id)
            if quantity:
                if remove_cart:
                    if quantity<=1:
                        cart.pop(book_id)
                    else:
                        cart[book_id]=quantity-1
                else:
                    cart[book_id]=quantity+1
            else:
                cart[book_id] =1
        else:
            cart={}
            cart[book_id]=1

        request.session['cart']=cart #cart object is assinged
        print('cart:',request.session['cart'])
        return redirect('media')

    return render(request, 'freebook.html',{'book':book,'filter':book_filter,'users':users})





# ______________________________________________________________________________________________________________________


# def Checkout(request):
#
#     return render(request,'checkout.html')
# ______________________________________________________________________________________________________________________


def About(request):
    return render(request,'about.html')
# ______________________________________________________________________________________________________________________


def P_detail(request,myid):
    product = models.SellBook.objects.filter(id=myid)

    object = models.SellBook.objects.exclude(id=myid)
    o=list(object)
    n=3
    x = random.sample(o, n)

    cart = request.session.get('cart')
    if not cart:
        request.session.clear = {}

    if request.method == 'POST':
        # it is key=id in key-value ditionary
        book_id = request.POST.get('b.id')
        remove_cart = request.POST.get('remove')

        # print(book_id)
        # cart object which is in seesion is called
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(book_id)
            if quantity:
                if remove_cart:
                    if quantity <= 1:
                        cart.pop(book_id)
                    else:
                        cart[book_id] = quantity - 1
                else:
                    cart[book_id] = quantity + 1

            else:
                cart[book_id] = 1
        else:
            cart = {}
            cart[book_id] = 1

        request.session['cart'] = cart  # cart object is assinged
        print('cart:', request.session['cart'])







    return render(request, 'p_detail.html', {'product': product[0],'x':x})
# ______________________________________________________________________________________________________________________


def Blog(request):
    return render(request,'blog.html')
# ______________________________________________________________________________________________________________________


def SellBookHistory(request):
    a=models.SellBook.objects.filter(user=request.user, price=0)
    b=models.SellBook.objects.filter(user=request.user)
    x=[]
    p=list(a)
    q=list(b)
    print(p,q)
    for i in p:
        for j in q:
            if i == j:
                q.remove(j)

    print(q)
    paginator = Paginator(q, 12)
    page = request.GET.get('page', 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users':users }
    return render(request,'sellbookhistory.html',context)
# ______________________________________________________________________________________________________________________



def DonateBookHistory(request):
    b=models.SellBook.objects.filter(user=request.user,price=0)

    paginator = Paginator(b, 12)
    page = request.GET.get('page', 1)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users':users }

    return render(request,'donatebookhistory.html',context)
# ______________________________________________________________________________________________________________________

def Book_Delete(request, id):
    book = models.SellBook.objects.get(pk=id)
    book.delete()
    return redirect('history')
# ______________________________________________________________________________________________________________________


def Contact(request):
    form=forms.ContactUsForm()
    if request.method=='POST':
        form = forms.ContactUsForm(request.POST)
        if form.is_valid():
            form.From = request.POST.get('Form')

            form.save()
            return redirect('contact')

    return render(request,'contact.html',{'Cform':form})
# ______________________________________________________________________________________________________________________


def Testimonial(request):
    return render(request,'testimonial.html')
# ______________________________________________________________________________________________________________________


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def ChangePassword(request):
    if request.method == 'POST':
        passform = PasswordChangeForm(request.user, request.POST)
        if passform.is_valid():
            user = passform.save()
            update_session_auth_hash(request, user)  # Important!
            #messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        #else: messages.error(request, 'Please correct the error below.')
    else:
        passform = PasswordChangeForm(request.user)
    return render(request, 'ChangePassword.html', {'passform': passform})


# ______________________________________________________________________________________________________________________
from django.contrib.auth.models import User
def Cart(request):
    # print(request.session.get('cart'))
    ids=request.session.get('cart').keys()
    print(ids)
    book=models.SellBook.get_book_by_id(ids)
    print(book)

    return render(request, 'cart.html',{'book':book})

def Order(request):
    user=request.user
    orders = models.Order.objects.filter(user=user)
    print(orders)
    return render(request , 'orders.html'  , {'orders' : orders})


def Done(request):
    user = request.user
    orders = models.Order.objects.filter(user=user)
    print(orders)
    request.session['cart'] = {}
    return render(request , 'done.html',{'orders':orders})


from .templatetags import cart as c
def Checkout(request):
    ids = request.session.get('cart').keys()
    book = models.SellBook.get_book_by_id(ids)
    p = c.total_cart_price(book, request.session['cart'])
    total_p = int(p) + 100

    shipping='100.00'

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_zip = request.POST.get('postal_zip')
        # user = request.session.get('user')
        cart = request.session.get('cart')
        print(cart)
        book_list = models.SellBook.get_book_by_id(cart.keys())
        print(book_list)
        # print(address, phone, name, cart, city,state,postal_zip,email,user)
        for b in book_list:
            # print(cart.get(str(product.id)))
            order = models.Order(user=request.user,
                                 book=b,
                                 price=b.price,
                                 name=name,
                                 email=email,
                                 address=address,
                                 phone=phone,
                                 city=city,
                                 state=state,
                                 postal_zip=postal_zip,
                                 quantity=cart.get(str(b.id)))
            order.save()
        p = c.total_cart_price(book, request.session['cart'])
        total_p=p+100
        return redirect('done')
        # request.session['cart'] = {}
    para={'p':p,'total_p':total_p,'shipping':shipping}
    return render(request, 'checkout.html',para)