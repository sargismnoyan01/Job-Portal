from django.contrib import admin
from .models import *


admin.site.register(HomeAbout)
admin.site.register(MainCategories)
admin.site.register(Testimonial)
admin.site.register(Saved)
admin.site.register(ContactUs)
admin.site.register(OneUser)

@admin.register(Apply)
class ApplyModelAdmin(admin.ModelAdmin):
    list_display=['name','obj','phone'] 
    list_display_links=['name','obj','phone']
    search_fields=['name','obj','phone']


@admin.register(HomeCarousel)
class HomeCarouselHodelAdmin(admin.ModelAdmin):
    list_display=['title','subtitle']
    list_display_links=['title','subtitle']
    search_fields=['title','subtitle']

@admin.register(JobCreate)
class JobCreateListModelAdmin(admin.ModelAdmin):
    list_display=['proff','location','dt']
    list_display_links=['proff','location','dt']
    search_fields=['proff','location','dt']


@admin.register(Talent)
class TalentModelAdmin(admin.ModelAdmin):
    list_display=['name','rank','prof']
    search_fields=['name','rank','prof']

@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display=['name']
    list_display_links=['name']
    search_fields=['name']


@admin.register(UserInfo)
class UserInfoModelAdmin(admin.ModelAdmin):
    list_display=['prof','skills']
    list_display_links=['prof','skills']
    search_fields=['prof','skills']