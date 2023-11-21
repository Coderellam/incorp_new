from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=20)

    message = models.TextField()
    is_solved = models.BooleanField(default=False)

    web_development = models.BooleanField(default=False)
    ux_ui = models.BooleanField(default=False)
    internet_platform = models.BooleanField(default=False)
    mobile_development = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    positioning = models.CharField(max_length=20,
                                   choices=[('left_top', 'Left Top'), ('right_top', 'Right Top'), ('top', 'Top')],
                                   blank=True, null=True)

    def __str__(self):
        return f'name: {self.name}'


class Phonenumber(models.Model):
    admin_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
