class CalculaImc():
    def __init__(self, imc = 0):
        self.imc = imc


    def imc_calc(self, *, peso, altura):
        """
        Calcula o indice de massa corporal.
        """
        try:
            resultado = float(peso) / (float(altura) ** 2)
            self.imc = resultado
        
        except:
            self.imc = 0
        


    @staticmethod
    def ckeck_number(numero):
        """
        Verifica o resultado de input.
        """
        if len(numero) == 0:
            return 0
        else:
            return numero.replace(" ", "")


    @staticmethod
    def classificacao(*, n: float):
        """
            Retorna a classificacão do imc.
        """
        if n > 2.0 and n <= 18.5:
            return "Abaixo do Peso\nNormal"
        
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