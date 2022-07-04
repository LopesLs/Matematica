#  1.	 Faça um programa que calcule em uma matriz 3x3;
#
# +-----+-----+-----+-----+
# | i,j |  1  |  2  |  3  |
# +-----+-----+-----+-----+
# |  1  |  0  |  1  |  2  |
# |  2  | 10  | 11  | 12  |
# |  3  | 20  | 21  | 22  |
# +-----+-----+-----+-----+

print('''
         Matriz
+-----+-----+-----+-----+
| i,j |  0  |  1  |  2  |
+-----+-----+-----+-----+
|  0  |  1  |  2  |  3  |
|  1  |  4  |  5  |  6  |
|  2  |  7  |  8  |  9  |
+-----+-----+-----+-----+''')


m1 = [
    [0o1, 0o2, 0o3],
    [4, 5, 6],
    [7, 8, 9]
]

somavrtc1 = 0
somavrtc2 = 0
somavrtc3 = 0

for i in m1:
    somavrtc1 += i[0]
    somavrtc2 += i[1]
    somavrtc3 += i[2]

print('\nSOMA DAS VERTICAIS DA MATRIZ')
print(f'\nSoma vertical primeira linha: {somavrtc1}')
print(f'Soma vertical segunda linha: {somavrtc2}')
print(f'Soma vertical terceira linha: {somavrtc3}')

somahorizontal1 = 0
somahorizontal2 = 0
somahorizontal3 = 0

indice = 0
for i in m1:
    
    if indice == 0:
        somahorizontal1 = sum(i)
    
    elif indice == 1:
        somahorizontal2 = sum(i)
    
    elif indice == 2:
        somahorizontal3 = sum(i)
    
    else:
        pass

    indice += 1 

print('\nSOMA DAS HORIZONTAIS DA MATRIZ')
print(f'\nSoma horizontal primeira linha: {somahorizontal1}')
print(f'Soma horizontal segunda linha: {somahorizontal2}')
print(f'Soma horizontal terceira linha: {somahorizontal3}')

indice = 0
soma_first_diagonal = 0
soma_second_diagonal = 0

for i in m1:
    
    for j in i:
    
        if indice == m1[indice].index(j):
            soma_first_diagonal += j
        
        elif indice == 2 and m1[indice].index(j) == 0 or indice == 0 and m1[indice].index(j) == 2:
            print(j)
            soma_second_diagonal += j
        
        if indice == 1 and m1[indice].index(j) == 1:
            soma_second_diagonal += j

    indice += 1

print('\nSOMA DAS DIAGONAIS DA MATRIZ')
print(f'\nSoma da diagonal principal: {soma_first_diagonal}')
print(f'Soma da diagonal secundária: {soma_second_diagonal}')
