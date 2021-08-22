#!/usr/bin/python3
"""
defines class Student
"""


class Student:
    """Define the variable or attribute in the principal method"""
    def __init__(self, first_name, last_name, age):
        """initializes attributes
        Args:
            first_name (string): student's first name
            last_name (string): student's last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        Returns:
            converted class to dictionary
        """
        return self.__dict__
