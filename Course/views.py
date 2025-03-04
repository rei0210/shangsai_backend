from django.http import JsonResponse
from django.shortcuts import render
from .service import get_all_courses
# Create your views here.

def get_all_courses_view(request):
    courses = get_all_courses()
    return JsonResponse(courses,safe=False)