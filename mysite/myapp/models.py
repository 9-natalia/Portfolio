from django.db import models

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
