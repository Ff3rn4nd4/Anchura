#es necesario importar la liberia time para que muestre el tiempo que tardo en la ejecucion
import time
start_time = 0
import os

#GRAFO, donde nuestros saltos son la relacion que hay entre B/P

grafo = {
			'I': [('1',3), ('2',2.5), ('3',2),('4',1.86)],
         	'1': [('2',2.5), ('3',2),('4',1.86)],
			'2': [('1',3),('3',2),('4',1.86)],
			'3': [('1',3), ('2',2.5),('4',1.86)],
			'4': [('1',3), ('2',2.5), ('3',2)]
		}
		
visitados = []
cola = []

origen = input("Ingresa el nodo origen: ")
print("\nLista de recorrido en anchura\n")
#Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA COLA
cola.append(origen)
#Paso 2: MIENTRAS LA COLA NO ESTE VACÍA
while cola:
	#paso 3: DESENCOLAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
	actual = cola.pop(0)

	#paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
	if actual not in visitados:
		#paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
		print("Vertice actual -> ", actual)
		#paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
		visitados.append(actual)
	#paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
	#        Y QUE NO HA SIDO VISITADO:
	#        ENCOLAR EL VERTICE
	for key, lista in grafo[actual]:
		if key not in visitados:
			cola.append(key)

print()
print("--------%s seconds -----"%(time.time() - start_time))
