from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView,DetailView
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from Job.settings import EMAIL_HOST_USER
from django.core.paginator import Paginator
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string



# ***Home***
class HomeListView(ListView):
    template_name='index.html'


    def get(self,request):
        homecarousel=HomeCarousel.objects.all()
        jobcreate=JobCreate.objects.all().order_by('-likes')
        ourcleint=Testimonial.objects.filter(id__in=[1,2,3,4,5,6]) 
        homeabout=HomeAbout.objects.get()
        maincategories=MainCategories.objects.all()
        contactus=ContactUs.objects.get()



        context={
            'link':'home',
            'ourcleint':ourcleint,
            'homecarousel':homecarousel,
            'jobcreate':jobcreate,
            'homeabout':homeabout,
            'maincategories':maincategories,
            'contactus':contactus

                }
        
        return render(request,self.template_name,context)


def SearchWord(request):
    ourcleint=Testimonial.objects.filter(id__in=[1,2,3,4,5,6])
    contactus=ContactUs.objects.get()

    jobcreate=JobCreate.objects.filter(proff__icontains=request.GET.get('p'),
                        categories__icontains=request.GET.get('c'),location__icontains=request.GET.get('l'),\
                            jobtime__icontains=request.GET.get('j'))
    return render(request,'index.html',{
                                        'link':'Search',
                                        'jobcreate':jobcreate,
                                        'ourcleint':ourcleint,
                                        'contactus':contactus})



# ***Create***
class CreateDetalView(DetailView):
    template_name='create.html'
    def get(self,request):
        userinfo=UserInfo.objects.get(obj=request.user)
        form=CreateForm
        contactus=ContactUs.objects.get()


        return render(request,self.template_name,{'form':form,
                                                  'contactus':contactus,
                                                  'link':'Create',
                                                  'userinfo':userinfo,

                                                  })
    
    def post(self,request):
        
        usern=UserInfo.objects.get(obj=request.user)
        form=CreateForm(request.POST,request.FILES)
        subject='Նոր Նամակ JobEntry-ից'
        body=f'''Բարև։{request.POST.get('proff')}-ի վերաբերյալ ձեր աշխատաքի հայտարարությունը հաջողությամբ կատարվել է։
            Շնորհակալություն մեր կայքից օգտվելու համար։ 
            Ձեր ընթացիք միավորները կազմում են {request.POST.get('point')}'''
        if form.is_valid():
            usern.points -= 1
            form.save()
            email=EmailMessage(
                subject=subject,
                body=body,
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')]
               )
            email.send()
            return redirect('home')
        else:
            form=CreateForm()

        return render(request,self.template_name,{'form':form})
    

# ***List***
class JobListView(ListView):
    template_name='job-list.html'

    def get(self,request):
        contactus=ContactUs.objects.get()
        p=Paginator(JobCreate.objects.all().order_by('-id'),6)
        page=request.GET.get('page')
        create=p.get_page(page)
        context={
            'link':'Job List',
            'create':create,
            'contactus':contactus
                }
        
        return render(request,self.template_name,context)

# ***Detail*** 
class JobDetail(DetailView):
    template_name='job-detail.html'

    def get(self,request,id):
        jobcreate=JobCreate.objects.all()
        subjob=JobCreate.objects.filter(pk=id)
        contactus=ContactUs.objects.get()

        form=ApplyForm


        context={
            'link':'Job Detail',
            'subjob':subjob,
            'form':form,
            'jobcreate':jobcreate,
            'contactus':contactus,
                }
        return render(request,self.template_name,context)
        
        
    def post(self,request,id):
        subjobi=get_object_or_404(JobCreate,pk=id)
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.obj=subjobi
            obj.save()

            subject=f'Նոր տեղեկություն ձեր տեղադրած {subjobi.proff} հաստիքի վերաբերյալ'
            message=f'''
            name-    {request.POST.get('name')} |   
            email-   {request.POST.get('email')} |
            Phone-   {request.POST.get('phone')} |
            coverlatter-   {request.POST.get('coverlatter')} |
            Resiume - Դիտել հիմա։
            '''
            from_email=EMAIL_HOST_USER
            recipient_list=[subjobi.email]
            html_message=render_to_string('email_template.html',{'subject':subject,'content':message,})
            send_mail(subject,message,from_email,recipient_list,html_message=html_message)

            return redirect('joblist')
        else:
            form=ApplyForm()
        
        context={
            'subjobi':subjobi,
            'form':form,
                }
        
        return render(request,self.template_name,context)

