#!/usr/bin/python3
'''
    Define the class City.
'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id', ondelete='cascade'), nullable=False)
    places = relationship('Place',
                          cascade='delete', backref='cities')
