notas = []
while True:
    valor = float(input("Digite sua Nota: "))
    notas.append(float(valor))
    op = input("Digite exit para sair: ")
    if op == 'exit':
        print (notas)
        media = sum(notas)/len(notas)
        print(media)