# ***About***
class AboutDetalView(DetailView):
    template_name='about.html'

    def get(self,request):
        homeabout=HomeAbout.objects.get()
        contactus=ContactUs.objects.get()

        context={
            'link':'about',
            'homeabout':homeabout,
            'contactus':contactus,
                }
        return render(request,self.template_name,context)

# ***Testimonial***
class TestimonialView(ListView):
    template_name='testimonial.html'

    def get(self,request):
        form=TestForm
        testimonial=Testimonial.objects.filter(id__in=[1,2,3,4,5]).order_by('-id')
        contactus=ContactUs.objects.get()

        context={
            'link':'Testimonial',
            'form':form,
            'testimonial':testimonial,
            'contactus':contactus,
                }
        
        return render(request,self.template_name,context)
    
    def post(self,request):
        form=TestForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            subject = f'''ԲԱրև {request.POST.get('name')}'''
            message = f'''
                Ձեր կարծիքը կարևոր է մեզ համար \U0001F917
                '''
            from_email = EMAIL_HOST_USER
            recipient_list = [request.POST.get('email')]

            html_message = render_to_string('email_template.html', {'subject': subject, 'content': message,})

            send_mail(subject, message, from_email, recipient_list, html_message=html_message)

            return redirect('home')
        else:
            form = TestForm()

        return render(request, 'testimonial.html', {'form': form})

# ***Resiume***
class Resiume(ListView):
    template_name='resiume.html'

    def get(self,request):
        form=TalentForm
        contactus=ContactUs.objects.get()
        context={
            'link':'Resiume',
            'form':form,
            'contactus':contactus,

                }
        
        return render(request,self.template_name,context)
    

    def post(self,request):

        form=TalentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('joblist')
        else:
            form=TalentForm()

        return render(request,self.template_name,{'form':form})
    
# ***Talant***
class TalantListView(ListView):
    template_name='talent.html'


    def get(self,request):
        p=Paginator(Talent.objects.all(),5)
        contactus=ContactUs.objects.get()

        page=request.GET.get('page')
        talan=p.get_page(page)



        return render(request,self.template_name,{'talan':talan,
                                                  'contactus':contactus,
                                                  'link':'Talents'})

# ***TalentDetai*** 
class TalentDetailView(DetailView):
    template_name='talent-detail.html'
    def get(self,request,id):
        subtalent=Talent.objects.filter(pk=id)
        contactus=ContactUs.objects.get()

        context={
            'link':'Talent',
            'subtalent':subtalent,
            'contactus':contactus,
                }
        return render(request,self.template_name,context)
    
# ***Contact***
class ContactView(ListView):
    template_name='contact.html'

    def get(self,request):
        contactus=ContactUs.objects.get()
        form=MessageForm
        context={
            'link':'Contact Us',
            'contactus':contactus,
            'form':form
                }
        
        return render(request,self.template_name,context)
    
    def post(self,request):
        contactus=ContactUs.objects.get()
        form=MessageForm(request.POST)
        if form.is_valid():
            form.save()
            email=EmailMessage(
                subject=f'Բարև սիրելի {request.POST.get("name")}',
                body='''Ձեր կարծիքը կարևոր է մեզ համար։Շարունակեք ձեր գործունեություն
                և ձեր գործերին բարի ընթացք ։—)''',
                from_email=EMAIL_HOST_USER,
                to=[request.POST.get('email')]
            )
            email.send()
            return redirect('contact')
        else:
            form=MessageForm()
            messages.warning(request,'There are incorrect or missing data')

        return render(request,self.template_name,{
                                            'contactus':contactus,
                                            'form':form,
                                                })


