# selic and tr are basis rates for calculating yields.
selic = 0.045
tr = 0.0
# input the amount of money the user has in poupança
caixa = float(input('Quanto você tem na poupança? R$'))
# cdi and poupança formulas
cdi = float((selic-0.001))
poupança = float((0.7*cdi))
# yield formulas
rcdi = float((caixa*(cdi)))
rpoupança = float((caixa*(poupança)))
# outputs yields and the difference between them
print('Seu dinheiro rende R${:.2f} na poupança e R${:.2f} no CDI.' .format(rpoupança, rcdi))
print('Você está perdendo R${:.2f} por ano investindo na poupança.' .format((rcdi-rpoupança)))
