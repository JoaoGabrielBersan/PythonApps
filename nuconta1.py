# Input Selic e dinheiro na NuConta
nuconta = float(input('Quanto você tem na sua NuConta? R$'))
selic = float(input('Quanto vale a taxa Selic? (em %) '))
# Fórmula para o CDI anual e diário
cdiano = (selic-0.1)
cdidia = (((1+(cdiano/100))**(1/252)-1)*100)
# Fórmula para o rendimento
rendia = (nuconta*(cdidia/100))
# Output CDI diário, rendimentos em diferentes períodos
print('O CDI rende {:.4f}% em um dia'.format (cdidia))
print('Mantendo o valor do CDI, sua conta vai render:')
print('R${:.2f} em um dia;' .format(rendia))
print('R${:.2f} em 5 dias (1 semana útil);' .format(((1+rendia)*5)-1))
print('R${:.2f} em 21 dias (1 mês útil);' .format(((1+rendia)*21)-1))
print('R${:.2f} em 252 dias (1 ano útil);' .format(((1+rendia)*252)-1))
# Comparação com poupança: fórmulas p/ rendimento, input TR e output rendimentos
p = int(input('Quer comparar o rendimento com o da poupança? \n 1 - Sim \n 2 - Não \n ->'))
if p == 1:
    tr = float(input('Qual é a TR atual? (em %)'))
    poup = ((selic * 0.7 / 100) + (tr / 100))
    renpoup = (nuconta * poup)
    print('Essa mesma quantidade renderia R${:.2f} na poupança em um ano.' .format(renpoup))
    print('Ao deixar seu dinheiro na NuConta, você está ganhando R${:.2f} em relação à poupança.' .format((((1+rendia)*252)-1)-renpoup))
