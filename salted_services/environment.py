"""
Ryan Long
2018-06-25
environment.py
"""
import os


class EnvironmentMixin:
    """
    This Module is responsible for helping in
    environment variable getting and setting.
    """

    @staticmethod
    def get_environ_variable_value(name):
        """
        Gets an environment variable by name.

        :param name: the variable to fetch
        :return: string
        """
        try:
            return os.environ[name]
        except KeyError:
            raise EnvironmentVariableNotFoundError("Could not find environement variable {}".format(name))

    @staticmethod
    def set_environ_variable_value(name, value):
        """
        Sets an environment variables value.  It is
        created if it does not already exist.

        :param name:
        :param value:
        :return:
        """
        os.environ[name] = str(value)
        return True


class EnvironmentVariableNotFoundError(Exception):
    """
    Exception raised for environment variables that are not defined.

    Attributes:
        message = the message containing what variable could not be found
    """

    def __init__(self, message):
        self.message = message
