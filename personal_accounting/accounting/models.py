from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True,null=True)
    receipt = models.FileField(upload_to='receipts/',blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.title