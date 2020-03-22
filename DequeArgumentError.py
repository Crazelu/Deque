# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:28:07 2020

@author: Crazelu
"""
class DequeArgumentError(Exception):
    def __init__(self, method, required_args, passed_args):
        self.required_args = required_args
        self.passed_args = passed_args
        self.method = method
    
    def __str__(self):
        return '{} takes {} positional argument but {} were passed'.format(self.method, self.required_args, self.passed_args+1)
    