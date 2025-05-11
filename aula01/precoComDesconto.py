preco = 1000  # valor do produto
desconto = 15  # percentual de desconto

valor_do_desconto = preco * (desconto / 100)
valor_final = preco - valor_do_desconto

print("\nO preço do celular de Maria com {}% de desconto é R${:.2f}".format(desconto, valor_final))
