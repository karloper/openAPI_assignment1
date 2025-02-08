import connexion

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.service.student_service import *


def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501]
        return add(body)
    return 500,'error'


def delete_student(student_id):  # noqa: E501
    """deletes a student

    delete a single student  # noqa: E501

    :param student_id: the uid
    :type student_id: float

    :rtype: Student
    """
    try:
        result = delete(student_id)
        if result == 'not found':
            return 'Student not found', 404
        return 'Student successfully deleted', 200
    except Exception as e:
        return str(e), 500

def get_student_by_id(student_id):  # noqa: E501
    """gets student

    Returns a single student # noqa: E501

    :param student_id: the uid
    :type student_id: 

    :rtype: Student
    """
    try:
        result = get_by_id(student_id)
        if result == 'not found':
            return 'Student not found', 404
        return result, 200
    except Exception as e:
        return str(e), 500
