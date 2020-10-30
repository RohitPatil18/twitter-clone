from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager, AllUserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()
    all_objects = AllUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name

    def delete(self):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'users'
        default_permissions = ()
        permissions = (
            ('view_user', 'Can view user information.'),
            ('change_user', 'Can change user information.'),
            ('delete_user', 'Can delete user information.'),
            ('add_user', 'Can add user information.')
        )



"""
Following code can be removed if not wanted
"""
from masters.models import Gender
from locations.models import Country

class UserProfile(models.Model):
    """
    Table to store additional information about user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    birthdate = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        default_permissions = ()
    
    def __str__(self):
        return self.user.name