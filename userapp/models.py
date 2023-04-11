from django.db import models

# Create your models here.

class Message(models.Model):
    names=models.CharField("Enter your name",max_length=100)
    email=models.EmailField("Enter your email")
    phone=models.IntegerField("Enter your phone number")
    message=models.TextField("Enter your message")


class Userfeedback(models.Model):
    names=models.CharField("Enter your names", max_length=100)
    email=models.EmailField("Enter your email",max_length=100)
    phone=models.IntegerField("Enter your phone number",max_length=100)
    message=models.TextField("Enter your feedback message")
    def __str__(self):
        return self.names
class Sendmailmsg(models.Model):
    names=models.CharField("Enter crypto eg bitcoin", max_length=100)
    email=models.EmailField("Enter your email",max_length=100)
    def __str__(self):
        return self.names