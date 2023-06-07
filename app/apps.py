"""
Module containing Django applications.

This module contains the definitions of Django applications used in the project.
"""
from django.apps import AppConfig as Config


class AppConfig(Config):
    """
    Application configuration.

    This class defines the configuration for the application,
    including its name and various parameters.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
