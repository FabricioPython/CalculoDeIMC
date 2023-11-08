
class Imc():
    def __init__(self, valor=0):
        self.valor = valor


    def imc(self, *, p, a):
        """Calcula o indice de massa corporal"""
        try:
            resultado = float(p) / (float(a) ** 2)
            self.valor = resultado
        except:
            self.valor = 0

    @staticmethod
    def ckeck_number(numero):
        """Verifica o resultado de input"""
        if len(numero) == 0:
            return "cod1"
        else:
            return numero.replace(" ", "")


    @staticmethod
    def fator_imc(*, n):
        """Retorna a classe do imc de acordo com um numero"""

        if n > 2.0 and n <= 18.5:
            return "Magreza"
        
        elif n == 0:
            return "Dados\ninválidos!" 
        
        elif n <= 24.9:
            return "Normal"
        
        elif n <= 29.9:
            return "Sobrepeso"
        
        elif n <= 34.9:
            return "Obesidade\nGrau 1"
        
        elif n <= 39.9:
            return "Obesidade\nGrau 2"
        
        elif n >= 40.0:
            return "Obesidade\nGrau 3"
    

""" simulado
while True:

    print(fator_imc(float(input("N :"))))


print(fator_imc(n=imc(p=75.0, a=1.67)))
print(imc(p=75, a=1.67))

teste = Imc()

print(teste.valor, teste.titulo)

teste.imc(p=75, a=1.67)

print(teste.fator_imc(n=teste.valor))

print(teste.valor, teste.titulo)
"""
