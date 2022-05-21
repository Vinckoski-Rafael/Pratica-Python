import random

def layout_de_abertura():
  print('Bem vindo ao jogo de advinhação')

def escolha_nivel():
  print("Digite o a sua dificuldade")
  print("1 = Para modo facil  2= Para modo medio 3= Para modo dificil")
  escolha_modo = int(input(">"))
  if (escolha_modo == 1):
    numero_de_tentativas = 5
  elif (escolha_modo == 2):
    numero_de_tentativas = 4
  elif (escolha_modo == 3):
    numero_de_tentativas = 3
  else:
    print("Numero invalido")
  return numero_de_tentativas


def gerador_de_numeros():
  numero_secreto = random.randrange(1, 101)
  print(numero_secreto)
  return numero_secreto

def ciclo_de_tentativas(numero_secreto, numero_de_tentativas):
  for rodada in range(1, numero_de_tentativas + 1):

    print("rodada {} de {}".format(rodada, numero_de_tentativas))
    chute = int(input("Digite o seu numero:"))

    if (chute < 0 or chute > 100):
      print("Você digitou um numero invalido")
      continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
      print("você acertou")
      break
    else:
      print("você errou")
      if (maior):
        print("seu chute esta acima do valor secreto")
      elif (menor):
        print("Seu chute esta abaixo do valor secreto")

        rodada= rodada + 1

def layout_de_encerramento():
  print("Fim de jogo")

layout_de_abertura()
numero_de_tentativas= escolha_nivel()
numero_secreto= gerador_de_numeros()
ciclo_de_tentativas(numero_secreto,numero_de_tentativas)
layout_de_encerramento()

