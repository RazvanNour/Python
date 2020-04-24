'''
Created on 12 Nov 2018

@author: Polizei
'''

from Persoana import Persoana
from Eveniment import Eveniment
from ValidError import ValidError
from valideaza import ValideazaPersoana
from valideaza import ValideazaEveniment
from repository import Repository
from RepoError import RepoError
from Registru import Registru
from Repo_registru import Repo_registru
r=Repo_registru()
class Test(object):
    def __init__(self):
        self.__id = "19"
        self.__nume = "Razvan"
        self.__adresa = "Botosani"
        
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        
        self.__badId = "389178"
        self.__badNume = ""
        self.__badAdresa = ""
        
        self.__badPersoana = Persoana(self.__badId,self.__badNume,self.__badAdresa)
        self.__validator = ValideazaPersoana()
        
        self.__id = 1
        self.__data = [12, 11, 2018]
        self.__timp = "14:53"
        self.__descriere ="Descriere"
        
        self.__eveniment = Eveniment(self.__id,self.__data,self.__timp,self.__descriere)
        
        self.__id = 1
        self.__data = [12, 11, 2018]
        self.__timp = "14:53"
        self.__descriere ="Descriere"
        self.__eveniment = Eveniment(self.__id,self.__data,self.__timp,self.__descriere)
        
        self.__id = -3
        self.__data = [32, 13, 2070]
        self.__timp = "25:64"
        self.__descriere = ""
        self.__badEveniment = Eveniment(self.__id, self.__data, self.__timp, self.__descriere)
        self.__validatorEv = ValideazaEveniment() 
    
        self.__repo = Repository()
    
    def __testPersoana(self):
        assert self.__persoana.get_id() == "19"
        assert self.__persoana.get_nume() == "Razvan"
        assert self.__persoana.get_adresa() == "Botosani"
        
    
    
    def __testValideazaPersoana(self):
        try:
            self.__validator.valideazaPersoana(self.__persoana)
            assert True
        except ValidError:
            assert False
        
        
    
    
    def __testEveniment(self):
        assert self.__eveniment.get_id() == 1
        assert self.__eveniment.get_data() == [12, 11, 2018]
        assert self.__eveniment.get_timp() == "14:53"
        assert self.__eveniment.get_descriere() == "Descriere"
    
    
    def __testValideazaEveniment(self):
        try:
            self.__validatorEv.valideazaEveniment(self.__eveniment)
            assert True
        except ValidError:
            assert False
        
        try:
            self.__validatorEv.valideazaEveniment(self.__badEveniment)
            assert False
        except ValidError as msg:
            assert str(msg) == "id invalid!\ndata invalida!\nora invalida!\ndescriere invalida!\n"
            
    
    
    def __testAdaugaElement(self):
        assert len(self.__repo) == 0
        
        self.__id = "19"
        self.__nume = "Razvan"
        self.__adresa = "Botosani"
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        
        self.__repo.adaugaElement(self.__persoana)
        assert len(self.__repo) == 1
        
        
        
        try:
            self.__repo.adaugaElement(self.__persoana)
            assert False
        except RepoError as msg:
            assert str(msg) == "obiectul exista deja!\n"
    

    def __testStergeElement(self):
        self.__repo = Repository()
        assert len(self.__repo) == 0
        
        self.__id = 1
        self.__nume = "Razvan"
        self.__adresa = "Botosani"
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        
        self.__repo.adaugaElement(self.__persoana)
        
        self.__id = 2
        self.__nume = "Cristian"
        self.__adresa = "Botosani"
        self.__persoana1 = Persoana(self.__id,self.__nume,self.__adresa)
        
        self.__repo.adaugaElement(self.__persoana1)
        assert len(self.__repo) == 2
        
        try:
            self.__repo.stergereElement(self.__persoana1)
            assert True
        except RepoError:
            assert False
        
        try:
            self.__repo.stergereElement(self.__persoana1)
            assert False
        except RepoError as msg:
            assert str(msg) == "obiectul nu exista!\n"
        
        try:
            self.__repo.stergereElement(self.__persoana)
            assert True
        except RepoError:
            assert False
        
        try:
            self.__repo.stergereElement(self.__persoana)
            assert False
        except RepoError as msg:
            assert str(msg) == "obiectul nu exista!\n"
        
    
    def __testCautaPersoana(self):
        self.__id = 1
        self.__nume = "Razvan"
        self.__adresa = "Botosani"
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        
        
        try:
            self.__repo.cautarePersoana(self.__persoana)
            assert False
        except RepoError as msg:
            assert str(msg) == "persoana nu exista!\n"
        
        self.__repo.adaugaElement(self.__persoana)
        try:
            self.__repo.cautarePersoana(self.__persoana)
            assert True
        except RepoError:
            assert False
            
            
    def __testCautaEveniment(self):
        self.__repo = Repository()
        try:
            self.__repo.cautareEveniment(self.__eveniment)
            assert False
        except RepoError as msg:
            assert str(msg) == "evenimentul nu exista!\n"
        
        self.__repo.adaugaElement(self.__eveniment)
        try:
            self.__repo.cautareEveniment(self.__eveniment)
            assert True
        except RepoError:
            assert False

    
    

    
    
    def __testModificaElement(self):
        self.__repo = Repository()
        assert len(self.__repo) == 0
        
        self.__id = 1
        self.__nume = "Razvan"
        self.__adresa = "Botosani"
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        
        self.__repo.adaugaElement(self.__persoana)
        
        self.__adresa = "Cluj-Napoca"
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        self.__repo.modificaElement(self.__persoana)
        
        assert self.__persoana.get_adresa() == self.__repo.cautarePersoana(self.__persoana).get_adresa()
        
    def __testInscriePersoana(self):
        self.__repoRegistru=Repo_registru()
        assert len(self.__repoRegistru)==0
        
        self.__id = 1
        self.__nume = "Razvan"
        self.__adresa = "Botosani"
        self.__persoana = Persoana(self.__id,self.__nume,self.__adresa)
        
        self.__id = 1
        self.__data = [12, 11, 2018]
        self.__timp = "14:53"
        self.__descriere ="Descriere"
        self.__eveniment = Eveniment(self.__id,self.__data,self.__timp,self.__descriere)
        
        registru=Registru(self.__persoana,self.__eveniment)
        self.__repoRegistru.adaugaElement(registru)
        assert self.__persoana==self.__repoRegistru.cautarePersoana(registru).get_persoana()
    
    def ruleazaTeste(self):
        '''Persoana si validarea datelor'''
        self.__testPersoana()
        self.__testValideazaPersoana()
        
        '''Eveniment si validarea datelor'''
        self.__testEveniment()
        self.__testValideazaEveniment()
        
        '''Repository tests'''
        self.__testAdaugaElement()
        self.__testModificaElement()
        self.__testStergeElement()
        self.__testCautaPersoana()
        self.__testCautaEveniment()
        self.__testInscriePersoana()
        
        
        
    
