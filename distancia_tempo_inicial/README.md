Método da separação diferença de altura
============

Aqui, as notas são separadas pela diferença de altura entre as suas sucessivas
ocorrências. Por exemplo, se observamos a partir do modelo em distancia_musical:

A#80
...
...
...
A#40
...
...
...
A#40

Ao aplicar esse novo método, as notas serão:

A#40
...
...
...
A#00
...
...
...

(A última nota é omitida uma vez que não temos como referência qual será a
diferença de altura para próxima nota)

Para executar o script para o arquivo macarena_file_colunas_novo.txt e gerar
o código de barras de todas as notas:
```bash
python3 stats_music_initial_time.py -s macarena -b true
```

Estatísticas
============

O arquivo stats_metrics.py possui as métricas de avaliação dos dados.
Atualmente, a Lei de Zipf e Herdan-Heaps podem ser avaliadas com os métodos
implementados.
