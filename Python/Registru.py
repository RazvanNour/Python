class Registru(object):
    
    
    def __init__(self, __persoana, __eveniment):
        self.__persoana = __persoana
        self.__eveniment = __eveniment

    def get_persoana(self):
        return self.__persoana


    def get_eveniment(self):
        return self.__eveniment


    def set_persoana(self, value):
        self.__persoana = value


    def set_eveniment(self, value):
        self.__eveniment = value
    
    def __eq__(self, reg):
        return reg.get_persoana()==self.__persoana and reg.get_eveniment()==self.__eveniment
    
    def __str__(self):
        return str(self.__persoana.get_nume() + " " + str(self.__eveniment.get_id()))
    persoana = property(get_persoana, set_persoana, None, None)
    eveniment = property(get_eveniment, set_eveniment, None, None)
    
    



