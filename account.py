class Account:
    def __init__(self, number_account, holder, balance, limit = 1000.0): #valor padrão que pode ser mudado
        self.__number_account = number_account
        self.__holder = holder
        self.__balance = balance;            #variáves com "__" são privadas
        self.__limit = limit;

    def extract(self): #recebe o self para poder pegar as informações do objeto
        print("Saldo {} do títular {}".format(self.__balance, self.__holder));

    def deposite(self, value):
        self.__balance += value;
    
    def __can_draw(self, draw_value):
        return draw_value <= (self.__balance + self.__limit) #valor disponivel para saque

    def draw(self, value):
        if(self.__can_draw(value)):
            self.__balance -= value;
        else:
            print("{} está estourando o limite".format(value))

    def transference(self,value, fate):
        self.draw(value);
        fate.deposite(value);
        self.extract();
        fate.extract();
    
    @staticmethod
    def bank_code():            #método estático (não precisa do objeto)
        return "001";

    @staticmethod
    def banks_codes():            
        return "{'BB': '001', 'Caixa': '104', 'Bradesco':'237'}"; #dicionário

    @property
    def limit(self):
        return self.__limit;

    @limit.setter
    def limit(self, limit):
        self.__limit = limit;