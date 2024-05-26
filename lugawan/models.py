from django.db import models

# Create your models here.


    
class branch(models.Model):
    
    branch = models.CharField(max_length=100)
    branch_address = models.CharField(max_length=250)
   

    def __str__(self):
        return self.branch


class Product(models.Model):
    
    branch = models.ForeignKey(branch,null=True, on_delete=models.SET_NULL)
    product = models.CharField(max_length=250)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=150)
   

    def __str__(self):
        return self.product
    

class transaction(models.Model):
    
    transdate= models.DateTimeField(auto_now_add=True, null=True)
    branch = models.OneToOneField(branch,null=True, on_delete=models.SET_NULL)
    item = models.OneToOneField(Product,null=True, on_delete=models.SET_NULL)
    price = models.FloatField(null=True)
    units = models.IntegerField(null=False)
    total=models.FloatField(null=True)

   

    def __str__(self):
        return self.product
    

class halin(models.Model):
    branch = models.CharField(max_length=150)
    transdate= models.DateTimeField(null=True)
    item = models.CharField(max_length=150)
    price = models.FloatField(null=True)
    
    
    def __str__(self):
         return f'{self.item} - {self.transdate}'
    
class expense(models.Model):
    branch = models.CharField(max_length=150)
    transdate= models.DateTimeField(null=True)
    
    categorys = (
    ("CONSUMABLE", "Consumable"),
    ("STOCKS", "Stocks"),    
    ("OPERATING", "Operating"),    
    )
    category = models.CharField(max_length=150,
                  choices=categorys,
                  default="Consumable")



    expenses = (
    ("EGG", "Egg"),
    ("WATER", "Water"),
    ("ICE", "Ice"),
    ("OIL", "Oil"),
    ("GAS", "Gas"),    
    ("ELECTRICITY", "Electricity"),
    ("RENT", "Rent"),
    ("INGREDIENTS", "Ingredients"),
    ("SOFTDRINKS", "Softdrinks"),
    ("SALARY", "Salary"),
    ("OTHERS", "Others"),    
    )
    expense = models.CharField(max_length=150,
                  choices=expenses,
                  default="WATER")

  
    Qty = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price = models.FloatField(null=True)
    notes = models.CharField(max_length=150)
    
    
    def __str__(self):
         return f'{self.expense} - {self.transdate}'