from django.contrib import admin
from django.utils.html import format_html
from django import forms

from .models import Contact, Portfolio, Phonenumber


# admin.site.register(Contact)
# admin.site.register(Portfolio)

class PhonenumberAdmin(admin.ModelAdmin):
    list_display = ('admin_name', 'phone_number')
    list_filter = ('admin_name',)


admin.site.register(Phonenumber, PhonenumberAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'message', 'is_solved', 'created_at')
    list_filter = ('is_solved',)


admin.site.register(Contact, ContactAdmin)


class PortfolioAdminForm(forms.ModelForm):
    positioning_choices = [
        ('left_top', 'Left Top'),
        ('right_top', 'Right Top'),
        ('top', 'Top')
    ]

    positioning = forms.ChoiceField(choices=positioning_choices, required=False)

    class Meta:
        model = Portfolio
        fields = '__all__'


class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioAdminForm
    list_display = ('id', 'image', 'preview', 'positioning', 'is_active', 'created_at')
    list_filter = ('is_active',)

    list_editable = ('is_active',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60" style="position: {obj.positioning}; top: 0; left: 0; right: 0;">"""

        return format_html(html_code)


admin.site.register(Portfolio, PortfolioAdmin)

# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'preview', 'is_active', 'created_at')
#     list_filter = ('is_active',)
#
#     list_editable = ('is_active',)
#
#     def preview(self, obj):
#         html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""
#
#         return format_html(html_code)
#
#
# admin.site.register(Portfolio, PortfolioAdmin)
