from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField()
    delete_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()  # datetime.now()
        self.updated_at = timezone.now()
        return super(Person, self).save(*args, **kwargs)

        class Meta:
            db_table = 'person'


class Project(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100) 
    description = models.TextField()
    image = models.ImageField(upload_to='', null=True)
    url = models.URLField(null=True)
    # created_at = models.DateTimeField(auto_now_add = True, null=True)
    # updated_at = models.DateTimeField(null=True)
    # delete_at = models.DateTimeField(null=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created_at = timezone.now()  # datetime.now()
    #     self.updated_at = timezone.now()
    #     return super(Person, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"Imagen: {self.image}"

    class Meta:
        db_table = 'project'
    

