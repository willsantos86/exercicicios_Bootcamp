
#Classes filhas recebem metodos da classe mãe, porém as devolutivas são das classes filhas.

class Passaro:
    def voar(self):
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


def plano_voo(obj):
    obj.voar()


plano_voo(Pardal())
plano_voo(Avestruz())