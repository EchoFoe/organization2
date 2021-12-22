from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe


class Department(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование депортамента')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Employee(models.Model):
    last_name = models.CharField(max_length=200, db_index=True, verbose_name='Фамилия сотрудника')
    first_name = models.CharField(max_length=200, verbose_name='Имя сотрудника')
    middle_name = models.CharField(max_length=200, verbose_name='Отчество сотрудника')
    photo = models.ImageField(upload_to='photo_of_staff/', blank=True, verbose_name='Фотография сотрудника')
    function_position = models.CharField(max_length=200, verbose_name='Должность сотрудника')
    salary = models.DecimalField(max_digits=8, decimal_places=1, verbose_name='Оклад сотрудника')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees',
                                   verbose_name='Департамент')
    is_active = models.BooleanField(default=True, verbose_name='Актуальность')
    created = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')

    class Meta:
        unique_together = ('last_name', 'department',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    def full_name(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)

    full_name.short_description = 'ФИО сотрудника'

    def photo_img(self):
        if self.photo:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="25"/></a>'.format(self.photo.url))
        else:
            return 'Фотографии нет'

    photo_img.short_description = 'Фотография'
    photo_img.allow_tags = True

    def get_absolute_url(self):
        return reverse('staff:employee_detail', args=[self.id])
