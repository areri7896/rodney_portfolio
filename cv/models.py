from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # username = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField
    alt_emails = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(blank=True, max_length=10)
    alt_phone_number = models.CharField(blank=True, max_length=100)
    git_hub_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    address = models.CharField(blank=True, max_length=50)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    language = models.CharField(blank=True, max_length=50)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="profile_pic")

    def __str__(self):
        return self.email


class Expertise(models.Model):
    class Meta:
        verbose_name_plural = 'Expertise'
        verbose_name = 'Expertise'

    course_name = models.CharField(blank=True, max_length=50)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    school = models.CharField( max_length=50)
    period_from = models.CharField( max_length=50)
    period_to = models.CharField( max_length=50)
    is_key_expertise = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name


class Project(models.Model):
    portfolio_image = models.ImageField(upload_to="portfolio_image", blank=True, null=True)
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    period_done = models.CharField(max_length=20)

    def __str__(self):
        return self.project_name


class Education(models.Model):
    class Meta:
        verbose_name_plural = 'Education'
        verbose_name = 'Education'

    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField(blank=True)
    school = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    is_key_education = models.BooleanField(default=False)

    def __str__(self):
        return self.course


class Skill(models.Model):
    pass


class Webinar(models.Model):
    w_name = models.CharField(max_length=100)
    date_conducted = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.w_name


class Service(models.Model):
    icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.service_name