p1 = (7.0, 8.3, 10.0, 6.5, 9.3)
p2 = (8.5, 6.9, 5.0, 7.5, 9.8)

media_p1 = sum(p1)/len(p1)

soma = 0 
for nota in p2:
    soma = soma + nota

media_p2 = sum(p2)/len(p2)

print(f'Media turma 1 = {media_p1:.2f}')
print(f'Media turma 2 = {media_p2:.2f}')

if media_p1 > media_p2:
    print('A turma obteve a melhor média na prova 1')
else:
    print('A turma obteve a melhor média na prova 2')
