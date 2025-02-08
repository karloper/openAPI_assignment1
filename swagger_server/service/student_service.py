from swagger_server.persistence.student_dao import StudentDAO

student_dao = StudentDAO()

def add(student=None):
    return student_dao.add(student)

def get_by_id(student_id=None):
    return student_dao.get_by_id(student_id)


def delete(student_id=None):
    return student_dao.delete(student_id)
