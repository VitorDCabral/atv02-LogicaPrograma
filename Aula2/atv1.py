idade1 = int(input("Digite a sua idade:"))
idade2 = int(input("Digite a idade do seu amigo:"))

if idade1 > idade2:
    print("Você é mais velho que seu amigo")
elif idade1 < idade2:
   print("Seu amigo é mais velho que você")
elif idade1 == idade2:
    print("Você e seu amigo tem a mesma idade")
else:
    print("ERRO")
