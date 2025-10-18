memoria = []
page_faults = 0
fila = []

paginas = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
quadros = 8

for pagina in paginas:
    
    if pagina not in memoria:

        if len(memoria) < quadros:
            memoria.append(pagina)
            fila.append(pagina)
            page_faults = page_faults + 1
            
        else:
            pagina_removida = fila.pop(0)
            memoria.remove(pagina_removida)
            memoria.append(pagina)
            fila.append(pagina)
            page_faults = page_faults + 1
            
    else:
        fila.remove(pagina)
        fila.append(pagina)

if 7 in memoria:
    print("\nA página 7 ficou na posição: ", memoria.index(7))
else:
    print("\nA página 7 não ficou na memória no final.")


memoria = []
page_faults = 0
fila = []

paginas = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
quadros = 8

for pagina in paginas:
    
    if pagina not in memoria:

        if len(memoria) < quadros:
            memoria.append(pagina)
            fila.append(pagina)
            page_faults = page_faults + 1
            
        else:
            pagina_removida = fila.pop(0)
            memoria.remove(pagina_removida)
            memoria.append(pagina)
            fila.append(pagina)
            page_faults = page_faults + 1
            
    else:
        fila.remove(pagina)
        fila.append(pagina)

if 11 in memoria:
    print("A página 11 ficou na posição: ", memoria.index(11))
else:
    print("A página 11 não ficou na memória no final.")


memoria = []
page_faults = 0
fila = []

paginas = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
quadros = 8

for pagina in paginas:
    
    if pagina not in memoria:

        if len(memoria) < quadros:
            memoria.append(pagina)
            fila.append(pagina)
            page_faults = page_faults + 1
            
        else:
            pagina_removida = fila.pop(0)
            memoria.remove(pagina_removida)
            memoria.append(pagina)
            fila.append(pagina)
            page_faults = page_faults + 1
            
    else:
        fila.remove(pagina)
        fila.append(pagina)

if 11 in memoria:
    print("A página 11 ficou na posição: ", memoria.index(11))
else:
    print("A página 11 também não ficou na memória no final.")
