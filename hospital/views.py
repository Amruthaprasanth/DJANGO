from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import*
def fun1(request):
    return HttpResponse("hihello")
def fun2(request):
    return HttpResponse("<h1>good morning</h1>")
def fun3(request):
    return render(request,"h1.html",{'name':'PRASANTH'})
def fun4(request):
    context={"fruits":['apple','banana','cherry'],}
    return render(request,'fruit.html',context)
def fun5(request):
    items=[{'name':'laptop','price':200,'quantity':10},{'name':'phone','price':300,'quantity':1},{'name':'tv','price':310,'quantity':12}]
    return render(request,'item.html',{'item':items})
def fun6(request):
    context = {
        "products": [
            {"name": "Laptop", "price": 200, "in_stock": "In Stock"},
            {"name": "Smartphone", "price": 300, "in_stock": "Out of Stock"},
            {"name": "Tablet", "price": 210, "in_stock": "In Stock"},
            {"name": "Headphones", "price": 140, "in_stock": "In Stock"},
        ]
    }
    return render(request, 'product.html', context)
def fun7(request):
    data=user.objects.all()
    return render(request,"all.html",{"data1":data})
def fun8(request):
    if request.method == "POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        user_obj=user()
        user_obj.user_id=id
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.date=date
        user_obj.save()
    return render(request,"form.html")
def fun9(request):
    if request.method == "POST":
        id=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        book_obj=Book()
        book_obj.book_id=id
        book_obj.title=title
        book_obj.author=author
        book_obj.date=date
        book_obj.isbn=isbn
        book_obj.save()
    return render(request,"bookadd.html")
def fun10(request):
    details=Book.objects.all()
    return render(request,'display.html',{'display':details})
def fun11(request):
    if request.method == "POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        emp_obj=employe()
        emp_obj.id=id
        emp_obj.name=name
        emp_obj.age=age
        emp_obj.phone=phone
        emp_obj.save()
        return redirect('as')
    return render(request,"empadd.html")
def fun12(request):
    details=employe.objects.all()
    return render(request,'display_emp.html',{'display':details})
def create_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock_quantity = request.POST.get('stock_quantity')
        product_obj = Product()
        product_obj.name = name
        product_obj.description = description
        product_obj.price = price
        product_obj.stock_quantity = stock_quantity
        product_obj.save()
        return redirect('product_list')
    return render(request, "create_product.html")  
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'display': products})  
def delete_user(request,id):
    user=employe.objects.get(id=id) 
    user.delete()
    return redirect("as")
def update_user(request,id):
    user=employe.objects.filter(id=id)
    if request.method=='POST':
        ID=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        emp_obj=employe()
        emp_obj.id=id
        emp_obj.name=name
        emp_obj.age=age
        emp_obj.date=date
        emp_obj.save()
        return redirect('as')
    return render(request,"update.html",{'user1':user})
def cus_add(request):
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=request.POST.get('dob')
        cus=Customer()
        cus.first_name=f_name
        cus.last_name=l_name
        cus.email=email
        cus.phone_number=phone
        cus.address=address
        cus.date_of_birth=date
        cus.save()
        return redirect('display_customer')
    return render(request,'add_customer.html')
def cus_display(request):
    value=Customer.objects.all()
    return render(request,'customer_details.html',{'customer':value})
def cus_update(request,id):
    update=Customer.objects.get(id=id)
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=request.POST.get('date')
        update.first_name=f_name
        update.last_name=l_name
        update.email=email
        update.phone_number=phone
        update.address=address
        update.date_of_birth=date
        update.save()
        return redirect('display_customer')
    return render(request,'update_cust.html',{'update':update})
def cus_delete(request,id):
    value=Customer.objects.get(id=id)
    value.delete()
    return redirect('display_customer')
def fun8(request):
    if request.method =='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        date=request.POST.get('date')
        user_obj=blog()
        user_obj.title=title
        user_obj.content=content
        user_obj.author=author
        user_obj.date=date
        user_obj.save()
        return redirect('di')
    return render(request,'b.html')
def dis(request):
    data=blog.objects.all()
    return render(request,"bt.html",{'data1':data})
def upda(request,pk):
    user=blog.objects.get(pk=pk)
    if request.method == 'POST':
        date=request.POST.get('date')
        user.date=date
        user.save()
        return redirect('di')
    return render(request,"nb.html",{"user":user})
