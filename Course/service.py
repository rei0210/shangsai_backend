from Course.models import Course


def create_course(self, course_id, course_name, course_simplified_name):
    return Course.manager.create_course(course_id, course_name, course_simplified_name)



def get_all_courses():
    return list(Course.manager.get_all_courses().values('course_id', 'course_name', 'course_simplified_name'))

def get_course_by_id(course_id):
    return Course.manager.get_course_by_id(course_id)

def get_course_by_name(course_name):
    return Course.manager.get_course_by_name(course_name)

def get_course_by_simplified_name(simplified_name):
    return Course.manager.get_course_by_simplified_name(simplified_name)

def delete_course_by_id(course_id):
    return Course.manager.delete_course(course_id)