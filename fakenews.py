# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:26:51 2021

@author: anarayan
"""

from pydantic import BaseModel

class FakeNews(BaseModel):
    title: str
    author: str
    text: str
