PS C:\Users\User\Downloads\tde_mapeamentoCache> cd .\s_comentados\
PS C:\Users\User\Downloads\tde_mapeamentoCache\s_comentados> python .\FIFO.py

1A (FIFO) - A página 7 ficou na posição: 5
Page Faults: 13
Memória final: [45, 22, 3, 25, 7, 6, 16, 35]

1B (FIFO) - A página 11 ficou na posição: 6
Page Faults: 0
Memória final: [65, 2, 1, 6, 8, 11, 14, 64]

1C (FIFO) - A página 11 ficou na posição: 5
Page Faults: 0
Memória final: [2, 4, 6, 12, 11, 10, 15, 16]
PS C:\Users\User\Downloads\tde_mapeamentoCache\s_comentados> python .\LRU.py

1A (LRU) - A página 7 ficou na posição: 6
Page Faults: 12
Memória final: [45, 22, 25, 8, 3, 7, 16, 35]

1B (LRU) - A página 11 ficou na posição: 3
Page Faults: 16
Memória final: [45, 65, 11, 2, 1, 6, 8, 14]

1C (LRU) - A página 11 ficou na posição: 6
Page Faults: 11
Memória final: [4, 6, 2, 12, 1, 11, 15, 16]
PS C:\Users\User\Downloads\tde_mapeamentoCache\s_comentados> python .\MRU.py

1A (MRU) - A página 7 ficou na posição: 3
Page Faults: 11
Memória final: [4, 3, 7, 8, 19, 6, 16, 22]

1B (MRU) - A página 11 ficou na posição: 7
Page Faults: 14
Memória final: [4, 5, 8, 9, 46, 45, 11, 64]

1C (MRU) - A página 11 ficou na posição: 8
Page Faults: 12
Memória final: [2, 12, 7, 8, 4, 10, 15, 11]
PS C:\Users\User\Downloads\tde_mapeamentoCache\s_comentados>