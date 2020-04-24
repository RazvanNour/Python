from repository import Repository
from RepoError import RepoError
from Eveniment import Eveniment

class Repo_registru():
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
    def genereaza_persoana_eveniment(self,persoana):
        l=[]
        for registru in range (len(self.__elem)):
            if persoana==self.__elem[registru].get_persoana():
                l.append(self.__elem[registru])
        if len(l)==0:
            print("Lista este goala\n")
            
        for i in range (0,len(l)-1):
            for j in range (i,len(l)):
                e1=l[i].get_eveniment()
                e2=l[j].get_eveniment()
                d1=e1.get_descriere()
                d2=e2.get_descriere()
                if d1>d2:
                    l[i],l[j]=l[j],l[i]
                    
        return l 
    
    def Persoane_evenimente(self):
        l={}
        for registru in range (len(self.__elem)):
            p1=self.__elem[registru].get_persoana()
            i=p1.get_id()
            l[i]=0
        for registru in range (len(self.__elem)):
            p1=self.__elem[registru].get_persoana()
            i=p1.get_id()
            l[i]=l[i]+1
        max=0
        m={}
        for j in l:
            if l[j]>max:
                max=l[j] 
                m={}
                m[j]=l[j]
            elif l[j]==max:
                m[j]=l[j]
        return m    
                
    def Procent_evenimente(self):
        l=[]
        p={}
        z={}
        k=0
        for registru in range (len(self.__elem)):
            e1=self.__elem[registru].get_eveniment()
            i=e1.get_id()
            if i in l:
                p[i]=p[i]+1
            else:
                l.append(i)
                k+=1
                p[i]=1
        return p
            
    def chestie_noua(self,__repoEvent,__repoPers):
        q=[]
        c=(len(__repoPers))
        v=(len(__repoEvent))
        b=(len(self.__elem))
        l=[]
        for registru in range (len(self.__elem)):
            p1=self.__elem[registru].get_persoana()
            i=p1.get_id()
            if i not in l:
                l.append(i)
        k=[]
        
        for reg in range (len(__repoPers)):
            f=[]
            i1=__repoPers[reg].get_id()
            a1=__repoPers[reg].get_adresa()
            n1=__repoPers[reg].get_nume()
            f.append(i1)
            f.append(n1)
            f.append(a1)
            if i1 not in l:
                k.append(f)
        print("Nr persoane: ")
        print(c)
        print ("Nr evenimente: ")
        print(v)
        print ("nr asignari: ")
        print(b)
        print ("persoane care nu participa: ")
        print(k)
            
        
        


