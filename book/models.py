from django.db import models

# Create your models here.

class BookCategory(models.Model):
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Book(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(default= "", null= False,blank=True, db_index= True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail = models.ImageField()
    publication_name = models.CharField(max_length=250)
    file = models.FileField(upload_to='uploads/')
    edition = models.CharField(max_length=100)
    discount_flag = models.BooleanField(default=False)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_free = models.BooleanField(default=False)
    preview = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.category} - {self.updated_date}"

