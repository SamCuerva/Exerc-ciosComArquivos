import os

valor: int = 0
dir: str = '/tmp/exercicios'
arq: str = 'Ex34.txt'


def main():
    global valor

    contador = 0
    result = 0

    os.makedirs(dir, exist_ok=True)
    os.chmod(dir, 0o744)

    valor = int(input('Digite um valor entre 1 e 10: '))

    while valor < 1 or valor > 10:
        valor = int(input('Valor inválido! Digite um valor entre 1 e 10: '))

    for contador in range(0, 11):
        result = mult(valor, contador)
        grava(contador, result)


def mult(vlr, tab):
    res = vlr * tab
    return res


def grava(c, rslt):
    global dir, arq

    file: str = ''
    tipo: str = ''
    enc: str = ''
    linha: str = ''

    file = dir + "/" + arq

    enc = 'utf-8'
    linha = str(rslt) + '\n'

    if os.path.exists(dir) and os.path.isdir(dir):

        tipo = 'w'

        if os.path.isfile(file) and c > 0:
            tipo = 'a'

        with open(file, tipo, encoding=enc) as arquivo:
            arquivo.write(linha)


if __name__ == '__main__':
    main()
