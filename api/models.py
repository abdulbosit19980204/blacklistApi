from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    birthday = models.DateField(null=True, blank=True)
    passport_number = models.CharField(max_length=100, null=True, blank=True)
    id_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name[:20]

class Phones(models.Model):
    number = models.CharField(max_length=15, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name="phones")

    def __str__(self):
        return self.number[:15]

class Cards(models.Model):
    bank = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=16, null=True)
    expiry_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name="cards")

    def __str__(self):
        return self.number[:16]

class Friends(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name="friends")

    def __str__(self):
        return self.fullname[:20]

class Workers(models.Model):
    username = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username[:20]