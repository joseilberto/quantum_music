Distância entre tempos de ocorrência
============

Nesse modelo, as notas são definidas como a nota base e sua respectiva altura,
por exemplo: C#88 e A80. A distância entre cada nota é calculada simplesmente
pelo tempo que as separa, caso esse tempo seja maior que zero.

Para executar o script para o arquivo macarena_file_colunas.txt e gerar
o código de barras de todas as notas:
```bash
python3 stats_music.py -s macarena -b true
```
