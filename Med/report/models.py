from django.db import models

# Create your models here.

class TypeErrors(models.Model):
    type_error                  = models.CharField(max_length=50, verbose_name='Тип ошибки')
    description_type            = models.TextField(max_length=250, verbose_name='Описание типа ошибки')

    class Meta:
        verbose_name            = "Тип ошибоки"
        verbose_name_plural     = "Типы ошибок"

    def __str__(self):
        return self.type_error


class Report(models.Model):
    type_errors                 = models.ForeignKey(TypeErrors, verbose_name='Типы ошибок', on_delete=models.DO_NOTHING)
    topic                       = models.CharField(max_length=50, verbose_name='Тема сообщения')
    problem_description         = models.TextField(max_length=5000, verbose_name='Описание проблемы')
    image                       = models.ImageField(verbose_name='Изображение', upload_to='images/', height_field=None, width_field=None, max_length=None, null=True, blank=True)

    class Meta:
        verbose_name            = "Сообщение об ошибке"
        verbose_name_plural     = "Сообщения об ошибках"

    def __str__(self):
        return self.topic