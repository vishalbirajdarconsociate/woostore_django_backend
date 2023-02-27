from django.db import models

# Create your models here.
class Customer(models.Model):
    customerFirstName=models.CharField( max_length=50,default='')
    customerLastName=models.CharField( max_length=50,default='')
    customerUsername=models.CharField( max_length=100)
    customerPassword=models.CharField( max_length=100)
    customerEmail=models.CharField(max_length=254)
    
    customerAddress=models.TextField()
    customerImg=models.ImageField(upload_to='static/img/customer/', height_field=None, width_field=None, max_length=None,default='static/img/default/customer/default_user.png',blank=True)
    def __str__(self):
        return self.customerFirstName


class Product(models.Model):
    productName=models.CharField( max_length=50)
    SKU=models.CharField( max_length=50)
    productPrice=models.FloatField()
    productDesc=models.TextField()
    productStock=models.IntegerField()
    productImg=models.ImageField( upload_to='static/img/product/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.productName

class Category(models.Model):
    categoryName=models.CharField( max_length=50)
    categoryDesc=models.TextField()
    categoryImg=models.ImageField( upload_to='static/img/Category/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.categoryName


class ProductCategory(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.product.productName+" | "+self.category.categoryName

    
class Reviews(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    review=models.TextField()
    rating=models.FloatField()
    def __str__(self):
        return self.product.productName+" | "+self.customer.customerFirstName

    
class PaymentMethods(models.Model):
    methodName=models.CharField( max_length=50)
    methodDesc=models.CharField( max_length=50)
    getway=models.CharField( max_length=50)
    def __str__(self):
        return self.methodName


class Discount(models.Model):
    discountCode=models.CharField( max_length=50)
    discountValue=models.FloatField()
    discountDesc=models.TextField()
    def __str__(self):
        return self.discountCode

    
class Cart(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)


class CartContain(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()


class ProductImages(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/img/product_images/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.product.productName+" | image "+str(self.pk)
    