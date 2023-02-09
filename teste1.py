#Programa 03, livro pense bem ATIVIDADES 3
input("Digite o codigo 031 -> ")
nome = input("Digite nome do jogador: ")
pontos = 0
acertou = False
resp = input("Digite a resposta da pergunta 1 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 1 (A)
if resp == 'A':
        pontos +=3
        acertou = True
        print("Parabens, proxima pergunta, 3 pontos")
        resp = input("Digite a resposta da pergunta 2 (A/B/C/D)? -> ")
else:
        print ("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 1 (A/B/C/D)? -> ")

if (acertou == False) :
        if resp == 'A':
          pontos +=2
          acertou = True
          print("Parabens, proxima pergunta, 2 pontos")
          resp = input("Digite a resposta da pergunta 2 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, tente outra vez...")
          resp = input("Digite a resposta da pergunta 1 (A/B/C/D)? -> ")

if (acertou == False):
        if resp == 'A':
          pontos +=1
          print("Parabens, proxima pergunta, 1 pontos")
          resp = input("Digite a resposta da pergunta 2 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, proxima pergunta, 0 pontos...")
          resp = input("Digite a resposta da pergunta 2 (A/B/C/D)? -> ")
resp = resp.upper()
#pergunta 2(A)

if resp == 'A':
        pontos +=3
        acertou = True
        print("Parabens, proxima pergunta, 3 pontos")
        resp = input("Digite a resposta da pergunta 3 (A/B/C/D)? -> ")
else:
        print ("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 2(A/B/C/D)? -> ")

if (acertou == False) :
        if resp == 'A':
          pontos +=2
          acertou = True
          print("Parabens, proxima pergunta, 2 pontos")
          resp = input("Digite a resposta da pergunta 3 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, tente outra vez...")
          resp = input("Digite a resposta da pergunta 2 (A/B/C/D)? -> ")

if (acertou == False):
        if resp == 'A':
          pontos +=1
          print("Parabens, proxima pergunta, 1 pontos")
          resp = input("Digite a resposta da pergunta 3 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, proxima pergunta, 0 pontos...")
          resp = input("Digite a resposta da pergunta 3 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 3 (D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 4 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 3 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 4 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 3 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 4 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 4 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 4 (C)
if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 5 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 4 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 5 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 4 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 5 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 5 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 5 (B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 6 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 5 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 6 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 5 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 6 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 6 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 6 (D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 7 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 6 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 7 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 6 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 7 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 7 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 7 (A)
if resp == 'A':
        pontos +=3
        acertou = True
        print("Parabens, proxima pergunta, 3 pontos")
        resp = input("Digite a resposta da pergunta 8 (A/B/C/D)? -> ")
else:
        print ("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 7 (A/B/C/D)? -> ")

if (acertou == False) :
        if resp == 'A':
          pontos +=2
          acertou = True
          print("Parabens, proxima pergunta, 2 pontos")
          resp = input("Digite a resposta da pergunta 8 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, tente outra vez...")
          resp = input("Digite a resposta da pergunta 7 (A/B/C/D)? -> ")

if (acertou == False):
        if resp == 'A':
          pontos +=1
          print("Parabens, proxima pergunta, 1 pontos")
          resp = input("Digite a resposta da pergunta 8 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, proxima pergunta, 0 pontos...")
          resp = input("Digite a resposta da pergunta 8 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 8(A)
if resp == 'A':
        pontos +=3
        acertou = True
        print("Parabens, proxima pergunta, 3 pontos")
        resp = input("Digite a resposta da pergunta 9 (A/B/C/D)? -> ")
else:
        print ("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 8 (A/B/C/D)? -> ")

if (acertou == False) :
        if resp == 'A':
          pontos +=2
          acertou = True
          print("Parabens, proxima pergunta, 2 pontos")
          resp = input("Digite a resposta da pergunta 9 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, tente outra vez...")
          resp = input("Digite a resposta da pergunta 8 (A/B/C/D)? -> ")

if (acertou == False):
        if resp == 'A':
          pontos +=1
          print("Parabens, proxima pergunta, 1 pontos")
          resp = input("Digite a resposta da pergunta 9 (A/B/C/D)? -> ")
        else:
          print("Resposta errada, proxima pergunta, 0 pontos...")
          resp = input("Digite a resposta da pergunta 9 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 9 (D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 10 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 9 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 10 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 9 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 10 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 10 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 10 (C)
if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 11 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 10 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 11 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 10 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 11 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 11 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 11 (B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 12 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 11 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 12 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 11 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 12 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 12 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 12 (B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 13 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 12 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 13 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 12 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 13(A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 13 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 13 (C)
if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 14 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 13 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 14 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 13 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 14 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 14 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 14 (D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 15 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 14 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 15 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 14 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 15 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 15 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 15(D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 16 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 15 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 16 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 15 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 16 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 16 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 16(D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 17 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 16 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 17 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 16 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 17 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 17 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 17(D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 18 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 17 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 18 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 17 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 18 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 18 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 18(B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 19 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 18 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 19 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 18 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 19 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 19 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 19(D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 20 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 19 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 20 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 19 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 20 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 20 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 20(C)
if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 21 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 20 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 21 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 20 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 21 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 21 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 21(D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 22 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 21 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 22 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 21 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 22 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 22 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 22(A)
if resp == 'A':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 23 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 22 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'A':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 23 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 22 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'A':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 23 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 23 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 23(B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 24 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 23 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 24 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 23 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 24 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 24 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 24(D)
if resp == 'D':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 25 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 24 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 25 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 24 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'D':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 25 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 25 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 25(A)
if resp == 'A':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 26 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 25 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'A':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 26 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 25 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'A':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 26 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 26 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 26(C)

if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 27 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 26 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 27 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 26 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 27 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 27 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 27(B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 28 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 27 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 28 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 27 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 28 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 28 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 28(C)

if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 29 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 28 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 29 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 28 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 29 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 29 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 29(C)
if resp == 'C':
    pontos += 3
    acertou = True
    print("Parabens, proxima pergunta, 3 pontos")
    resp = input("Digite a resposta da pergunta 30 (A/B/C/D)? -> ")
else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 29 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 2
        acertou = True
        print("Parabens, proxima pergunta, 2 pontos")
        resp = input("Digite a resposta da pergunta 30 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 29 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'C':
        pontos += 1
        print("Parabens, proxima pergunta, 1 pontos")
        resp = input("Digite a resposta da pergunta 30 (A/B/C/D)? -> ")
    else:
        print("Resposta errada, proxima pergunta, 0 pontos...")
        resp = input("Digite a resposta da pergunta 30 (A/B/C/D)? -> ")
resp = resp.upper()
#PERGUNTA 30(B)
if resp == 'B':
    pontos += 3
    acertou = True
    print("Parabens, 3 pontos")

else:
    print("Resposta errada, tente outra vez...")
    resp = input("Digite a resposta da pergunta 30 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 2
        acertou = True
        print("Parabens, 2 pontos")

    else:
        print("Resposta errada, tente outra vez...")
        resp = input("Digite a resposta da pergunta 30 (A/B/C/D)? -> ")

if (acertou == False):
    if resp == 'B':
        pontos += 1
        print("Parabens,  1 pontos")

    else:
        print("Resposta errada, 0 pontos...")



print("**********FIM DE JOGO**********")


input("Digite OK para a contagem de pontos -> ")


print("Iniciando contagem.....")


print("O jogador ",nome, "fez o total de", pontos, "pontos")

