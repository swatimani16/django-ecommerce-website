from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse


#List of items that you can purchase

CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW','Sport Wear'),
    ('OW','OutWear')
)

LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    label = models.CharField(choices = LABEL_CHOICES, max_length = 1)
    slug = models.SlugField()
    description = models.TextField()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("products",kwargs = {
            'slug' : self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart",kwargs = {
            'slug' : self.slug
        })

#Shopping cart,everytime you sign in, it will fetch the order for that user(Linking between the item and the order!)
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


#To link all the order items to that order
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)



    def __str__(self):
        return self.user.username

