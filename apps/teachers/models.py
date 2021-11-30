from django.db import models
from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    exp = models.CharField(max_length=128)

    def __str__(self):
        return str(self.teacher)


@receiver(post_save, sender=User)
def create(sender, instance, created, **kwargs):
    if created and instance.is_srudent:
        Teacher.objects.create(Teacher=instance)
