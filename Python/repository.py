'''
Created on 12 Nov 2018

@author: Polizei
'''
from RepoError import *
from Persoana import Persoana
from Eveniment import Eveniment


class Repository():
    
    
    def __init__(self):
        self.__elem = []
    
    
    
    def __len__(self):
        return len(self.__elem)
    
    def __getitem__(self,value):
        return self.__elem[value]
    
    def adaugaElement(self,elem):
        '''
        Adauga un element in lista cu elemente
        in: elem
        pre: elem - obiectul pe care vrem sa-l stocam
        raise RepoError daca obiectul deja exista
        '''
        for x in self.__elem:
            if x == elem: raise RepoError("obiectul exista deja!\n")
        
        self.__elem.append(elem)
        
    def savePersToFile(self,FisierPers):
        txt=""
        for pers in self.__elem:
            perstxt=""
            id=str(pers.get_id())
            nume=pers.get_nume()
            adresa=pers.get_adresa()
            perstxt=id+'/'+nume+'/'+adresa+'\n'
            txt+=perstxt
            
        with open(FisierPers,"w") as fh:
            fh.write(txt)     
                   
    def loadPersFromFile(self,FisierPers):
        self.__elem=[]
        with open (FisierPers) as fh:
            for line in fh:
                line=line.strip()
                attr=line.split("/")
                if len(attr)==3:
                    id=int(attr[0])
                    nume=attr[1]
                    adresa=attr[2]
                    b=Persoana(id,nume,adresa)
                    self.adaugaElement(b)

    def saveEventToFile(self,FisierEvent):
        txt=""
        for event in self.__elem:
            eventtxt=""
            id=str(event.get_id())
            data=str(event.get_data())
            ora=str(event.get_timp())
            descriere=event.get_descriere()
            eventtxt=id+'/'+data+'/'+ora+'/'+descriere+'\n'
            txt+=eventtxt
            
        with open(FisierEvent,"w") as fh:
            fh.write(txt)     
                   
    def loadEventFromFile(self,FisierEvent):
        self.__elem=[]
        with open (FisierEvent) as fh:
            for line in fh:
                line=line.strip()
                attr=line.split("/")
                if len(attr)==4:
                    id=int(attr[0])
                    data=attr[1]
                    ora=attr[2]
                    descriere=attr[3]
                    b=Eveniment(id,data,ora,descriere)
                    self.adaugaElement(b)

    
    
    def modificaElement(self,elem):
        '''
        Modifica un element deja existent cu unul nou
        in: elem
        pre: elem--obiectul pe care vrem sa-l stocam
        raise RepoError daca obiectul nu exista
        '''
        for i in range(len(self.__elem)):
            if self.__elem[i] == elem:
                self.__elem[i] = elem
                return
        
        raise RepoError("elementul nu a putut fi identificat\n!")
    def stergereElement(self,elem):
        '''
        Sterge elementul 'elem' din lista
        in: elem
        pre: elem - obiectul pe care il stergem
        '''
        for el in self.__elem:
            if el == elem:
                self.__elem.remove(el)
                return
        
        raise RepoError("obiectul nu exista!\n")
    
    def cautaPersoana(self,stri):
        
        lista=[]
        for persoana in self.__elem:
            if str(stri) in persoana.get_nume():
                lista.append(persoana)
                
        return lista
    
    def cautarePersoana(self,persoana):
        
        for pers in self.__elem:
            if pers == persoana:
                return pers
        
        raise RepoError("persoana nu exista!\n")
    
    
    
    
    
    def cautareEveniment(self,event):
        '''
        Cauta evenimentul in functie de id sau data si ora si descrierea
        in: event
        pre: event- evenimentul de tipul eveniment ce trebuie sa contina data si ora
        post: Evenimentul cautat
        raise RepoError daca evenimentul nu este gasit
        '''
        for ev in self.__elem:
            if event == ev:
                return ev
        raise RepoError("evenimentul nu exista!\n")
    
    