# Input CDI anual e dinheiro na NuConta
nuconta = float(input('Quanto você tem na sua NuConta?'))
cdiano = float(input('Qual é o valor do CDI? (em %)'))
# Fórmula p o CDI diário
cdidia = (((1+(cdiano/100))**(1/252)-1)*100)
# Fórmula para o rendimento
rendia = (nuconta*(cdidia/100))
# Output CDI diário, rendimentos em diferentes períodos
print('O CDI rende {:.4f}% em um dia'.format (cdidia))
print('Mantendo o valor do CDI, sua conta vai render:')
print('{:.2f} em um dia;' .format(rendia))
print('{:.2f} em 5 dias (1 semana útil);' .format(((1+rendia)*5)-1))
print('{:.2f} em 21 dias (1 mês útil);' .format(((1+rendia)*21)-1))
print('{:.2f} em 252 dias (1 ano útil);' .format(((1+rendia)*252)-1))
