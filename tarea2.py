"""
Estrucutras de Datos 2do semestre 2019
Tarea2
Lester Efrain Ajucum Santos
201504510
"""
import os

def printMain():
	print()
	print ("----------- Main Menu -----------")
	print ("1.Mapeo Por Filas")
	print ("2.Mapeo Por Columnas")
	print ("3.Generar Imagen Matriz")
	print ("4.Generar Arreglo Linealizado")
	print ("5.Salir")

strInput = 0

rows = 0
columns = 0
rowToMap = 0
columnToMap = 0
mapResult = 0

graphTxt = ""
dotFile = None
strNewline = "\r\n"
while strInput != '5':
	print ()
	print ("-------------------------------------")
	print ("USAC")
	print ("FACULTAD DE INGENIERIA")
	print ("LESTER EFRAIN AJUCUM SANTOS")
	print ("EDD 2DO SEMESTRE")
	print ()
	printMain()
	print ()
	strInput = input("Option:")

	if strInput == '1':
		print()
		print("--------MAPEO LEXICOGRAFICO POR FILAS --------")
		print()
		print(" DIMENSIONES DEL ARREGLO (filas, columnas)")
		print()
		rows = input("Ingrese el numero de Filas del arreglo: ")
		columns = input("Ingrese el numero de Columnas del arreglo: ")
		print()
		print("Las Dimensiones de tu arreglo "+"("+rows+","+columns+")")
		print()
		print(" POSICION A LINEALIZAR (fila, columna)")
		print()
		rowToMap = input("Fila: ")
		columnToMap = input("Columna: ")
		print()
		print("La Posicion A linealizar "+"("+rowToMap+","+columnToMap+")")
		print()
		mapResult = int(rowToMap)*int(columns)+int(columnToMap)

		print("RESULTADO MAPEO LEXICOGRAFICO POR FILAS")
		print()
		print("Resultado = " + str(mapResult))

		graphTxt = "digraph matriz {"+"\r\n"

		graphTxt +=str("node [shape = record];"+strNewline)

		for i in range(int(rows)):
			graphTxt += str("node"+str(i)+"[label = \"")
			for j in range(int(columns)):
				graphTxt += str("<f"+str(j)+"> |")
			graphTxt += str("\"];"+strNewline)
		
		
		for i in range(int(rows)):
			graphTxt += str("{ rank = same;")
			graphTxt += str("\""+"node"+str(i)+"\";")
			graphTxt += str("}"+strNewline)

		for i in range(int(rows)):
			graphTxt += str("node"+str(i)+"->")
			graphTxt += str("[style = invis];"+strNewline)
			

		graphTxt += "}"

		dotFile = open("tarea2.txt","w+")
		dotFile.write(graphTxt)
		dotFile.close()   
	
	elif strInput == '2':
		print()
		print("--------MAPEO LEXICOGRAFICO POR COLUMNAS --------")
		print()
		print(" DIMENSIONES DEL ARREGLO (filas, columnas)")
		print()
		rows = input("Ingrese el numero de Filas del arreglo: ")
		columns = input("Ingrese el numero de Columnas del arreglo: ")
		print()
		print("Las Dimensiones de tu arreglo "+"("+rows+","+columns+")")
		print()
		print(" POSICION A LINEALIZAR (fila, columna)")
		print()
		rowToMap = input("Fila: ")
		columnToMap = input("Columna: ")
		print()
		print("La Posicion A linealizar "+"("+rowToMap+","+columnToMap+")")
		print()
		mapResult = int(columnToMap)*int(rows)+int(rowToMap)

		print("RESULTADO MAPEO LEXICOGRAFICO POR FILAS")
		print()
		print("Resultado = " + str(mapResult))

	elif strInput == '3':
		os.system("dot -Tjpg tarea2.txt -o matriz.jpg")
		os.system('matriz.jpg')
	#elif strInput == '4':
	#	stackMenu()
	elif strInput == '5':
		break