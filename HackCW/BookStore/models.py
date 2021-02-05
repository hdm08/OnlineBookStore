from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

def get_upload_path(instance,filename):
    return 'document/{0}/{1}'.format(instance.user.username,filename)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    # [username,firsname,lastname,email]
    picture = models.ImageField(upload_to=get_upload_path, default='no-img.jpg', blank=True)
    address=models.CharField(max_length=200,default='')
    city=models.CharField(max_length=100,default='')
    pincode=models.IntegerField(default='00')
    state=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default='0')
    university_name=models.CharField(max_length=200,default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



class SellBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path, default='no-img.jpg')
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300,default='')
    college_name=models.CharField(max_length=200,default='')
    book_university=models.CharField(max_length=200,default='')
    seller_name=models.CharField(max_length=200,default='')
    seller_email=models.EmailField(default='')


    @staticmethod
    def get_book_by_id(ids):
        #id__in is used for list here ids are list
        return SellBook.objects.filter(id__in=ids)


    def __str__(self):
      if self.price==0:
          return 'Donate Book: {}'.format(self.name)
      else:
          return 'Selling Book: {}'.format(self.name)

def create_book(sender, **kwargs):
    if kwargs['created']:
        sellbook = SellBook.objects.create(user=kwargs['instance'])
post_save.connect(create_book, sender=User)



class ContactUs(models.Model):
    username=models.CharField(max_length=100, default="")
    From=models.EmailField(max_length=100, default="")
    Subject=models.CharField(max_length=100, default="")
    Message=models.CharField(max_length=1000, default="")


    def __str__(self):
        return self.username


import datetime


class Order(models.Model):
    book = models.ForeignKey(SellBook,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    name=models.CharField(max_length=100, default="")
    email=models.EmailField(default="")
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    postal_zip = models.CharField(max_length=100, default="")

    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    def __str__(self):
        return self.name


    @staticmethod
    def get_orders_by_book(book_id):
        return Order.objects.filter(book=book_id).order_by('-date')