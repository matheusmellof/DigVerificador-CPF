cpf = input('Digite seu CPF (os primeiros 9 digitos somente): ')
num_cpf = 0
resto_1 = 0
resto_2 = 0
dv_1 = 0
dv_2 = 0
i = 1
j = 0

for num_1 in cpf:
    num_1 = int(num_1)
    num_1 = num_1 * i
    resto_1 = resto_1 + num_1
    i = i + 1

for num_2 in cpf:
    num_2 = int(num_2)
    num_2 = num_2 * j
    resto_2 = resto_2 + num_2
    j = j + 1

if dv_1 == 10:
    dv_1 = 0
    dv_1 = resto_1 % 11
    cpf = cpf + str(dv_1)
else:
    dv_1 = resto_1 % 11
    cpf = cpf + str(dv_1)

if dv_2 == 10:
    dv_2 = 0
    dv_2 = resto_2 % 11
    cpf = cpf + str(dv_2)
else:
    dv_2 = resto_2 % 11
    cpf = cpf + str(dv_2)

print(f'--------------------------------------------------')
print(f'O primeiro digito verificador do seu CPF é: {dv_1}')
print(f'O segundo digito verificador do seu CPF é: {dv_2}\n')
print(f'CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')

for soma_cpf in cpf:
    soma_cpf = int(soma_cpf)
    num_cpf += soma_cpf
else:
    if num_cpf % 11 == 0:
        print('-------------------')
        print("O CPF é verdadeiro!\n")
    else:
        print('-------------------')
        print("O CPF é falso!\n")