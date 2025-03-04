from django.db import models

class CourseManager(models.Manager):

    def get_all_courses(self):
        return self.all()

    def get_course_by_id(self,id):
        return self.get(course_id=id)

    def get_course_by_name(self, name):
        return self.filter(course_name=name)

    def get_course_by_simplified_name(self, simplified_name):
        return self.filter(course_simplified_name=simplified_name)

    def create_course(self, course_id,course_name, course_simplified_name):
        return self.create(course_id=course_id,course_name=course_name,course_simplified_name=course_simplified_name)

    def delete_course(self, course_id):
        return self.delete(course_id=course_id)