# -*- coding: utf-8 -*-
# pip install spacy --upgrade
# python -m spacy download pt
"""_summary_"""
from pathlib import Path

from libs.limpeza import (
    limpa_caracteres_especiais,
    limpa_palavras_pequenas,
    limpa_sem_acentos,
    limpa_stopwords2,
    limpa_substantivos,
    limpa_texto_arcaismo,
    limpa_texto_final,
    limpa_texto_verbo,
    pega_nomes_proprios,
    save_file,
)
from util import *

with open("./files.txt", "r", encoding="utf-8") as fs:
    files = fs.readlines()

    for file in files:
        file = Path(file.replace("\n", ""))

        with open(file, "r", errors="ignore", encoding="utf-8") as arquivo:
            txt = arquivo.read()

        # Define o caminho RAIZ onde serão  gravados os arquivos

        file_proc = f"txt_processados/{file.name}"

        # Ver se o arquivo de ENTRADA possui pelo menos 50 caracteres para serem avaliados
        # Se não houver nada - é gravado um arquivo com esse nome VAZIO

        if txt.strip() == "" or len(txt) < 50:
            save_file(file_proc, "vazio", txt)
            continue

        # Ver se o arquivo de ENTRADA possui pelo menos 50 caracteres para serem avaliados
        # Se não houver nada - é gravado um arquivo com esse nome VAZIO

        # Aqui são retirados os caracteres especiais - verificar se ainda ficaram alguns

        texto_limpo_p1, texto_lixo_p1 = limpa_caracteres_especiais(txt)

        texto_limpo_p2, texto_lixo_p2 = limpa_palavras_pequenas(
            texto_limpo_p1, palavras_pequenas
        )
        texto_limpo_p3, texto_lixo_p3 = limpa_sem_acentos(texto_limpo_p2)
        # texto_limpo_p4, texto_lixo_p4 = transforma_texto_arcaismo(texto_limpo_p3 ,arcaismos)
        texto_limpo_p45, texto_lixo_p45 = limpa_stopwords2(texto_limpo_p3, stop_words)

        # transforma todos as palavras em minusculas
        texto_limpo_p45 = [[item[0], item[1].lower()] for item in texto_limpo_p45]

        texto_substantivos, texto_p4 = limpa_substantivos(texto_limpo_p45, substantivos)

        # start_time = time.time()

        # Estamos TROCANDO de posição da pesquisa nos VERBOS para depois dos nomes próprios
        texto_nomes, texto_p8 = pega_nomes_proprios(texto_p4, nomes_proprios)
        texto_verbos, texto_p7 = limpa_texto_verbo(texto_p8, verbos)
        # print("--- %s seconds ---" % (time.time() - start_time))

        # texto_nomes, texto_p8 = pega_nomes_proprios(texto_p7, nomes_proprios)
        texto_arcaismo, texto_p9 = limpa_texto_arcaismo(texto_p8, arcaismos)

        texto_final, texto_sobra = limpa_texto_final(
            texto_p9, texto_substantivos, texto_verbos, texto_nomes, texto_arcaismo
        )
        texto_lixo_final = (
            texto_lixo_p1 + texto_lixo_p2 + texto_lixo_p45 + texto_lixo_p3
        )

        set1 = set()
        for i in texto_lixo_final:
            i[1] = i[1].lower()
            set1.add(tuple(i))

        texto_lixo_final = sorted(list(set1), key=lambda x: x[1])

        # texto_lixo_final = f'{texto_lixo_p1}'

        save_file(file_proc, "final", texto_final)
        save_file(file_proc, "sobra", texto_sobra)

        # Rotina que salva todos os arquivos intermediarios separadamente
        #
        save_file(file_proc, "lixo", texto_lixo_final)
        print(f"--- FIM {file.name} ---")
