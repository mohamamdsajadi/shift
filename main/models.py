import jdatetime
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django_jalali.db import models as jmodels


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('The phone_number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_confirmed', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=13, blank=True, unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    profile_picture = models.ImageField(upload_to='users/profiles/', default='users/default_profile.png')
    id_card = models.ImageField(upload_to='users/profiles/')
    degree = models.ImageField(upload_to='users/degrees/')
    auth = models.ImageField(upload_to='users/auths/')

    is_confirmed = models.BooleanField(default=False)

    objects = UserManager()

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at', ]


class BankInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sheba = models.CharField(max_length=100)


class Code(models.Model):
    code = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=11)


class Shift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = jmodels.jDateField()
    string_date = models.CharField(max_length=11)
    sobh = models.BooleanField(null=True, default=False)
    asr = models.BooleanField(null=True, default=False)
    shab = models.BooleanField(null=True, default=False)


class RequestEdit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = jmodels.jDateField()
    string_date = models.CharField(max_length=11)
    new_sobh = models.BooleanField(null=True, default=False)
    new_asr = models.BooleanField(null=True, default=False)
    new_shab = models.BooleanField(null=True, default=False)
    is_approved = models.BooleanField(default=False)
    request_date = jmodels.jDateField(auto_now=True)


class ControlShift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField()
    month = models.IntegerField()
    user_change_time = models.IntegerField(default=0)
    limit = models.IntegerField(default=3)


class Discount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.FloatField()
    month = models.IntegerField()
    year = models.IntegerField()
    submit_date = models.CharField(default=jdatetime.datetime.now().strftime("%Y-%m-%d")  , max_length=10)
