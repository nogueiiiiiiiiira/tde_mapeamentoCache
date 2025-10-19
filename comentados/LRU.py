memoria = []  # lista para armazenar as páginas em memória
page_faults = 0  # contador de page faults
fila = []  # lista que funciona como fila para controlar a ordem de uso das páginas
paginas = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7] 
quadros = 8 

for pagina in paginas:
    
    if pagina not in memoria:  # se a página não está na memória
        page_faults = page_faults + 1 # aumenta o número de page faults
        
        if len(memoria) < quadros:  # se ainda há espaço na memória
            memoria.append(pagina)  # adiciona a página na memória
            fila.append(pagina)  # adiciona a página na fila de uso, mais recentemente usada
        else:
            pagina_removida = fila.pop(0)  # remove a página menos recentemente usada
            index = memoria.index(pagina_removida)  # encontra o índice da página removida na memória
            memoria[index] = pagina  # substitui a página na memória pela nova página
            fila.append(pagina)  # adiciona a nova página no final da fila
    else:
        fila.remove(pagina)  # remove a página da fila para atualizar a posição de uso
        fila.append(pagina)  # adiciona a página no final da fila para marcar como mais recentemente usada

posicao_7 = -1  # posição da página 7 na memória, -1 indica não encontrada

for i in range(len(memoria)):
    if memoria[i] == 7:
        posicao_7 = i  # armazena a posição da página 7
        
if posicao_7 != -1:
    print("\n1A (LRU) - A página 7 ficou na posição:", posicao_7 + 1)
else:
    print("\n1A (LRU) - A página 7 não ficou na memória")
    
print("Page Faults:", page_faults)
print("Memória final:", memoria)



# reinicia para 1B

memoria = []
page_faults = 0
fila = []

paginas = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
quadros = 8

for pagina in paginas:
    
    if pagina not in memoria:
        page_faults = page_faults + 1
        
        if len(memoria) < quadros:
            memoria.append(pagina)
            fila.append(pagina)
        else:
            pagina_removida = fila.pop(0)
            index = memoria.index(pagina_removida)
            memoria[index] = pagina
            fila.append(pagina)
    else:
        fila.remove(pagina)
        fila.append(pagina)

posicao_11 = -1

for i in range(len(memoria)):
    if memoria[i] == 11:
        posicao_11 = i
        
if posicao_11 != -1:
    print("\n1B (LRU) - A página 11 ficou na posição:", posicao_11 + 1)
else:
    print("\n1B (LRU) - A página 11 não ficou na memória")
    
print("Page Faults:", page_faults)
print("Memória final:", memoria)



# reinicia para 1C

memoria = []
page_faults = 0
fila = []

paginas = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
quadros = 8

for pagina in paginas:
    
    if pagina not in memoria:
        page_faults = page_faults + 1
        
        if len(memoria) < quadros:
            memoria.append(pagina)
            fila.append(pagina)
        else:
            pagina_removida = fila.pop(0)
            index = memoria.index(pagina_removida)
            memoria[index] = pagina
            fila.append(pagina)
    else:
        fila.remove(pagina)
        fila.append(pagina)

posicao_11 = -1

for i in range(len(memoria)):
    if memoria[i] == 11:
        posicao_11 = i

if posicao_11 != -1:
    print("\n1C (LRU) - A página 11 ficou na posição:", posicao_11 + 1)
else:
    print("\n1C (LRU) - A página 11 não ficou na memória")
    
print("Page Faults:", page_faults)
print("Memória final:", memoria)