def Register(request):
    contactus=ContactUs.objects.get()
    form=CretionUserForm()
    if request.method=='POST':
        form=CretionUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.warning(request,'Review the filled data and try again')

    return render(request,'register.html',{'form':form,
                                           'contactus':contactus,
                                           'link':'Register Page'})


def LoginPage(request):
    contactus=ContactUs.objects.get()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Incorrect username or password')

    return render(request,'login.html',{'contactus':contactus,
                                        'link':'Login Page'})

def LogoutPage(request):
    logout(request)
    
    return redirect('home')
        
def custom_404_view(request,exception):
    return render(request, '404.html', status=404)



def like(request,jobcreate_id):
    user=request.user
    jobcreate=JobCreate.objects.get(id=jobcreate_id)
    current_likes=jobcreate.likes
    liked=Likes.objects.filter(user=user,jobcreate=jobcreate).count()
    if not liked:
        liked=Likes.objects.create(user=user,jobcreate=jobcreate)
        current_likes=current_likes + 1
    else:
        liked=Likes.objects.filter(user=user,jobcreate=jobcreate).delete()
        current_likes=current_likes - 1
    jobcreate.likes=current_likes
    jobcreate.save()
    return redirect('detail', id=jobcreate_id)


class UserPage(DetailView):
    template_name='user.html'

    def get(self,request,id):
        user=User.objects.filter(pk=id)
        usern=request.user
        usern.username=usern.username.capitalize()
        # userinfo=UserInfo.objects.get(user=usern)

        context={
                'user':user,
                'usern':usern,
                # 'userinfo':userinfo
                }
        return render(request,self.template_name,context)
    




class UserFormView(ListView):
    template_name='user1.html'

    def get(self,request):
        form=UserForm

        context={
                'form':form,  
                }
        

        return render(request,self.template_name,context)

    def post(self,request):
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.obj=request.user
            obj.save()
            return redirect('home')
        else:
            form=UserCreationForm()

        return render(request,self.template_name,{'form':form})
    
class SearchUser(ListView):
    template_name = 'searchuser.html'

    def get(self,request):
        me=request.user
        user=User.objects.all()
        subuser=User.objects.filter()
        context={
            'me':me,
            'user':user,
            'subuser':subuser,


                }
        
        return render(request,self.template_name,context)
    
def SearchWorker(request):
    me=request.user
    subuser=User.objects.filter()
    user=User.objects.filter(username__icontains=request.GET.get('u'))

    context={
        'me':me,
        'subuser':subuser,
        'user':user,
            }
    
    return render(request,'searchuser.html',context)

def Saves(request,id):
    job=JobCreate.objects.get(pk=id)
    user=request.user
    current_savec=job.savec
    current_moment = job.dissave
    saved=Saved.objects.filter(job=job,user=user).count()
    if not saved:
        saved=Saved.objects.create(user=user,job=job)
        current_savec=current_savec + 1
        current_moment = False

    else:
        saved=Saved.objects.filter(user=user,job=job).delete()
        current_savec=current_savec - 1
        current_moment = True

    job.savec=current_savec
    job.dissave = current_moment
    job.save()

    return redirect('savepage')

class SavePage(ListView):
    template_name='savepage.html'

    def get(self,request):
        contactus=ContactUs.objects.get()
        user=request.user
        job=Saved.objects.filter(user=user)
        context={
            'link':'savepage',
            'job':job,
            'contactus':contactus,
                }
        
        return render(request,self.template_name,context)
    
def SerachTalent(request):
    talan=Talent.objects.filter(prof__icontains=request.GET.get('prof'),\
                                rank__icontains=request.GET.get('rank'))
    
    context={
        'talan':talan,

            }
    
    return render(request,'talent.html',context)



def analyse(request):
    jobcreate=JobCreate.objects.count()
    user=User.objects.count()
    users=User.objects.all()
    subuser=User.objects.filter()
    resiume=Talent.objects.count()
    return render(request,'analyse/index_analyse.html',{'jobcreate':jobcreate,
                                                        'user':user,
                                                        'resiume':resiume,
                                                        'users':users,
                                                        'subuser':subuser
                                                        })


