# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.grade_record import GradeRecord  # noqa: F401,E501
from swagger_server import util


class Student(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, student_id: str=None, first_name: str=None, last_name: str=None, grade_records: List[GradeRecord]=None):  # noqa: E501
        """Student - a model defined in Swagger

        :param student_id: The student_id of this Student.  # noqa: E501
        :type student_id: str
        :param first_name: The first_name of this Student.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Student.  # noqa: E501
        :type last_name: str
        :param grade_records: The grade_records of this Student.  # noqa: E501
        :type grade_records: List[GradeRecord]
        """
        self.swagger_types = {
            'student_id': str,
            'first_name': str,
            'last_name': str,
            'grade_records': List[GradeRecord]
        }

        self.attribute_map = {
            'student_id': 'student_id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'grade_records': 'grade_records'
        }
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._grade_records = grade_records

    @classmethod
    def from_dict(cls, dikt) -> 'Student':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Student of this Student.  # noqa: E501
        :rtype: Student
        """
        return util.deserialize_model(dikt, cls)

    @property
    def student_id(self) -> str:
        """Gets the student_id of this Student.


        :return: The student_id of this Student.
        :rtype: str
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id: str):
        """Sets the student_id of this Student.


        :param student_id: The student_id of this Student.
        :type student_id: str
        """

        self._student_id = student_id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Student.


        :return: The first_name of this Student.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Student.


        :param first_name: The first_name of this Student.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Student.


        :return: The last_name of this Student.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Student.


        :param last_name: The last_name of this Student.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def grade_records(self) -> List[GradeRecord]:
        """Gets the grade_records of this Student.


        :return: The grade_records of this Student.
        :rtype: List[GradeRecord]
        """
        return self._grade_records

    @grade_records.setter
    def grade_records(self, grade_records: List[GradeRecord]):
        """Sets the grade_records of this Student.


        :param grade_records: The grade_records of this Student.
        :type grade_records: List[GradeRecord]
        """

        self._grade_records = grade_records
