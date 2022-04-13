import re

def transformar(n_1,n_2):
    """
    Transforma las listas de notas string en enteros
    para asi poder sacar la suma y el promedio de dichas notas
    y generar una nueva lista de cada par de notas unidas en una sola
    """
    promedio = lambda x,y: (x + y) / 2
    n_1f = list(map(int, n_1))
    n_2f = list(map(int, n_2))
    n_f = []
    """
    Se juntan las 2 listas en una haciendo los promedios de ambar listas
    """
    for i in range(len(n_1)):
        n_f.append(promedio(n_1f[i],n_2f[i]))
    return n_f

def listar(arch):
    """
    Genera 3 listas de cada archivo para procesarlas    
    """
    aux = []
    for i in arch.readlines():
        aux.append(i.replace(",","").replace("'","").replace("\n",""))
    return aux

def merge(nota_final,nombre):
    """
    Une la nota final con el nombre en un diccionario para asi conseguir la 
    estructura final
    """
    n_f = {}
    for i in range(len(nota_final)):
        n_f[nombre[i]] = nota_final[i]
    return  n_f

def imprimir(estructura,prom_general):
    """
    Imprime las personas con sus respectivas notas que estan debajo del promedio general
    """
    for nombre,nota in estructura.items():
        if (nota < prom_general):
            print(f"Nombre: {nombre} \nPromedio: {nota}")
            print('*' * 30 )

def main():
    """
    El main del programa donde se desarrollan las funciones del merge de las notas y
    promedio de las mismas por cada alumno y el promedio general imprimiendo los alumnos
    con nota debajo del promedio
    """
    with open("nombres_1.txt","r",encoding="utf-8") as nombres:
        nom = listar(nombres)
    with open("eval1.txt","r",encoding="utf-8") as  notas_1:
        n_1 = listar(notas_1)
    with open("eval2.txt","r",encoding="utf-8") as notas_2:
        n_2 = listar(notas_2)
    n_final = transformar(n_1,n_2)
    fin = sum(n_final)
    general = (fin / len(n_final))
    estructura = merge(n_final,nom)
    imprimir(estructura,general)

if __name__ == '__main__':
    main()