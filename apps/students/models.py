from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=16)

    def __str__(self):
        return str(self.student)


@receiver(post_save, sender=User)
def create(sender, instance, created, **kwargs):
    if created and instance.is_srudent:
        Student.objects.create(User=instance)
