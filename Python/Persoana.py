'''
Created on 12 Nov 2018

@author: Polizei
'''
class Persoana(object):
    
    
    def __init__(self, __id, __nume, __adresa):
        self.__id = __id
        self.__nume = __nume
        self.__adresa = __adresa

    def get_id(self):
        return self.__id


    def get_nume(self):
        return self.__nume


    def get_adresa(self):
        return self.__adresa


    def set_id(self, value):
        self.__id = value


    def set_nume(self, value):
        self.__nume = value


    def set_adresa(self, value):
        self.__adresa = value
    
        
        
    
    def __eq__(self,persoana):
        return (self.__id == persoana.get_id() or(self.__nume == persoana.get_nume() and self.__adresa == persoana.get_adresa()))
    
    def __str__(self):
        return str("ID:" + str(self.__id) + " Nume:" + self.__nume + " Adresa:" + self.__adresa )
    id = property(get_id, set_id, None, None)
    nume = property(get_nume, set_nume, None, None)
    adresa = property(get_adresa, set_adresa, None, None)
    
    



