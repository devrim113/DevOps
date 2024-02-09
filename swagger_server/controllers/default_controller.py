import connexion
from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util
from swagger_server.service.student_service import add, get_by_id, delete


def add_student(body=None):  # noqa: E501
    """Add a new student
    Adds an item to the system # noqa: E501
    :param body: Student item to add
    :type body: dict | bytes
    :rtype: float
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        student_id, status = add(body)
        if status == 409:
            return 'Student already exists', 409
        return student_id, 200
    return 'Invalid input', 500


def delete_student(student_id):  # noqa: E501
    """Deletes a student
    Delete a single student # noqa: E501
    :param student_id: the uid
    :type student_id: str
    :rtype: None
    """
    result = delete(student_id)
    if result == 'not found':
        return 'Student not found', 404
    return 'Student deleted', 200


def get_student_by_id(student_id):  # noqa: E501
    """Gets student
    Returns a single student # noqa: E501
    :param student_id: the uid
    :type student_id: str
    :rtype: Student
    """
    student = get_by_id(student_id)
    if student == 'not found':
        return 'Student not found', 404
    # Convert MongoDB document to Student model
    student_model = Student.from_dict(student)
    return student_model
