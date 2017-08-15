from django.db import models
from users.models import User, Artist
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(max_length=100, null=True)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               related_name='child')
    cat_slug = models.SlugField(allow_unicode=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', 'id', related_name="product_price")
    price = models.FloatField()
    status = models.IntegerField()
    date = models.DateTimeField()


class ProductOption(models.Model):
    id = models.AutoField(primary_key=True)
    option = models.ManyToManyField('Option')
    value = models.CharField(max_length=50)
    product = models.ForeignKey('Product', 'id')

    def __str__(self):
        return self.value


class ProductPriceOption(models.Model):
    id = models.AutoField(primary_key=True)
    product_color = models.OneToOneField('ProductColor', on_delete=models.CASCADE, default='0')
    price_diff = models.IntegerField(blank=True, default=0, null=True)


class CategoryOption(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Category', 'id')
    value = models.CharField(max_length=50)
    option = models.ManyToManyField('Option')

    def __str__(self):
        return self.value


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    types = models.IntegerField(choices=())

    def __str__(self):
        return self.title


class ProductQuantity(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    product_color = models.OneToOneField('ProductColor', on_delete=models.CASCADE, default='0')


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 null=True)
    name = models.CharField(max_length=100)
    description_short = models.CharField(max_length=200,
                                         null=True)
    description = models.TextField(null=True)
    add_date = models.DateField(null=True,
                                default=timezone.now)
    active = models.BooleanField(default=1)
    caziwa_suggest = models.BooleanField(default=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('B', 'Both')
    )
    gender = models.CharField(
        "gender",
        max_length=1,
        choices=GENDER_CHOICES,
        default='B'
    )
    pic = models.ForeignKey('Image', 'id', related_name='pic', null=True, blank=True)
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    main_image = models.ImageField(null=True, )

    similars = models.ManyToManyField('Product', blank=True)


    def __str__(self):
        return self.name

    def admin_thumbnail(self):
        return u'<img src="%s" style="width:50px; height:50px;"/>' % (self.main_image.url)

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(null=True)

    class Meta:
        db_table = 'product_images'


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    users = models.ForeignKey(settings.AUTH_USER_MODEL)
    cm_text = models.CharField(max_length=100, blank=False)
    likes = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cm_text




class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey('Size', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_size.size


class ProductColor(models.Model):
    product_size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    product_color = models.ForeignKey('Color', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_color.color_name


class Color(models.Model):
    color_name = models.CharField(blank=True, max_length=50)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.color_name


class Size(models.Model):
    size = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.size


class CatImage(models.Model):
    banner_one = models.ImageField(upload_to='', blank=True)
    banner_two = models.ImageField(upload_to='', blank=True)
    banner_three = models.ImageField(upload_to='', blank=True)
    banner_four = models.ImageField(upload_to='', blank=True)
    banner_five = models.ImageField(upload_to='', blank=True)
    banner_six = models.ImageField(upload_to='', blank=True)
    banner_seven = models.ImageField(upload_to='', blank=True)
    banner_eight = models.ImageField(upload_to='', blank=True)
    banner_nine = models.ImageField(upload_to='', blank=True)
    banner_ten = models.ImageField(upload_to='', blank=True)
    subcategory = models.ForeignKey('Category', on_delete=models.CASCADE)


class CatSlider(models.Model):
    slider_image = models.ImageField(upload_to='', blank=True)
    subcategory = models.ForeignKey('Category', on_delete=models.CASCADE)
