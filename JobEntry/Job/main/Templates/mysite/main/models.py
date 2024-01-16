from django.db import models

# Create your models here.

class HomeLogo(models.Model):

    logo = models.ImageField('Home logo', upload_to='index_images')
    date = models.DateTimeField('Home logo date', auto_now=True)

class HomeCaruselActive(models.Model):

    name1 = models.CharField('Carusel name1', max_length=100)
    name2 = models.CharField('Carusel name2', max_length=100)
    about = models.TextField('Carusel about')
    button_name = models.CharField('Carusel button name', max_length=40)
    img = models.ImageField('Carusel image', upload_to='index_images')
    price_image = models.ImageField('Carusel price image', upload_to='index_images')

    def __str__(self):
        return self.name1

class HomeCarusel(models.Model):

    name1 = models.CharField('Carusel name1', max_length=100)
    name2 = models.CharField('Carusel name2', max_length=100)
    about = models.TextField('Carusel about')
    button_name = models.CharField('Carusel button name', max_length=40)
    img = models.ImageField('Carusel image', upload_to='index_images')
    price_image = models.ImageField('Carusel price image', upload_to='index_images')

    def __str__(self):
        return self.name1

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Sub_Category(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categ')
    name = models.CharField('Sub category name', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub_Category'
        verbose_name_plural = 'Sub_Categories'

class Panel(models.Model):
    name = models.CharField('Category', max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, related_name='sub_prod')
    name = models.CharField('Product name', max_length=50)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='index_images')
    logo = models.ImageField('Product image logo', upload_to='index_images', blank=True)
    date = models.DateTimeField('Product create date', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Cart(models.Model):

    prod = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductType(models.Model):
    sub_type = models.ForeignKey(Panel, on_delete=models.CASCADE, related_name='type_key')
    name = models.CharField('Product name', max_length=50)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='index_images')
    logo = models.ImageField('Product image logo', upload_to='index_images', blank=True)
    date = models.DateTimeField('Product create date', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Contact(models.Model):
    contact_name = models.CharField('Name', max_length=50)
    user_email = models.CharField('Email', max_length=50)
    subject = models.CharField('Subject', max_length=255)
    massage = models.TextField('Massage')

    def __str__(self):
        return self.contact_name