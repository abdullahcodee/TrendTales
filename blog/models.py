from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def fullname(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def __str__(self):
        return self.fullname()



class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    slug = models.SlugField(unique= True, default="", null=False, db_index= True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="posts")
    date = models.DateField(null= True, auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    excerpt = models.CharField(max_length= 200, null= True)
    author = models.ForeignKey(Author,null= True, on_delete=models.SET_NULL, related_name= "posts")
    tags = models.ManyToManyField(Tag )

    def __str__(self):
        return f"{self.slug} on {self.date} - {self.author}"



class Comment(models.Model):
    username= models.CharField(max_length= 120)
    user_email = models.EmailField()
    text = models.TextField(max_length= 300)
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= "comments")

    def __STR__(self):
        return f"{self.username} / {self.text}"

