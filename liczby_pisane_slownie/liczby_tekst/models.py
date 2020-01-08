from django.db import models


class ChangeInput(models.Model):
    numbers = models.IntegerField()
    textOutput = models.CharField(max_length=255)

    def __str__(self):
        return self.numbers
