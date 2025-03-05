from django.db import models


class List(models.Model):
    number = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.number
    

class Category(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    course_no = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Course(models.Model):
    image = models.FileField(upload_to="course/")
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    star_image = models.FileField(upload_to="course/")
    rating = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Instructor(models.Model):
    image = models.FileField(upload_to="instructor/")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    star = models.FileField(upload_to="instructor/")
    rate = models.CharField(max_length=255)
    count = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    icon = models.FileField(upload_to="testimonial/")
    description = models.CharField(max_length=255)
    image = models.FileField(upload_to="testimonial/")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Reviews(models.Model):
    image = models.FileField(upload_to="review/")
    name = models.CharField(max_length=255)
    star = models.FileField(upload_to="review/")
    rating = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.name
    

class Design(models.Model):
    image = models.FileField(upload_to="design/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)
