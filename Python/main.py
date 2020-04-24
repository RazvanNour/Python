'''
Created on 6 Nov 2018

@author: Polizei
'''

      

from test import Test
from Repo_registru import Repo_registru
from console import Console
from repository import Repository
from service import ServiceOrganizareEvenimente
from valideaza import ValideazaPersoana, ValideazaEveniment


t = Test()
t.ruleazaTeste()
repoPers = Repository()
repoEvent = Repository()
valideazaPers = ValideazaPersoana()
valideazaEvent = ValideazaEveniment()
repoReg = Repo_registru()
service = ServiceOrganizareEvenimente(repoPers,repoEvent,valideazaPers,valideazaEvent,repoReg)
ui = Console(service)
ui.run()
