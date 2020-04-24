'''
Created on 12 Nov 2018

@author: Polizei
'''

class Eveniment(object):
    
    
    def __init__(self, __id, __data, __timp, __descriere):
        self.__id = __id
        self.__data = __data
        self.__timp = __timp
        self.__descriere = __descriere

    def get_id(self):
        return self.__id


    def get_data(self):
        return self.__data


    def get_timp(self):
        return self.__timp


    def get_descriere(self):
        return self.__descriere


    def set_id(self, value):
        self.__id = value


    def set_data(self, value):
        self.__data = value


    def set_timp(self, value):
        self.__timp = value


    def set_descriere(self, value):
        self.__descriere = value
        
    def __eq__(self,ev):
        return self.__id == ev.get_id() or(self.__data == ev.get_data() and self.__timp == ev.get_timp() and self.__descriere == ev.get_descriere())
    
    def __str__(self):
        return str("ID:" + str(self.__id) + " Data:" + str(self.__data) + " Ora:" + self.__timp + " Descriere:" + self.__descriere)
    id = property(get_id, set_id, None, None)
    data = property(get_data, set_data, None, None)
    timp = property(get_timp, set_timp, None, None)
    descriere = property(get_descriere, set_descriere, None, None)
    
    
