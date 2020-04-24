'''
Created on 12 Nov 2018

@author: Polizei
'''
import random 

from Eveniment import Eveniment
from Persoana import Persoana
from Registru import Registru
from RepoError import RepoError


class ServiceOrganizareEvenimente(object):
    
    
    def __init__(self, __repoPers, __repoEvent, __valideazaPers, __valideazaEvent, __repoRegistru):
        self.__repoPers = __repoPers
        self.__repoEvent = __repoEvent
        self.__valideazaPers = __valideazaPers
        self.__valideazaEvent = __valideazaEvent
        self.__repoRegistru = __repoRegistru
        self.__Filename="FisierPers"
    def __generareId(self):
        id = 0
        id += int(random.randint(0,1000))    
        return id
    
    
    def generarePersoane(self):
        lista_lit=["F", "J", "N", "E", "J", "I", "W", "D", "E"]
        lista_litere=["a","b","c","d","e", "f", "s", "a", "f", "a", "i", "n", "g", "w", "o", "e", "f", "n", "n", "g"]
        lista_nume=[]
        for i in range (12):
            l=""
            l=l+lista_lit[random.randint(0,8)]
            x=random.randint(1,10)
            for j in range (x):
                l=l+(lista_litere[random.randint(0,15)])
            lista_nume.append(l)
                
        lista_adresa = ["Botosani","Cluj","Timisoara","Bucuresti","Targu Mures","Oradea","Arad", "Sfnaoisfnes", "Dnwien", "Ingoewsnf", "Eogndis", "Rosdiias", "Ffsdofw", "Iubfsdfdsa", "Jbsdufba", "Nohfesdfus", "Opfsdnf", "Ojfkasb"]
        for x in range(5):
            id = self.__generareId()
            nume = lista_nume[random.randint(0,len(lista_nume)-1)]
            adresa = lista_adresa[random.randint(0,len(lista_adresa)-1)]
            persoana = Persoana(id,nume,adresa)
            self.__repoPers.adaugaElement(persoana)
    
    def generareEveniment(self):
        lista_data=[]
        for i in range (10):
            l=[]
            l.append(random.randint(1,31))
            l.append(random.randint(1,12))
            l.append(random.randint(2001,2020))
            lista_data.append(l)
        lista_ora=["12:45", "14:56", "20:45", "04:55", "23:30", "14:56", "13:23", "11:43", "13:39", "20:25", "23:19"]
        lista_descriere=["blana", "fain", "foarte frumos", "frumos", "elegant", "naspa", "obositor", "plictisitor", "excelent"]
        for i in range (5):
            id=self.__generareId()
            data=lista_data[random.randint(0,len(lista_data)-1)]
            ora=lista_ora[random.randint(0,len(lista_ora)-1)]
            descriere=lista_descriere[random.randint(0,len(lista_descriere)-1)]
            eveniment=Eveniment(id,data,ora,descriere)
            self.__repoEvent.adaugaElement(eveniment)
                            
    
    def savePers(self):
        self.__repoPers.savePersToFile(self.__Filename)
        
    def loadPers(self):
        self.__repoPers.loadPersFromFile(self.__Filename)
                      
    def printPersoane(self):
        if len(self.__repoPers) == 0:
            raise RepoError("lista este goala!\n")
        for pers in self.__repoPers:
            print(pers)    
            
    def printEvenimente(self):
        if len(self.__repoEvent) == 0:
            raise RepoError("lista este goala!\n") 
        for ev in self.__repoEvent:
            print(ev)
                   
    def addPerson(self):
        self.__id = int(input("Introduceti id-ul persoanei:\n>>>"))
        self.__nume = input("Introduceti numele persoanei:\n>>>")
        self.__adresa = input("Introduceti adresa persoanei:\n>>>")
        self.__persoana = Persoana(self.__id, self.__nume, self.__adresa)
        self.__valideazaPers.valideazaPersoana(self.__persoana)
        self.__repoPers.adaugaElement(self.__persoana)
         
    
    def addEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        self.__data = []
        self.__data.append(input ("Introduceti ziua evenimentului:\n>>>"))
        self.__data.append(input ("Introduceti luna evenimentului:\n>>>"))
        self.__data.append(input ("introduceti anul evenimentului:\n>>>"))
        self.__timp = input("Introduceti ora evenimentului:\n>>>")
        self.__descriere = input("Introduceti descrierea evenimentului:\n>>>")
        
        self.__eveniment = Eveniment(self.__id, self.__data, self.__timp, self.__descriere)
        self.__valideazaEvent.valideazaEveniment(self.__eveniment)
        
        self.__repoEvent.adaugaElement(self.__eveniment)
        
        
    def updatePerson(self):
        self.__id = int(input("Introduceti id-ul persoanei:\n>>>"))
        self.__nume = input("Introduceti numele persoanei:\n>>>")
        self.__adresa = input("Introduceti adresa persoanei:\n>>>")
        
        self.__persoana = Persoana(self.__id, self.__nume, self.__adresa)
        self.__valideazaPers.valideazaPersoana(self.__persoana)
        
        self.__repoPers.modificaElement(self.__persoana)
        
        
    def updateEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        self.__data = []
        self.__data.append(input ("Introduceti ziua evenimentului:\n>>>"))
        self.__data.append(input ("Introduceti luna evenimentului:\n>>>"))
        self.__data.append(input ("introduceti anul evenimentului:\n>>>"))
        self.__timp = input("Introduceti ora evenimentului:\n>>>")
        self.__descriere = input("Introduceti descrierea evenimentului(minim 3 caractere):\n>>>")
        
        self.__eveniment = Eveniment(self.__id, self.__data, self.__timp, self.__descriere)
        self.__valideazaEvent.valideazaEveniment(self.__eveniment)
        
        self.__repoEvent.modificaElement(self.__eveniment)
        
    
    def deletePerson(self):
        self.__id = int(input("Introduceti id-ul persoanei:\n>>>"))
        
        
        self.__persoana = Persoana(self.__id, None,None)
        
        self.__repoPers.stergereElement(self.__persoana)
        
    def deleteEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        
        
        self.__eveniment = Eveniment(self.__id, None,None,None)
        
        self.__repoEvent.stergereElement(self.__eveniment)
         
        
        
    def searchPerson(self):
        name = input("nume:")
        lista=self.__repoPers.cautaPersoana(name)
        
        for pers in lista:
            print(pers)
        
        
    
    def searchEvent(self):
        self.__id = int(input("Introduceti id-ul evenimentului:\n>>>"))
        self.__eveniment = Eveniment(self.__id, None,None,None)
        
        __ev = self.__repoEvent.cautareEveniment(self.__eveniment)
        print(__ev)

    def registerForEvent(self):
        idP=int(input("introduceti Id Persoana:>>"))
        idE=int(input("introduceti Id Event:>>"))
        self.__persoana = Persoana(idP,None,None)
        self.__eveniment = Eveniment(idE,None,None,None)
        
        persoana=self.__repoPers.cautarePersoana(self.__persoana)
        eveniment=self.__repoEvent.cautareEveniment(self.__eveniment)
        
        registru=Registru(persoana,eveniment)
        self.__repoRegistru.adaugaElement(registru)
        
    def raportPersonToEvent(self):
        id=int(input("introduceti Id>>"))
        self.__persoana = Persoana(id,None,None)
        persoana=self.__repoPers.cautarePersoana(self.__persoana)
        lista=self.__repoRegistru.genereaza_persoana_eveniment(persoana)
        for registru in lista:
            print (registru)
    def raportMaxPersoana(self):
        l=self.__repoRegistru.Persoane_evenimente()
        print (l)
    
    def procenteEvent(self):
        p=self.__repoRegistru.Procent_evenimente()
        b=1
        z={}
        while float(b/len(p))<=0.5:
            max=0
            q=""
            for j in p:
                if p[j]>max:
                    max=p[j] 
                    q=j 
            b+=1
            self.__e=Eveniment(int(q),None,None,None)
            eveniment=self.__repoEvent.cautareEveniment(self.__e)
            z[eveniment.get_descriere()]= max 
            p[q]=0
        print (z)
    
    def printeazaRegistru(self):
        for registru in self.__repoRegistru:
            print (registru)
        
    def chestie(self):
        self.__repoRegistru.chestie_noua(self.__repoEvent,self.__repoPers)