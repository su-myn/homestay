from django.db import models
from django.db.models import Count

class RepairForm(models.Model):
    unit_number = models.CharField(max_length=20)
    contractor = models.CharField(max_length=40)
    repair_issue = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.unit_number

class Tag(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class AdhocItemForm(models.Model):
    CATEGORY = (
                ("Not Chosen", "Not Chosen"),
                ("Todo", "Todo"),
                ("Personal Growth", "Personal Growth"),
                ("Opportunity", "Opportunity"),
                ("Homestay", "Homestay"),
                ("Stock Market", "Stock Market"),
                ("Ecommerce","Ecommerce"),
    )

    tags = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True, choices=CATEGORY)
    adhoc_item = models.CharField(max_length=200, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.adhoc_item} ---- {self.category}"
