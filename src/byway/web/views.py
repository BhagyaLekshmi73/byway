from django.shortcuts import render
from web.models import List, Category, Course, Instructor, Testimonial, Reviews, Design


def index(request):
    lists = List.objects.all()
    categories = Category.objects.all()
    courses = Course.objects.all()[:4]
    instructors = Instructor.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        "lists": lists,
        "categories": categories,
        "courses": courses,
        "instructors": instructors, 
        "testimonials": testimonials, 
    }

    return render(request, "index.html", context=context)

def course(request):
    reviews = Reviews.objects.all()
    testimonials = Testimonial.objects.all()
    courses = Course.objects.all()[:4]
    designs = Design.objects.all()

    context = {
        "reviews": reviews,  
        "testimonials": testimonials, 
        "courses": courses,
        "designs": designs, 
    }

    return render(request, "course.html", context=context)

def all_courses(request):
    courses = Course.objects.all()

    context = {
        "courses": courses,
    }

    return render(request, "all_courses.html", context=context)

def category(request):
    courses = Course.objects.all()
    
    context = {
        "courses": courses,
    }
    
    return render(request, "category.html", context=context)
