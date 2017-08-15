from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,  UserManager, BaseUserManager
from django.conf import settings

class SocialUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address",
                              max_length=254,
                              unique=True,
                              )

    first_name = models.CharField("first name",
                                  max_length=30,
                                  blank=True)
    last_name = models.CharField("last name",
                                 max_length=30,
                                 blank=True)
    is_staff = models.BooleanField("staff status",
                                   default=False,
                                   )
    is_active = models.BooleanField("active",
                                    default=True,
                                    )

    date_joined = models.DateTimeField("date joined",
                                       default=timezone.now)
    last_login = models.DateTimeField("last login",
                                      default=timezone.now)

    phone = models.IntegerField(blank=True,
                                null=True)
    cell_phone = models.IntegerField(blank=True,
                                     null=True)

    birth_date = models.DateField("birth date",
                                  null=True,
                                  )

    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'),
                      )
    gender = models.CharField("gender",
                              max_length=1,
                              choices=GENDER_CHOICES,
                              default='M')
    # subscribe = models.BooleanField(default=True)
    objects = SocialUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:

        verbose_name = _('user')
        verbose_name_plural = _('users')


    def __str__(self):
        return self.email

    def get_full_name(self):

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):

        return self.first_name




class BillingAddress(models.Model):

    title = models.CharField(max_length=20,
                             blank=True,
                             null=True)
    location = models.CharField(max_length=1000,
                                blank=True,
                                null=True)
    postal_code = models.IntegerField(blank=True,
                                      null=True)
    receiver_name = models.CharField(max_length=100,
                                     blank=True,
                                     null=True)

    phone = models.IntegerField(blank=True,
                                null=True)

    users = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)

    class Meta:
        order_with_respect_to = 'users'

    def __str__(self):
        return self.title


class Artist(models.Model):
    users = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 blank=True)
    brand = models.CharField(max_length=30,
                             blank=True,
                             null=True)
    bio = models.CharField(max_length=1000,
                           blank=True)
    skill = models.CharField(max_length=200,
                             blank=True)
    avatar = models.ImageField()

    def __str__(self):
        return self.brand


class ArtistImage(models.Model):
    artist_image = models.ImageField()
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE,
                               blank=True)


class Subscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    sub_email = models.EmailField("email address",
                                  max_length=254,
                                  unique=True)
    
    def __str__(self):
        return self.sub_email