def f9(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        user_obj=publisher()
        user_obj.name=name
        user_obj.address=address
        user_obj.email=email
        user_obj.save()
        return redirect('bh')
    return render(request,'p.html')
def disf(request):
    data=publisher.objects.all()
    return render(request,"pt.html",{'dat':data})

def f15(request):
    dd=publisher.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')

        user=bokk()
        user.title=title
        user.date=date
        user.isbn=isbn

        user.publi=publisher.objects.get(id=request.POST.get('id'))
        user.save()
        return redirect('b')
    return render(request,'bp.html',{'d':dd})

def disb(request):
    data=bokk.objects.all()
    return render(request,"btt.html",{'da':data})

def updatt(request,pk):
    data5=publisher.objects.all()
    user1=bokk.objects.get(pk=pk)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        publi=request.POST.get('publi')

        user1.title=title
        user1.date=date
        user1.isbn=isbn
        user1.publi=publi
        user1.publi=publisher.objects.get(id=request.POST.get('id'))
        user1.save()
        return redirect('b')
    return render(request,"nbk.html",{"user":user1,'das':data5})

def de(request,pk):
    user=bokk.objects.get(pk=pk)
    user.delete()
    return redirect('b')

def add_student(request):
    courses = Course.objects.all()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        course = Course.objects.get(id=request.POST.get('course'))
        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            course=course
        )
        student.save()
        return redirect('displayStudents')
    return render(request, 'add_student.html', {'courses': courses})

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {'students': students}) 
def displaySpecificStudent(request,id):
    data=Student.objects.get(id=id)
    return render(request,'display_specific_student.html',{'specific':data})    


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {'courses': courses}) 
def updateStudent(request,id):
    data=Student.objects.get(id=id)
    dataa=Course.objects.all()
    if request.method == 'POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone')
        data.first_name=first_name
        data.last_name=last_name
        data.email=email
        data.phone_number=phone_number
        data.course=Course.objects.get(id=request.POST.get('course'))
        data.save()
        return redirect('displayStudents')
    return render(request,'update_student.html',{'data1':data,'data2':dataa})
def deleteStudent(request,id):
    dele=Student.objects.get(id=id)
    dele.delete()
    return redirect('displayStudents')
def organizerget(request):
    oraganizer=Organizer.objects.all()
    return render(request,"organizer_get.html",{'data':oraganizer})

def organizeradd(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        organizer_obj=Organizer()
        organizer_obj.name=name
        organizer_obj.contact_email=email
        organizer_obj.phone_number=phno
        organizer_obj.save()
        return redirect('or')
    return render(request,"organizeradd.html")

def organizer_del(request,id):
    orgainzer=Organizer.objects.get(id=id)
    orgainzer.delete()
    return redirect('or')

def organizer_update(request,id):
    orgainzer=Organizer.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        orgainzer.name=name
        orgainzer.contact_email=email
        orgainzer.phone_number=phno
        orgainzer.save()
        return redirect('or')
    return render(request,"update_organizer.html",{'data':orgainzer})

from django.db.models import Q
def eventget(request):
    event=Event.objects.all()
    if request.method == 'POST':
        value=request.POST.get('search')
        srch=Event.objects.filter(Q(title__icontains=value))
        return render(request,"em_display_event.html",{'data':srch})
    return render(request,"event_get.html",{'data':event})

def eventadd(request):
    organizer=Organizer.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        lcn=request.POST.get('location')
        event_obj=Event()
        event_obj.title=title
        event_obj.date=date
        event_obj.location=lcn
        event_obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        event_obj.save()
        return redirect('ev')
    return render(request,"eventadd.html",{'data':organizer})

def event_del(request,id):
    event=Event.objects.get(id=id)
    event.delete()
    return redirect('ev')

def event_update(request,id):
    organizer=Organizer.objects.all()
    event=Event.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        lcn=request.POST.get('location')
        event.title=title
        event.date=date
        event.location=lcn
        event.organizer=Organizer.objects.get(id=request.POST.get('org'))
        event.save()
        return redirect('ev')
    return render(request,"update_event.html",{'data':event,'data2':organizer})
def add_product_cate(request):
    data=Category.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        obj=Product_cate()
        obj.name=name
        obj.price=price
        obj.stock_quantity=quantity
        obj.category=Category.objects.get(id=request.POST.get('categ'))
        obj.save()
        return redirect('display_product_cate')
    return render(request,'c_add_product.html',{'dataa':data})
def display_product_cate(request):
    data=Product_cate.objects.all()
    return render(request,'c_display_product.html',{'dataa':data})
def update_product_cate(request,id):
    data=Category.objects.all()
    obj=Product_cate.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        obj.name=name
        obj.price=price
        obj.stock_quantity=quantity
        obj.category=Category.objects.get(id=request.POST.get('categ'))
        obj.save()
        return redirect('display_product_cate')
    return render(request,'c_update_product.html',{'dataa':data,'obj':obj})
def delete_product_cate(request,id):
    data=Product_cate.objects.get(id=id)
    data.delete()
    return redirect('display_product_cate')

def display_products_in_stock(request):
    products_in_stock = Product.objects.filter(stock_quantity__gt=3)
    
    return render(request, 'display_products.html', {'products': products_in_stock})
def loading(request):
    return render(request,'login.html')
def post_get(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", {'data': posts})

def post_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        post_obj = Post(title=title, content=content)
        post_obj.save()
        
        return redirect('post_list')
    return render(request, "post_add.html")
from .forms import *
def post_v(request):
    if request.method == 'POST':
        form=postform(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=postform()
            return render(request,"posth.html",{'form':form})
def add_userRegistration(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserRegistrationForm()
    return render(request,'userss.html',{'form':form})        
def media(request):
    i=usermedia.objects.all()
    return render(request,"media.html",{'image':i})
def add_image(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        image=request.FILES.get('img')
        obj=Image()
        obj.title=title
        obj.image=image
        obj.save()
        return redirect('ag')
    return render(request,'image_form.html')
def view_image(request):
    data=Image.objects.all()
    v=data.values()
    print(v)
    return render(request,'image_view.html',{'dataa':data})
def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def products(request):
    return render(request, "products.html")
def base2(request):
    return render(request,"base2.html")
def home2(request):
    return render(request,"home2.html")