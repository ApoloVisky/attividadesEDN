def classificar_idade(idade):
    if idade >= 65:
        return "idoso"
    elif idade >= 18:
        return "adulto"
    elif idade >= 12:
        return "adolescente"
    elif idade >= 3:
        return "criança"
    else:
        return "bebê"

idade = int(input("Digite a sua idade: "))
categoria = classificar_idade(idade)

print("Você é " + categoria)
