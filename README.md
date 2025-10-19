# Mapeamento Cachê

O FIFO (First-In, First-Out) substitui a página que está há mais tempo na memória. Ele usa uma lista chamada memoria para armazenar as páginas e um ponteiro que indica qual posição será substituída próxima.

O LRU (Least Recently Used) substitui a página que não é usada há mais tempo. Ele mantém uma fila que controla a ordem de acesso das páginas, onde a página no início é a menos recentemente usada.

O MRU (Most Recently Used) substitui a página que foi usada mais recentemente. Ele usa um dicionário chamado ultimo_acesso para registrar o momento exato em que cada página foi acessada, permitindo identificar qual página foi a mais recente.

---

# Resultados

Caso A - Página 7:
  - FIFO: Posição 5. Page Faults: 13.
  - LRU: Posição 6. Page Faults: 12.
  - MRU: Posição 3. Page Faults: 11 (MENOR PAGE FAULTS)

Caso B - Página 11:
  - FIFO: Posição 6. Page Faults: 14. (EMPATE)
  - LRU: Posição 3. Page Faults: 16.
  - MRU: Posição 7. Page Faults: 14. (EMPATE)

Caso C - Página 11:
  - FIFO: Posição 5. Page Faults: 13.
  - LRU: Posição 6. Page Faults: 11. (MENOR PAGE FAULTS)
  - MRU: Posição 8. Page Faults: 12.

Page Faults Totais:

  FIFO: 13 + 14 + 13 = 40
  LRU: 12 + 16 + 11 = 39
  MRU: 11 + 14 + 12 = 27

---

# Qual a Melhor Política de Substituição?

Baseado nos page faults totais, nos exemplos dados, o MRU apresentou a melhor performance geral, seguido pelo LRU e FIFO.

# Link

https://youtu.be/StVvrrPjV-M
