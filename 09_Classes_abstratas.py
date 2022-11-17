from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Controle_tv(Controle_remoto):
    def ligar(self):
        print("Ligando a tv...")
        print("Ligado!")

    def desligar(self):
        print("desligando a tv...")
        print("desligado!")


class Controle_arcondicionado(Controle_remoto):
    def ligar(self):
        print("Ligando o ar condicionado...")
        print("Ligado!")


   
    def desligar(self):
        print("Desligando o ar condicionado!...")
        print("Desligado!")


controle = Controle_tv()
controle.ligar()
controle.desligar()


controle1 = Controle_arcondicionado()
controle1.ligar
controle1.desligar