from django import forms

class NeuAddForm(forms.Form):
    neu_f_name = forms.CharField(label="First Name", max_length=100)
    neu_l_name = forms.CharField(label="Last Name", max_length=100)
    neu_id = forms.IntegerField(label="ID")
    
    location = forms.ChoiceField(label="Radio Options",choices=[("","Select a option"),("Dinajpur", "Dinajpur"),("Bogura", "Bogura"),("Rajshahi", "Rajshahi"),("Chottogram", "Chottogram"),("Sylhet", "Sylhet")])
    
    produce = forms.ChoiceField(label="Dropdown", choices=[("","Select a option"),("Potato", "Potato"),("Cucumber", "Cucumber"),("Tomato", "Tomato"),("Cabbage", "Cabbage"),("Onion", "Onion")])
    
    applicable_temperature = forms.FloatField(label="Temperature (°C)",widget=forms.NumberInput(attrs={"type": "range", "min": "-50", "max": "50", "step": "1","oninput": "updateTempValue(this.value)" }))
    applicable_humidity = forms.FloatField(label="Humidity (%)",widget=forms.NumberInput(attrs={"type": "range", "min": "0", "max": "100", "step": "1","oninput": "updateHumidityValue(this.value)"}))



class SeedRequestForm(forms.Form):
    farmer_full_name = forms.CharField(label="Farmer Full Name", max_length=100)
    farmer_id = forms.IntegerField(label="Farmer ID")
    seed_variety = forms.ChoiceField(label="Variety of Crops Seed", choices=[("","Select a option"),("Potato", "Potato"),("Cucumber", "Cucumber"),("Tomato", "Tomato"),("Cabbage", "Cabbage"),("Onion", "Onion")])
    other_seed_name = forms.CharField(label="Other Seed Name", required=False, max_length=100)



class ProductAddForm(forms.Form):
    product_name = forms.CharField(label="Product Name", max_length=100)
    price = forms.FloatField(label="Price ($ per kg)")
    quantity = forms.FloatField(label="Quantity (kg)")
    description = forms.CharField(
        label="Description", widget=forms.Textarea, required=False
    )
    required_temperature = forms.FloatField(label="Temperature (°C)")
    required_humidity = forms.FloatField(label="Humidity (%)")
    warehouse_location = forms.ChoiceField(
        label="Warehouse Location",
        choices=[("", "Select Location"), ("Dhaka", "Dhaka"), ("Bogura", "Bogura"), ("Chottogram", "Chottogram")],
    )
    available_quantity = forms.FloatField(label="Available Quantity in Warehouse (kg)")
