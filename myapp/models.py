from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username