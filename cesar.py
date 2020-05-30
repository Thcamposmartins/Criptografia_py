#CRiptografia de Cesar
print('-'*40)
print('{:^40}'.format('Criptografia  de César 4 casas'))
print('-'*40)
print("Digite a opção desejada: ")
menu =(int(input('Para Criptografar uma frase - 1\nPara Descriptografar uma frase - 2\nPara Sai r - 0 \n:  ')))
while (menu!=0):
    if menu == 1:
        frase=(str(input('Digite a frase a ser criptografada: \n').lower()))
        x=len(frase)
        while (x!=0):
            for p in frase:
                for letra in p:

                    if letra in 'a':
                        print('d',end='')
                    if letra in 'b':
                        print('e',end='')
                    if letra in 'c':
                        print('f',end='')
                    if letra in 'd':
                        print('g',end='')
                    if letra in 'e':
                        print('h',end='')
                    if letra in 'f':
                        print('i',end='')
                    if letra in 'g':
                        print('j',end='')
                    if letra in 'h':
                        print('k',end='')
                    if letra in 'i':
                        print('l',end='')
                    if letra in 'j':
                        print('m',end='')
                    if letra in 'k':
                        print('n',end='')
                    if letra in 'l':
                        print('o',end='')
                    if letra in 'm':
                        print('p',end='')
                    if letra in 'n':
                        print('q',end='')
                    if letra in 'o':
                        print('r',end='')
                    if letra in 'p':
                        print('s',end='')
                    if letra in 'q':
                        print('t',end='')
                    if letra in 'r':
                        print('u',end='')
                    if letra in 's':
                        print('v',end='')
                    if letra in 't':
                        print('w',end='')
                    if letra in 'u':
                        print('x',end='')
                    if letra in 'v':
                        print('y',end='')
                    if letra in 'w':
                        print('z',end='')
                    if letra in 'x':
                        print('a',end='')
                    if letra in 'y':
                        print('b',end='')
                    if letra in 'z':
                        print('c',end='')
                    if letra in ' ':
                        print(' ', end='')
                    if letra in '.,:?/\][()*&$#@!':
                        print(letra, end='')
                    if letra in '1234567890':
                         print(letra, end='')
                x-=1
        if x == 0:
           menu=int(input('\nDeseja contunuar?\nPara Criptografar uma frase - 1\nPara Descriptografar uma frase - 2\nPara Sai r - 0 \n: '))
    elif menu == 2:
        frase = (str(input('Digite a frase cripitografada: \n').lower()))
        x = len(frase)
        while (x != 0):
            for p in frase:
                for letra in p:

                    if letra in 'd':
                        print('a', end='')
                    if letra in 'e':
                        print('b', end='')
                    if letra in 'f':
                        print('c', end='')
                    if letra in 'g':
                        print('d', end='')
                    if letra in 'h':
                        print('e', end='')
                    if letra in 'i':
                        print('f', end='')
                    if letra in 'j':
                        print('g', end='')
                    if letra in 'k':
                        print('h', end='')
                    if letra in 'l':
                        print('i', end='')
                    if letra in 'm':
                        print('j', end='')
                    if letra in 'n':
                        print('k', end='')
                    if letra in 'o':
                        print('l', end='')
                    if letra in 'p':
                        print('m', end='')
                    if letra in 'q':
                        print('n', end='')
                    if letra in 'r':
                        print('o', end='')
                    if letra in 's':
                        print('p', end='')
                    if letra in 't':
                        print('q', end='')
                    if letra in 'u':
                        print('r', end='')
                    if letra in 'v':
                        print('s', end='')
                    if letra in 'w':
                        print('t', end='')
                    if letra in 'z':
                        print('u', end='')
                    if letra in 'y':
                        print('v', end='')
                    if letra in 'z':
                        print('w', end='')
                    if letra in 'a':
                        print('x', end='')
                    if letra in 'b':
                        print('y', end='')
                    if letra in 'c':
                        print('z', end='')
                    if letra in ' ':
                        print(' ', end='')
                    if letra in '.,:?/\][()*&$#@!':
                        print(letra, end='')
                    if letra in '1234567890':
                        print(letra, end='')
                x -= 1
        if x == 0:
            menu = int(input('\nDeseja contunuar?\nPara Criptografar uma frase - 1\nPara Descriptografar uma frase - 2\nPara Sai r - 0 \n: '))
    else:
        print('Opção digitada não é valida!')
        menu = print(int(input('Para Criptografar uma frase - 1\nPara Descriptografar uma frase - 2\nPara Sai r - 0 \n:  ')))
