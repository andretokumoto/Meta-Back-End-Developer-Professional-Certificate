def soma(**kwargs):
    soma = 0 
    for prd,number in kwargs.items():
        soma+=number
        
    return soma

print(soma(cafe=12.50,bolo=23.4,suco=10))