from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Service(models.Model):
    name = models.CharField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField(max_length=10)
    vin_code = models.CharField(max_length=17)
    client_name = models.CharField()
    photo = models.ImageField(upload_to='cars', null=True, blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    car = models.ForeignKey(to="Car",
                            on_delete=models.SET_NULL,
                            null=True, blank=True,
                            related_name='orders')

    LOAN_STATUS = (
        ('d', 'Administered'),
        ('t', 'Done'),
        ('i', 'In Progress'),
        ('c', 'Cancelled'),
    )

    status = models.CharField(verbose_name="Status", max_length=1, choices=LOAN_STATUS, default="d")
    client = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)

    def is_overdue(self):
        return self.deadline and timezone.now() > self.deadline

    def total(self):
        return sum(line.line_sum() for line in self.lines.all())

    def __str__(self):
        return f"{self.car.make} {self.car.model} ({self.date})"


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, related_name="lines")
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.IntegerField(default=1)

    def line_sum(self):
        return self.service.price * self.qty

    def service_price(self):
        return self.service.price

    def __str__(self):
        return f"{self.service} - {self.qty}"


class OrderComment(models.Model):
    order = models.ForeignKey(to="Order",
                              on_delete=models.SET_NULL,
                              null=True, blank=True,
                              related_name="comments")
    author = models.ForeignKey(to=User,
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)

    class Meta:
        ordering = ['-pk']
