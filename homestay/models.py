from django.db import models

STATUS = (
    (0, "Pending"),
    (1, "Completed")
)

class RepairForm(models.Model):
    unit_number = models.CharField(max_length=20)
    contractor = models.CharField(max_length=40)
    email = models.EmailField()
    date = models.DateField()
    repair_issue = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=1)


    def __str__(self):
        return self.unit_number