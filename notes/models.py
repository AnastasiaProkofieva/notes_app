from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.title}"

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    reminder = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return f"{self.title} {self.text}"


