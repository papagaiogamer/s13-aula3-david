
#feito por:david 
def categorizar_livro(titulo,  categoria): 
    categoria_dict={
    "ficção": f"{titulo} é um livro de ficção.",
    "não ficção": f"{titulo} é um livro de não ficção.",
    "referência": f"{titulo} é um livro de referência."
    } 
    return categoria_dict.get(categoria,f"{titulo} não é um livro válido.")
 
def calcular_multa(categoria,  dias_atraso): 
    if categoria == "ficção": 
        return dias_atraso * 0.50
    elif categoria == "não ficção": 
        return dias_atraso * 0.60
    else: 
        return 0

titulo = input("Digite o titulo do livro:  ")
categoria = input("Digite a categoria do livro (ficção,  não ficção,  referência):  ")
dias_atraso = int(input("Digite o número de dias em atraso:  "))

print(categorizar_livro(titulo,  categoria))
print("A multa é de R$", calcular_multa(categoria,   dias_atraso))
