lista_codigos = []
lista_altura = []
lista_peso = []


def guardarDados(altura, codigo_cliente, peso):
    lista_altura.append(altura)
    lista_codigos.append(codigo_cliente)
    lista_peso.append(peso)


def media_pesos(lista_peso):
    print('A média dos pesos é ' + str(float(sum(lista_peso) / len(lista_peso))))


def media_alturas(lista_altura):
    print('A média das alturas é ' +
          str(float(sum(lista_altura) / len(lista_altura))))


i = 1

maior_peso = 0
menor_peso = 99999

maior_altura = 0
menor_altura = 99999

while i != 0:
    codigo_cliente = str(
        input('Digite seu código de 4 dígitos (apenas números): '))
    if len(codigo_cliente) == 4 and codigo_cliente not in lista_codigos:
        altura = int(input('Qual a sua altura: '))
        peso = int(input('Qual o seu peso: '))

        if (peso > maior_peso):
            maior_peso = peso
            maior_peso_id = codigo_cliente
            altura_maior_peso = altura

        if (peso < menor_peso):
            menor_peso = peso
            menor_peso_id = codigo_cliente
            altura_menor_peso = altura

        if (altura > maior_altura):
            maior_altura = altura
            maior_altura_id = codigo_cliente
            peso_maior_altura = peso

        if (altura < menor_altura):
            menor_altura = altura
            menor_altura_id = codigo_cliente
            peso_menor_altura = peso

        guardarDados(altura, codigo_cliente, peso)

        i = int(input('Digite 0 se deseja encerrar ou 1 para continuar: '))

    elif len(codigo_cliente) < 4:
        print('Inválido, digite um código de 4 dígitos: ')
    elif codigo_cliente in lista_codigos:
        print('Código repetido, favor digitar outro: ')

if i == 0:
    print('O mais gordo possui: ' + str(maior_peso) +
          'Kg e ' + str(altura_maior_peso) + 'Cm de altura - CÓDIGO ' + str(maior_peso_id))
    print('O mais magro possui: ' + str(menor_peso) +
          'Kg e ' + str(altura_menor_peso) + 'Cm de altura - CÓDIGO ' + str(menor_peso_id))
    print('O mais alto possui: ' + str(maior_altura) +
          'Cm de altura e  ' + str(peso_maior_altura) + 'Kg - CÓDIGO ' + str(maior_altura_id))
    print('O mais baixo possui: ' + str(menor_altura) +
          'Cm de altura e ' + str(peso_menor_altura) + 'Kg - CÓDIGO ' + str(menor_altura_id))
    media_alturas(lista_altura)
    media_pesos(lista_peso)
