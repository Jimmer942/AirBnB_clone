#!/usr/bin/env python3
""" Class Basemodel """
import uuid
from datetime import *


class BaseModel():
    """ Class Basemodel """

    def __init__(self, *args, **kwargs):
        """ Init """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """ Print """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """ Save """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """ Dictionary """
        my_dict = self.__dict__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
