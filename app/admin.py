from django.contrib import admin
from django.utils.html import format_html

from .models import Contact, Portfolio


# admin.site.register(Contact)
# admin.site.register(Portfolio)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'message')
    list_filter = ('name',)


admin.site.register(Contact, ContactAdmin)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('image', 'preview')
    # list_display = ('image', 'preview')
    list_filter = ('image',)

    def preview(self, obj):
        html_code = f"""<img src={obj.image.url} alt="No image" width="80" height="60">"""

        return format_html(html_code)


admin.site.register(Portfolio, PortfolioAdmin)
