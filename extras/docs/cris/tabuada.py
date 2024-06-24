import time
#import Tkinter

def limit():
	question = input(" Por favor, Digite o número que deseja ver a tabuada:   ")
	question_l = input(" Até onde devo calcular? ")
	time.sleep(0.4)
	print("Calculando a tabuada...")
	time.sleep(0.96)
	num = (question)
	print("\n", f"Tabuada de {question}: ", "\n")
	
	l = int(question_l) +1
	if l != str:
		time.sleep(1.5)
		for i in range(1, l):
			n = int(num)*i
			time.sleep(0.4)
			print(f"{question} x {i} = ",n)
			print("___")
	else:
		for i in range(1, 11):
			n = int(num)*i
			print(f"{question} x {i} = ",n)
			print("_____")
	print("\n")
	action()

#question = input(" Deseja ver uma tabuada completa? se sim, digite um número: ")

def multiplication_table():
	question = input(" Até qual tabuada deseja ver completa?  ")
	limit = int(question) +1
	for i in range(1,limit):
		time.sleep(0.6)
		print("\n")
		print(f" Tabuada de {i}: ", "\n")
		print("calculando..")
		time.sleep(0.5)
		for x in range(1,11):
			n = i*x
			print(f"| {i} × {x} = ",n)
	
	action()


def action():
	print("\n")
	rer = input(" Deseja ver uma tabuada específica? ou uma completa (1/2)?  ")
	print(rer)
	print(type(rer))
	while rer not in ["1", "2"]:
		print("| Resposta inválida, por favor digite 1 ou 2.")
		rer = input(" Deseja ver uma tabuada específica? ou uma completa (1/2)?  ")
		
	if rer == "1":
		limit()
	else:
		multiplication_table()
		
action()