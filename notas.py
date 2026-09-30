notas = []
for i in range(2):
    nota = float(input("Digite sua nota:"))
    notas.append(nota)

nota1 = notas[0]
nota2 = notas[1]
media =(nota1 + nota2) / 2
if media >= 7:
    print(f"Você está aprovado, sua media foi {media}")
else:
    print(f"Você esta reprovado sua nota foi apenas {media}")