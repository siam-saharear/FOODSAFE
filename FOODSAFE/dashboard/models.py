from django.db import models

# Create your models here.


class NeutritionProfile(models.Model):
    
    neu_f_name = models.CharField(max_length=100, verbose_name="First Name")
    neu_l_name = models.CharField(max_length=100, verbose_name="Last Name")
    neu_id = models.IntegerField(unique=True, verbose_name="ID")  
    LOCATION_CHOICES = [
        ('Dinajpur', 'Dinajpur'),
        ('Bogura', 'Bogura'),
        ('Rajshahi', 'Rajshahi'),
        ('Chottogram', 'Chottogram'),
        ('Sylhet', 'Sylhet'),
    ]
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='Dinajpur', verbose_name="Location")

    FOOD_CHOICES = [
        ('Potato', 'Potato'),
        ('Cucumber', 'Cucumber'),
        ('Tomato', 'Tomato'),
        ('Cabbage', 'Cabbage'),
        ('Onion', 'Onion'),
    ]
    produce = models.CharField(max_length=20, choices=FOOD_CHOICES, default='Potato', verbose_name="Food Selection")

    applicable_temperature = models.FloatField(default=10.0, verbose_name="Temperature (°C)")

    applicable_humidity = models.FloatField(default=50.0, verbose_name="Humidity (%)")

    def __str__(self):
        return f"{self.neu_f_name} {self.neu_l_name} ({self.neu_id})"
    
    
    
    
class SeedRequest(models.Model):
    farmer_full_name = models.CharField(max_length=100)
    farmer_id = models.IntegerField()
    seed_variety = models.CharField(max_length=100)
    other_seed_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.farmer_full_name} - {self.seed_variety}"
    
    
    
    
class Seller(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_id = models.IntegerField(unique=True)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.seller_name} ({self.seller_id})"


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="products")
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.FloatField()  
    description = models.TextField(blank=True)
    required_temperature = models.FloatField()
    required_humidity = models.FloatField()  
    warehouse_location = models.CharField(
        max_length=50,
        choices=[("Dhaka", "Dhaka"), ("Bogura", "Bogura"), ("Chottogram", "Chottogram")],
    )
    available_quantity = models.FloatField()  

    def __str__(self):
        return f"{self.product_name} ({self.seller.seller_name})"
    
