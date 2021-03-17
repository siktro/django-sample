from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=False, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    
    
    kinds = models.TextChoices('kind', 'Купить Продать Объменять')
    kind = models.CharField(max_length=10, choices=kinds.choices, blank=True)

    rubric = models.ForeignKey(
        'Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    def __str__(self):
        return f'{self.title} {self.content} {self.price}'


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
