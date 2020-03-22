# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 01:29:51 2020

@author: Crazelu
"""
from DequeArgumentError import DequeArgumentError

class deque():
    
    empty_list = []
    
    def __init__(self, *list_):
        if list_ is None:
            self.list_ = self.empty_list
        else:
            self.list_ = list(list_)
        
        global acc
        
        self.acc = self.empty_list
    
    def insert_front(self, element, *args):
        
        ''' Method inserts element at the beginning of deque'''
        
        if bool(args):
            raise DequeArgumentError('insert_front()', 1, len(args))
            
        else:
            self.out = self.empty_list + [element]
            for i in self.list_:
                self.out +=  [i]
            
            self.acc += self.out
            self.list_ = self.out
            return self.out
            

    
    def insert_rear(self, element, *args):
        
        ''' Method inserts element at the end of deque'''
        
        if bool(args):
            raise DequeArgumentError('insert_rear()', 1, len(args))
            
        else:
            self.out = self.list_ + [element]
            self.acc += self.out
            self.list_ = self.out
            return self.out
            
    
    def insert(self, index, element, *args):
        
        ''' Method inserts element at the specified index position in deque'''
        if bool(args):
            raise DequeArgumentError('insert()', 2, len(args)+1)
            
        else:
            self.pre_index_copy = self.list_[:index]
            self.post_index_copy = self.list_[index:]
            self.out = []
            
            for i in self.pre_index_copy:
                self.out +=  [i]
            self.out = self.out + [element]
            for i in self.post_index_copy:
                self.out += [i]
                
            self.acc += self.out
            self.list_ = self.out
            return self.out
    
    def get_all(self):
        ''' Method returns all the elements of deque'''
        return self.out
    
    def clear(self):
        '''Method returns an empty instance of the deque class'''
        self.out = []
        return self.out
    
