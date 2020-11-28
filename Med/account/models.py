from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Positions(models.Model):

    positions_name = models.CharField(max_length=50, verbose_name='Наименование роли')

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.positions_name


class MyAccountManager(BaseUserManager):
    def create_user(self, username, surname_doctor, name_doctor,middlename_doctor, password=None):
        if not username:
            raise ValueError('Введите логин!')
        if not password:
            raise ValueError('Выберите пароль!')

        user = self.model(
                username=username,
                surname_doctor=surname_doctor,
                name_doctor=name_doctor,
                middlename_doctor=middlename_doctor,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, surname_doctor, name_doctor,middlename_doctor):
        user = self.create_user(
                username=username,
                password=password,
                surname_doctor=surname_doctor,
                name_doctor=name_doctor,
                middlename_doctor=middlename_doctor,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username            = models.CharField(max_length=30, unique=True, verbose_name='Логин')
    surname_doctor      = models.CharField(max_length=50, verbose_name='Фамилия врача', null=True)
    name_doctor         = models.CharField(max_length=50, verbose_name='Имя врача', null=True)
    middlename_doctor   = models.CharField(max_length=50, verbose_name='Отчество врача', null=True) 
    date_joined         = models.DateTimeField(max_length=50, verbose_name='Дата регистраци', null=True, auto_now_add=True)
    last_login          = models.DateTimeField(max_length=50, verbose_name='Дата последнего входа', null=True, auto_now=True)
    positions_doctor    = models.ForeignKey(Positions, on_delete = models.DO_NOTHING, verbose_name = 'Должность', null=True)
    diseases            = models.ManyToManyField(to='app.Disease', verbose_name="Заболевания", blank='True')
    is_staff            = models.BooleanField(verbose_name='Доктор-администратор',default = False)
    is_admin            = models.BooleanField(default = False)
    is_active           = models.BooleanField(default = True)
    is_superuser        = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    # Обязательные поля
    REQUIRED_FIELDS = ['surname_doctor', 'name_doctor', 'middlename_doctor']

    objects = MyAccountManager()

    def __str__(self):
        return self.surname_doctor + ' ' + self.name_doctor + ' ' + self.middlename_doctor  + ' : ' + self.positions_doctor.positions_name
        # return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"
    