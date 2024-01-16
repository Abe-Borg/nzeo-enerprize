from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from district_management.models import SchoolDistrict


class MyAccountManager(BaseUserManager):
    def create_user(self, email, password = None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not password:
            raise ValueError("Users must have a password.")
        
        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )
        user.is_nzeo_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    account_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name = "email", max_length = 60, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20, default = 'N/A')
    company = models.CharField(max_length=20, default = 'N/A')
    date_joined = models.DateTimeField(verbose_name = 'date joined', auto_now_add = True)
    phone_number = models.CharField(max_length=20)
    is_nzeo_staff = models.BooleanField(default=False)
    is_site_staff = models.BooleanField(default=False)
    is_district_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    district_id = models.ForeignKey(SchoolDistrict, on_delete=models.CASCADE)
    school_id = models.ForeignKey('school_management.School', on_delete=models.CASCADE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'job_title', 'phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return f"Account: {self.first_name} {self.last_name}, Job Title: {self.job_title}, Company: {self.company}, Email: {self.email}, Phone: {self.phone_number}, District: {self.assigned_district}, School: {self.assigned_school}, Is NZEO staff: {self.is_nzeo_staff}, Is Site Staff: {self.is_site_staff}, Is District Staff: {self.is_district_staff}, Is Superuser: {self.is_superuser}, Is Active: {self.is_active}"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return True