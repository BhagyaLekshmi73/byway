from django.urls import  path
from web.views import index, course, all_courses, category


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("course/", course, name="course"),
    path("all_courses/", all_courses, name="all_courses"),
    path("category/", category, name="category"),
]