from Course.models import Course


def create_course(self, course_id, course_name, course_simplified_name):
    return Course.manager.create_course(course_id, course_name, course_simplified_name)



def get_all_courses():
    return Course.manager.get_all()

def get_course_by_id(course_id):
    return Course.manager.get_course(course_id)
def get_course_by_name(course_name):
    return Course.manager.get_course(course_name)
def get_course_by_simplified_name(course_name):
    return Course.manager.get_course(course_name, simplified_name=course_name)

def delete_course_by_id(course_id):
    return Course.manager.delete_course(course_id)