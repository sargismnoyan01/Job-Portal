from django.db import models


# ***Home***
class HomeCarousel(models.Model):
    img=models.ImageField('Imagers',upload_to='Home_media')
    title=models.CharField('Title',max_length=255)
    subtitle=models.CharField('Subtitle',max_length=500)

    def __str__(self) -> str:
        return self.title
    
class JobList(models.Model):
    Full_time='Full Time'
    Part_time='Part Time'
    timetype=[
        ('Full Time',Full_time),
        ('Part Time',Part_time),
    ]
    Marketing = 'Marketing'
    Customer_Service = 'Customer Service'
    Human_Resource = 'Human Resource'
    Project_Management = 'Project Management'
    Business_Development = 'Business Development'
    Sales_and_Communication = 'Sales & Communication'
    Teaching_and_Education = 'Teaching & Education'
    Design_and_Creative = 'Design & Creative'

    category = [
        (Marketing, 'Marketing'),
        (Customer_Service, 'Customer Service'),
        (Human_Resource, 'Human Resource'),
        (Project_Management, 'Project Management'),
        (Business_Development, 'Business Development'),
        (Sales_and_Communication, 'Sales & Communication'),
        (Teaching_and_Education, 'Teaching & Education'),
        (Design_and_Creative, 'Design & Creative'),
    ]

    proff=models.CharField('Job title',max_length=255)
    location=models.CharField('Location',max_length=55)
    jobtime=models.CharField('Job Time',choices=timetype,max_length=50)
    min_salary=models.IntegerField('Min salary')
    max_salary=models.IntegerField('Max salary')
    dt=models.DateField(auto_now_add=True)
    img=models.ImageField('Imagers',upload_to='Jobs_media')
    categories=models.CharField('Category',choices=category,max_length=50,blank=True)
    

    def __str__(self) -> str:
        return self.proff
    
    class Meta:
        verbose_name='Job'
        verbose_name_plural='Jobs'

class JobCreate(models.Model):
    Full_time='Full Time'
    Part_time='Part Time'
    timetype=[
        ('Full Time',Full_time),
        ('Part Time',Part_time),
    ] 
    Marketing = 'Marketing'
    Customer_Service = 'Customer Service'
    Human_Resource = 'Human Resource'
    Project_Management = 'Project Management'
    Business_Development = 'Business Development'
    Sales_and_Communication = 'Sales & Communication'
    Teaching_and_Education = 'Teaching & Education'
    Design_and_Creative = 'Design & Creative'

    category = [
        (Marketing, 'Marketing'),
        (Customer_Service, 'Customer Service'),
        (Human_Resource, 'Human Resource'),
        (Project_Management, 'Project Management'),
        (Business_Development, 'Business Development'),
        (Sales_and_Communication, 'Sales & Communication'),
        (Teaching_and_Education, 'Teaching & Education'),
        (Design_and_Creative, 'Design & Creative'),
    ]

    proff=models.CharField('Job title',max_length=255)
    location=models.CharField('Location',max_length=55)
    jobtime=models.CharField('Job Time',choices=timetype,max_length=50)
    min_salary=models.IntegerField('Min salary')
    max_salary=models.IntegerField('Max salary')
    dt=models.DateField(auto_now_add=True)
    img=models.ImageField('Imagers',upload_to='Jobs_media')
    categories=models.CharField('Category',choices=category,max_length=50,blank=True)
    discription=models.TextField('Job description',null=True)
    responsibility=models.TextField('Responsibility',null=True)
    qualifications=models.TextField('Qualifications',null=True)
    about_company=models.TextField('Company Detail',null=True)
    email=models.EmailField('Email',null=True)
    

    def __str__(self) -> str:
        return self.proff
    
    class Meta:
        verbose_name='Job Create'
        verbose_name_plural='Job Create'

class HomeAbout(models.Model):
    title=models.CharField('Title',max_length=255)
    text=models.TextField("text")
    skill=models.TextField('skill',blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='Home-about'
        verbose_name_plural='Home-about'
    
    
class Apply(models.Model):
    obj=models.ForeignKey(JobCreate,on_delete=models.CASCADE)
    name=models.CharField('Name',max_length=50)
    email=models.EmailField('email')
    portfolio=models.CharField('Portfolio',max_length=100)
    coverlatter=models.TextField('Coverlatter')
    img=models.ImageField('Imagers',upload_to='Apply_media')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Apply'
        verbose_name_plural='Apply'    


class OurCleints(models.Model):
    img=models.ImageField('Imagers',upload_to='Cleint_media')
    text=models.TextField('Text')
    name=models.CharField('Name',max_length=50)
    prof=models.CharField('Profession',max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Cleint'
        verbose_name_plural='Cleints'


class MainCategories(models.Model):
    icon=models.CharField('icon',max_length=255)
    category=models.CharField('Category',max_length=60)


    def __str__(self) -> str:
        return self.category
    
    class Meta:
        verbose_name='Main Category'
        verbose_name_plural="Main Categories"

class Testimonial(models.Model):
    text=models.TextField('Text')
    name=models.CharField('name',max_length=50)
    img=models.ImageField('Imagers',upload_to='Cleint_media')
    prof=models.CharField('Profession',max_length=255)
    email=models.EmailField('email')

    def __str__(self) -> str:
        return self.name
    
class Talent(models.Model):
    typerank = [
        ('Junior', 'Junior'),
        ('Middel', 'Middel'),  
        ('Senior', 'Senior'),
        ('Leader', 'Leader'),  
    ]
    name=models.CharField('Name',max_length=255)
    img=models.ImageField('imagers',upload_to='Talent_media')
    prof=models.CharField('profession',max_length=255)
    jobtime=models.CharField('Job Time',max_length=55)
    rank=models.CharField('rank',choices=typerank,max_length=55)
    address=models.CharField('Addres',max_length=255)
    coverlatter=models.TextField('Coverlatter')
    email=models.EmailField('email',null=True)
    skill=models.TextField('skills',null=True)
    summery=models.TextField('summery',null=True)

    def __str__(self) -> str:
        return self.prof

    class Meta:
        verbose_name='Talent'
        verbose_name_plural='Talents'    
    

class ContactUs(models.Model):
    address=models.CharField('address',max_length=50)
    email=models.EmailField('email')
    phone=models.CharField('prone',max_length=18)


    def __str__(self) -> str:
        return self.phone
    
    class Meta:
        verbose_name='Contact Us'
        verbose_name_plural='Contact Us'


class MessageModel(models.Model):
    name=models.CharField('name',max_length=50)
    email=models.EmailField('email')
    subject=models.CharField('Subject',max_length=255)
    message=models.TextField('Message')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Message'
        verbose_name_plural='Messages'

