from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Attribute(models.Model):
        txn_id=models.IntegerField()
        Document_Name=models.CharField(max_length=300)
        Agreement_Title=models.CharField(max_length=300)
        Party1_Name = models.CharField(max_length=300)
        Party2_Name = models.CharField(max_length=300)
        Term=models.CharField(max_length=300)
        Assignment_Clause=models.CharField(max_length=300)
        Governing_Law= models.CharField(max_length=300)
        Effective_date=models.CharField(max_length=300)
        Return_of_material=models.CharField(max_length=300)


        def __str__(self):
            return str(self.txn_id)
