from django.contrib import admin
from .models import ProductPrice, Product, Category, Image, ProductQuantity, ProductOption, Option, CategoryOption,\
    ProductPriceOption, ProductColor, ProductSize, Color, Size, Comment, CatSlider, CatImage
from django.contrib.admin.options import StackedInline
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ImageInline(StackedInline):
    model = Image
    extra = 1
    max_num = 10


# class ColorInline(StackedInline):
#     model = ProductColor
#     extra = 1
#     max_num = 10


class PriceInline(StackedInline):
    model = ProductPriceOption
    extra = 1
    max_num = 10

class ProductOptionInline(StackedInline):
    model = ProductOption
    extra = 1
    max_num = 10


class ProductQuantityInline(StackedInline):
    model = ProductQuantity
    extra = 1
    max_num = 10


class CategoryOptionAdmin(StackedInline):
    model = CategoryOption
    extra = 1
    max_num = 10


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    search_fields = ('name', 'id', 'artist', )
    list_display = ('admin_thumbnail', 'name', 'id', 'artist', 'active', )
    list_display_links = ('id', 'name',)
    readonly_fields = ('admin_thumbnail',)
    fieldsets = (
            ('Main', {
                'fields': ('name', 'category', 'description_short', 'description', 'add_date', 'active',
                           'caziwa_suggest', 'gender', 'pic', 'artist', 'main_image', ),
                'classes': ('baton-tabs-init', 'baton-tab-inline-image',  'baton-tab-fs-content',),
                'description': 'This is a description text'

            }),
            # ('Image', {
            #     'fields': ('name', ),
            #     'classes': ('tab-fs-image', ),
            #     'description': 'This is another description text'
            #
            # }),
        )
#
# class SizeAdmin(admin.ModelAdmin):
#     inlines = [ColorInline, ]


class ColorAdmin(admin.ModelAdmin):
    inlines = [PriceInline, ]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('name',)}


# class LevelThreeInline(NestedStackedInline):
#     model = LevelThree
#     extra = 1
#     fk_name = 'level'
class QuantityInline(NestedStackedInline):
    model = ProductQuantity
    extra = 1
    fk_name = ''

class PriceInline(NestedStackedInline):
    model = ProductPriceOption
    extra = 1
    fk_name = ''


class ColorInline(NestedStackedInline):
    model = ProductColor
    extra = 1
    fk_name = ''
    inlines = [PriceInline, QuantityInline]


class SizeAdmin(NestedModelAdmin):
    model = ProductSize
    inlines = [ColorInline]




admin.site.register(Product, ProductAdmin )
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductPrice)
admin.site.register(ProductQuantity)
admin.site.register(ProductOption)
admin.site.register(Option)
admin.site.register(CategoryOption)
admin.site.register(ProductPriceOption)
admin.site.register(ProductColor, ColorAdmin)
admin.site.register(ProductSize, SizeAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Comment)
admin.site.register(CatSlider)
admin.site.register(CatImage)