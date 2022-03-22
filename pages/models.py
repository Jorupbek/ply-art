from django.db import models


class Slider(models.Model):
    title = models.CharField('Заголовок слайда', max_length=300)
    description = models.TextField('Описание на слайде')
    link = models.CharField('Ссылка на продук', max_length=300, default='#')
    background = models.ImageField('Задний фон', upload_to='slides')
    is_active = models.BooleanField('Включить/Выключить', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Contacts(models.Model):
    phone_number = models.CharField('Номер телефона', max_length=255)
    phone_number2 = models.CharField('Номер телефона (Не обязательно)', max_length=255, null=True, blank=True)
    email = models.CharField('Электронная почта', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    work_from = models.CharField('Часы работы с', max_length=255)
    work_to = models.CharField('Часы работы по', max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
