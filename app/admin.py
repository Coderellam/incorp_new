from django.contrib import admin
from django.utils.html import format_html
from django import forms

from .models import Contact, Portfolio, Phonenumber, Web, Mobile, Uxui, Expertiza, \
    Individual, Innopodxod, Technical, Gibkost, Inno_razrabotki1, Inno_razrabotki2, Inno_razrabotki3, Expertiza473


# admin.site.register(Contact)
# admin.site.register(Portfolio)
class WebAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Web, WebAdmin)


class MobileAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Mobile, MobileAdmin)


class UxuiAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Uxui, UxuiAdmin)


class ExpertizaAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Expertiza, ExpertizaAdmin)


class InnopodxodAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Innopodxod, InnopodxodAdmin)


class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Technical, TechnicalAdmin)


class GibkostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Gibkost, GibkostAdmin)


class IndividualAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Individual, IndividualAdmin)


class Inno_razrabotki1Admin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Inno_razrabotki1, Inno_razrabotki1Admin)


class Inno_razrabotki2Admin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Inno_razrabotki2, Inno_razrabotki2Admin)


class Inno_razrabotki3Admin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Inno_razrabotki3, Inno_razrabotki3Admin)


class Ekspertiza473Admin(admin.ModelAdmin):
    list_display = ('title', 'image', 'preview')
    list_filter = ('title',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Expertiza473, Ekspertiza473Admin)


class PhonenumberAdmin(admin.ModelAdmin):
    list_display = ('admin_name', 'phone_number')
    list_filter = ('admin_name',)


admin.site.register(Phonenumber, PhonenumberAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'message', 'is_solved', 'created_at')
    list_filter = ('is_solved',)


admin.site.register(Contact, ContactAdmin)


# class PortfolioAdminForm(forms.ModelForm):
#     # positioning_choices = [
#     #     ('left_top', 'Left Top'),
#     #     ('right_top', 'Right Top'),
#     ('top', 'Top')
# ]
#
# positioning = forms.ChoiceField(choices=positioning_choices, required=False)

# class Meta:
#     model = Portfolio
#     fields = '__all__'

#
# class PortfolioAdmin(admin.ModelAdmin):
#     # form = PortfolioAdminForm
#     list_display = ('id', 'image', 'preview', 'positioning', 'is_active', 'created_at')
#     list_filter = ('is_active',)
#
#     list_editable = ('is_active',)
#
#     def preview(self, obj):
#         html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60" style="position: {obj.positioning}; top: 0; left: 0; right: 0;">"""
#
#         return format_html(html_code)
#
#
# admin.site.register(Portfolio, PortfolioAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'preview', 'is_active', 'created_at')
    list_filter = ('is_active',)

    list_editable = ('is_active',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Portfolio, PortfolioAdmin)
