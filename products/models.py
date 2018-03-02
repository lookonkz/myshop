from django.db import models


class Kitchen(models.Model):
    category_name = models.CharField(verbose_name='название', max_length=300, blank=True)


class Category(models.Model):
    category_name = models.CharField(verbose_name='название', max_length=300, blank=True)


class KitchenGoods(models.Model):
    name = models.CharField(verbose_name='название', max_length=300, blank=True)
    photo = models.ImageField(verbose_name='фото', upload_to='', blank=True)
    description = models.TextField(verbose_name='Описание', default=None, blank=True)


class Ingredient(models.Model):
    dishes_name = models.CharField(verbose_name='название эгридиента', max_length=300, blank=True)
    quantity = models.IntegerField(verbose_name='количество', default=0, blank=True)
    unit = models.SmallIntegerField(verbose_name='единица измерения', default=0, blank=True)
    description = models.TextField(verbose_name='Описание', default=None, blank=True)
    calories = models.SmallIntegerField(verbose_name='каллории', default=0, blank=True)
    proteins = models.SmallIntegerField(verbose_name='Белки', default=0, blank=True)
    fats = models.SmallIntegerField(verbose_name='жиры', default=0, blank=True)
    carbohydrates = models.SmallIntegerField(verbose_name='углеводы', default=0, blank=True)


class Dish(models.Model):
    dishes_name = models.CharField(verbose_name='название блюда', max_length=300, blank=True)
    complexity = models.SmallIntegerField(verbose_name='сложность', default=0, blank=True)
    time = models.SmallIntegerField(verbose_name='Время', default=0, blank=True)
    calories = models.SmallIntegerField(verbose_name='каллории', default=0, blank=True)
    proteins = models.SmallIntegerField(verbose_name='Белки', default=0, blank=True)
    fats = models.SmallIntegerField(verbose_name='жиры', default=0, blank=True)
    carbohydrates = models.SmallIntegerField(verbose_name='углеводы', default=0, blank=True)
    price = models.IntegerField(verbose_name='цена за порцию', default=0,blank=True)
    photo = models.ImageField(verbose_name='фото', upload_to='', default=None, blank=True)
    recipe = models.TextField(verbose_name='рецепт', default=None, blank=True)
    kitchen = models.ForeignKey('Kitchen', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    kitchen_goods = models.ManyToManyField(KitchenGoods, verbose_name='что должно быть дома')


class Bring(models.Model):
    dish = models.ForeignKey('Dish', verbose_name='блюдо', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='фото', upload_to='', default=None, blank=True)
    ingredients = models.ManyToManyField(Ingredient, verbose_name='ингредиент')





