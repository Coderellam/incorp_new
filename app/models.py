from django.db import models


service_type = [('ux-ui', 'ux-ui'),
                ('web-development', 'web-development'),
                ('internet-platform', 'internet-platform'), ('mobile-development', 'mobile-development')
                ]


class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=20)

    message = models.TextField()
    is_solved = models.BooleanField(default=False)

    service = models.CharField(max_length=100, unique=True, choices=service_type)

    web_development = models.BooleanField(default=False)
    ux_ui = models.BooleanField(default=False)
    internet_platform = models.BooleanField(default=False)
    mobile_development = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
