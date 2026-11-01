from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Employee(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    gender = models.CharField("Пол", max_length=10, choices=[('M', 'Мужской'), ('F', 'Женский')])
    skills = models.TextField("Навыки", blank=True) 

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class EmployeeImage(models.Model):
    employee = models.ForeignKey(Employee, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to='employees/')
    # К3: Порядковый номер
    order = models.PositiveIntegerField("Порядковый номер", default=0, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Фото {self.order} для {self.employee}"

@receiver(post_delete, sender=EmployeeImage)
def delete_employee_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)