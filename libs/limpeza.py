# -*- coding: utf-8 -*-
import os

from unidecode import unidecode


# PASSO 1 - Caracteres especiais
def limpa_caracteres_especiais(texto_file):
    """PASSO 1 - Caracteres especiais"""

    texto_tratado, texto_lixo = [], []
    for string in texto_file.split():
        original_string = string
        string = string.replace("ç", "c").replace("Ç", "c")
        new_string = ""
        for char in string:
            if char.isalpha() or char == "-":
                new_string += char
        texto_tratado.append([original_string, new_string])

    return texto_tratado, texto_lixo


# PASSO 2 - Palavras pequenas
# def limpa_palavras_pequenas(texto_file, file_pequenos):
def limpa_palavras_pequenas(texto_file, palavras_pequenas):
    """PASSO 2 - Palavras pequenas"""

    texto_limpo, texto_lixo = [], []

    for element in texto_file:
        string = element[1]
        if len(string) > 3 or string in palavras_pequenas:
            texto_limpo.append(element)
        else:
            texto_lixo.append(element)

    return texto_limpo, texto_lixo


# PASSO 3 - Acentos
def limpa_sem_acentos(texto_file):
    """PASSO 3 - Acentos"""

    texto_limpo, texto_lixo = [], []

    for element in texto_file:
        element[1] = unidecode(element[1])
        texto_limpo.append(element)

    return texto_limpo, texto_lixo


# PASSO 4 - ARCAÍSMO
def transforma_texto_arcaismo(texto_file, file_arcaismo):
    """PASSO 4 - ARCAÍSMO"""
    texto_tratado, texto_lixo = [], []

    for element in texto_file:
        string = element[1]
        nao_arc = True
        for arcaismo in file_arcaismo:
            if string.lower() in arcaismo.split(" "):
                element[1] = string
                texto_lixo.append(element)
                element[1] = arcaismo.split(" ")[-1]
                texto_tratado.append(element)
                nao_arc = False
                break
        if nao_arc:
            texto_tratado.append(element)

    return texto_tratado, texto_lixo


# PASSO 4 5 - Stopwords
def limpa_stopwords(texto_file, stopwords):
    """PASSO 4 5 - Stopwords"""

    texto_limpo, texto_lixo = [], []  # PASSO 1 - Caracteres especiais

    for element in texto_file:
        string = element[1]
        if string[0].isupper() and string in stopwords:
            texto_limpo.append(element)
        elif string not in stopwords:
            texto_limpo.append(element)
        else:
            texto_lixo.append(element)

    return texto_limpo, texto_lixo


# PASSO 4 5 - Stopwords
def limpa_stopwords2(texto_file, stopwords):
    """PASSO 4 5 - Stopwords"""
    texto_limpo, texto_lixo = [], []

    for element in texto_file:
        string = element[1]
        if string.lower() not in stopwords:
            if string[0].isupper():
                string = string.lower()
                element[1] = f"{string[0].upper()}{string[1:]}"
                texto_limpo.append(element)
            else:
                element[1] = string.lower()
                texto_limpo.append(element)
        else:
            texto_lixo.append(element)

    return texto_limpo, texto_lixo


# PASSO 6, 8 - Substantivos
def limpa_substantivos(texto_file, file_substantivos):
    """PASSO 6, 8 - Substantivos"""
    texto_limpo, texto_lixo = [], []

    for element in texto_file:
        string = element[1]
        nao_sub = True
        for substant in file_substantivos:
            if string.lower() in substant.split(" "):
                element[1] = substant.split(" ")[0]
                texto_limpo.append(element)
                nao_sub = False
                break
        if nao_sub:
            texto_lixo.append(element)

    return texto_limpo, texto_lixo


# PASSO 7 - Verbos
def limpa_texto_verbo(texto_file, file_verbo):
    """PASSO 7 - Verbos"""

    texto_tratado, texto_lixo = [], []
    for element in texto_file:
        string = element[1]
        nao_verbo = True
        for verbo in file_verbo:
            verbo = verbo + " "
            if verbo.find(f" {string.lower()} ") >= 0:
                element[1] = verbo.split(" ")[0]
                texto_tratado.append(element)
                nao_verbo = False
                break
        if nao_verbo:
            texto_lixo.append(element)

    return texto_tratado, texto_lixo


# PASSO 10 - ARCAÍSMO
def limpa_texto_arcaismo(texto_file, file_arcaismo):
    """PASSO 10 - ARCAÍSMO"""

    texto_tratado, texto_lixo = [], []

    for element in texto_file:
        string = element[1]
        nao_arc = True
        for arcaismo in file_arcaismo:
            if string.lower() in arcaismo.split(" "):
                element[1] = arcaismo.split(" ")[-1]
                texto_tratado.append(element)
                nao_arc = False
                break
        if nao_arc:
            texto_lixo.append(element)

    return texto_tratado, texto_lixo


# PASSO 10.1 - Nomes proprios
def pega_nomes_proprios(texto_file, file_nomes):
    """PASSO 10.1 - Nomes proprios"""

    texto_limpo, texto_lixo = [], []

    for element in texto_file:
        string = element[1]
        if string.lower() in file_nomes:
            texto_limpo.append(element)
        else:
            texto_lixo.append(element)

    return texto_limpo, texto_lixo


# PASSO 11 - JOIN
def limpa_texto_final(
    file_texto, file_substantivos, file_verbo, file_nomes, file_arcaismo
):
    """# PASSO 11 - JOIN"""

    file_limpo = file_substantivos + file_verbo + file_nomes + file_arcaismo

    file_lixo = []

    for element in file_texto:
        string = element[1].lower()
        if not any(string in i[1].lower() for i in file_limpo):
            file_lixo.append(element)

    set1 = set()
    set2 = set()

    for i in file_limpo:
        i[1] = i[1].lower()
        set1.add(tuple(i))

    for i in file_lixo:
        i[1] = i[1].lower()
        set2.add(tuple(i))

    return sorted(list(set1), key=lambda x: x[1]), sorted(
        list(set2), key=lambda x: x[1]
    )


def save_file(file, tipo, texto):
    ff = file.split(".")
    txt = ff[-1]
    ff[-1] = tipo
    file = "_".join(ff) + "." + txt

    if os.path.exists(file):
        os.remove(file)

    with open(file, "w", errors="ignore") as fs:
        for element in texto:
            fs.write(f"{element[0]} {element[1]}\n")
