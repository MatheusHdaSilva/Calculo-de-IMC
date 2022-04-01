altura = float(input('Qual a sua altura?:'))
peso = float(input('Qual o seu peso?:'))
c1 = altura * altura
c2 = peso / c1
print('O IMC da pessoa é {:.1f}!'.format(c2))
if c2 >= 40:
    print('Você está em obesidade Mórbida, \033[0;30;41mPERIGO!\033[m')
elif c2 >= 30 < 40:
    print('Você está com Obesidade, \033[0;30;43mCUIDADO!\033[m')
elif c2 >= 25 < 30:
    print('Voçê está sobre o peso ideal, \033[0;30;44mATENÇÃO!\033[m')
elif c2 >= 18.5 < 25:
    print('Você está no peso ideal, \033[0;30;42mPARABÉNS!\033[m')
else:
    print('Voçê está abaixo de seu peso ideal, \033[0;30;46mCUIDADO!\033[m')