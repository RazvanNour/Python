'''
Created on 12 Nov 2018

@author: Polizei
'''
from RepoError import RepoError
from ValidError import ValidError


class Console(object):
     
    def __init__(self, __service):
        self.__service = __service
        self.__actiunePersoane ={
                                "AdaugaP" : self.__service.addPerson,
                                "StergeP" : self.__service.deletePerson,
                                "ModificaP" : self.__service.updatePerson,
                                "CautaP" : self.__service.searchPerson,
                                "PrintP"  : self.__service.printPersoane,
                                "I" : self.__service.registerForEvent,
                                "Raport1" : self.__service.raportPersonToEvent,
                                "Raport2" : self.__service.raportMaxPersoana,
                                "Raport3" : self.__service.procenteEvent,
                                "PrintReg" : self.__service.printeazaRegistru,
                                "Chestie" : self.__service.chestie                              }
        self.__actiuneEvenimente ={
                                "AdaugaE" : self.__service.addEvent,
                                "StergeE" : self.__service.deleteEvent,
                                "ModificaE" : self.__service.updateEvent,
                                "CautaE" : self.__service.searchEvent,
                                "PrintE"  : self.__service.printEvenimente
                                }
    
    
    
    def __ui(self):
        print ("AdaugaP. Adauga o persoana noua in lista.")
        print ("AdaugaE. Adauga un eveniment nou in lista.")
        print ("StergeP. Sterge o persoana din lista.")
        print ("StergeE. Sterge un eveniment din lista.")
        print ("ModificaP. Modifica o persoana din lista.")
        print ("ModificaE. Modifica un eveniment din lista")
        print ("CautaP. Cauta persoana dupa nume si adresa")
        print ("CautaE. Cauta un eveniment dupa data si ora")
        print ("PrintE. Pentru a afisa evenimentele")
        print ("PrintP. Pentru a afisa persoanele")
        print ("I. Pentru a inscrie persoane la eveniment")
        print ("Raport1. Pentru a afisa ordonarea")
        print ("Raport2. Pentru a afla persoana cu cele mai multe prezente la evenimente")
        print ("Raport3. Pentru a printa cele mai frecventate 20% evenimente")
        print ("PrintReg. Pentru a afisa toate inscrierile")
        print ("exit. pentru a iesi din aplicatie\n")
    def run(self):
        self.__ui()
        self.__service.generarePersoane()
        self.__service.generareEveniment()
        while True:
            self.__service.loadPers()
            cmd = input("Introduceti comanda: ")
            if cmd == "exit":
                return
            else:
                try:
                    if cmd in self.__actiunePersoane:
                        self.__service.loadPers()
                        self.__actiunePersoane[cmd]()
                        self.__service.savePers()
                    elif cmd in self.__actiuneEvenimente:
                        self.__actiuneEvenimente[cmd]()
                    else: print("comanda invalida!\n")
                except ValueError as msg:
                    print(msg)
                except ValidError as msg:
                    print(msg)   
                except RepoError as msg:
                    print(msg)
