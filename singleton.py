"""
ProgramName: singleton.py
Author: BenLamb
Description: Creates a Singleton design-pattern in Python so that
only one instance of class can be initialized
"""


class Singleton:
    singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.singleton
