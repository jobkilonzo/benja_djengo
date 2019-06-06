from django.db import models

class Products(models.Model):
    item_name           = models.CharField(max_length=20)
    price_retail        = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    price_wholesale     = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    date                = models.DateField()



    def __str__(self):
        return self.item_name
    def __unicode__(self):
        return self.item_name
