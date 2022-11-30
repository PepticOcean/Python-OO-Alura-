def create_account(number, holder, balance, limit):
    account = {"Numero": number, "Titular": holder, "Saldo": balance, "Limite": limit}
    return account


def deposite(account, value):
    account["Saldo"] += value


def draw(account, value):
    account["balance"] -= value


def extract(account):
    print("Saldo {}".format(account["balance"]))
