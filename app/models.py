from django.db import models


class Inno_razrabotki1(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Inno_razrabotki2(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Inno_razrabotki3(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Web(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Mobile(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Uxui(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Expertiza473(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


""" 507 """


class Innopodxod(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


"""540"""


class Expertiza(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


"""574"""


class Individual(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Technical(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title


class Gibkost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(upload_to='images/')


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

    def __str__(self):
        return f'name: {self.name}'


class Phonenumber(models.Model):
    admin_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
