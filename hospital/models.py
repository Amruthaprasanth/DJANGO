from django.db import models
class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    date=models.DateField()
class Book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    date=models.DateField()
    isbn=models.CharField(max_length=13)    
class employe(models.Model):
    id=models.IntegerField(primary_key=True)  
    name=models.CharField(max_length=100)
    age=models.IntegerField()  
    phone=models.CharField(max_length=100)
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock_quantity = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField() 

class blog(models.Model):
    title=models.TextField()
    content=models.TextField()
    author= models.CharField(max_length=10)
    date=models.DateTimeField()
class publisher(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    email=models.EmailField()
    def str(self):
        return self.name

class bokk(models.Model):
    title=models.CharField(max_length=20)
    date=models.DateField()
    isbn=models.CharField(max_length=20)
    publi=models.ForeignKey(publisher,on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=255) 
    code = models.CharField(max_length=50, unique=True)
    date = models.DateField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Organizer(models.Model):
    name=models.CharField(max_length=100)
    contact_email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    def str(self):
        return self.name

class Event(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    location=models.CharField(max_length=255)
    organizer=models.ForeignKey(Organizer,on_delete=models.CASCADE)
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    def str(self):
        return self.name
class Product_cate(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.IntegerField()
    stock_quantity=models.IntegerField()
    def str(self):
        return self.namee    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class UserRegistration(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
class usermedia(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    image=models.ImageField(upload_to='image/')
class Image(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField()
    uploaded_at=models.DateTimeField(auto_now_add=True)        