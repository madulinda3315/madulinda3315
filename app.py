print("ola mundo")

nome= "maria eduarda"
idade= 19
altura= 1.70
estudante= True

print(f"NOME:{nome},idade:{idade},altura{altura},estudante{estudante}") 

mensagem= "python é divertido" 
print(mensagem.strip())
print(mensagem.lower())

nome= input("qual seu nome?")
print(f"ola,{nome}!bem vindo ao curso de python.")


nome=input ("qual é o seu nome?")
print(f"olá, {nome}!bem vindo ao curso de python.")



from datetime import datetime 
nome= input("qual é o seu nome?")
agora= datetime.now()
hora_atual= agora.strftime("%H:%M")
print(f"ola, {nome}!agora são {hora_atual}.")

from datetime import datetime
nome= input ("qual é o seu nome?")
agora= datetime.now ()
hora_atual= agora.strftime("%H;%M")
print(f" olá, {nome}! agora são {hora_atual}")