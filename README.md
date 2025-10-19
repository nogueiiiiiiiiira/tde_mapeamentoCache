Trabalho - Mapeamento de Memória Cache

===

FIFO (First-In, First-Out):
  - Substitui a página que está há mais tempo na memória

LRU (Least Recently Used):
  - Substitui a página que não é utilizada há mais tempo

MRU (Most Recently Used):
  - Substitui a página que foi utilizada mais recentemente

---

Resultados

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

Qual a Melhor Política de Substituição?

Baseado nos page faults totais, nos exemplos dados, o MRU apresentou a melhor performance geral, seguido pelo LRU e FIFO.
