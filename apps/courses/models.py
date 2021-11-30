from django.db import models
from apps.students.models import Student
from apps.teachers.models import Teacher


class Course(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True, null=True,
        db_index=True
    )
    description = models.TextField(
        blank=True, null=True,
    )
    background_image = models.ImageField(
        upload_to='image', blank=True, null=True,
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} -- {self.title}"
