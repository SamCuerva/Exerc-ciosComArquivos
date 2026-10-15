import os

nome: str = ""
nota1: float = 0
nota2: float = 0
nota3: float = 0
nota4: float = 0
valor_media: float = 0
dir: str = "/tmp/exercicios"
arq: str = "Ex21.txt"

def entrada():

    global nome
    global nota1
    global nota2
    global nota3
    global nota4
    global valor_media

    nome = input("Digite o nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))

    valor_media = med(nota1, nota2, nota3, nota4)
    print("Média: ", valor_media)

    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)

def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):

    global arq
    global dir

    linha: str = nm + ";\n" + "Nota 1: " + str(nt1) + ";\n" + "Nota 2: " + str(nt2) + ";\n" + "Nota 3: " + str(nt3) + ";\n" + "Nota 4: " + str(nt4) + ";\n" + "Média: " + str(vlr_med) + ";\n"
    escreveArq(dir, arq, linha)

def escreveArq(caminho, arquivo, linha_arq):

    file: str = ""
    tipo: str = ""
    enc: str = ""

    file = caminho + "/" + arquivo
    enc = "utf-8"

    os.makedirs(caminho, exist_ok=True)
    os.chmod(caminho, 0o744)

    if os.path.exists(caminho) and os.path.isdir(caminho):

        tipo = "w"

        if os.path.isfile(file):

            tipo = "a"

        with open(file, tipo, encoding=enc) as arquivo: 

            arquivo.write(linha_arq)

def med(n1, n2, n3, n4):

    media: float = 0
    media = (n1 + n2 + n3 + n4) / 4
    

    return media


def main():
    
    contador: int = 0
    for i in range(1, 6):

        entrada()


if __name__ == "__main__":
    main()