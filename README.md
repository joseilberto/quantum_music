Trabalho
============

Esse repositório é dedicado aos códigos funcionais da pesquisa em música quântica. Aqui, utilizamos algumas métricas já conhecidas no estudo
da linguística quantitativa e são aplicados novos modelos para definição de propriedades relevantes no estudo quantitativo da música.

Plots
============

O código plot já é capaz de gerar gráficos para ilustrar as leis de Zipf e
Herdan-Heaps, assim como gerar os gráficos com código de barra para as posições
dos tokens. Seguem abaixo alguns exemplos do uso do plots.py:
```bash
python3 plots.py -s macarena -p zipf -m distancia_musical
```

```bash
python3 plots.py -p herdan-heaps -m distancia_tempo_inicial
```

```bash
python3 plots.py -s macarena -p bar_code -m distancia_musical
```
