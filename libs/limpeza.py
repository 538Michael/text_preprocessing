# -*- coding: utf-8 -*-
import unicodedata
import os
import re

# PASSO 1 - Caracteres especiais
def limpa_caracteres_especiais(texto_file):
    """PASSO 1 - Caracteres especiais"""

    texto_tratado, texto_lixo = list(), set()

    for char in texto_file:
        char=(re.sub('ç','c',char))
        char=(re.sub('Ç','c',char))
        if char.isalpha() or char == '-' or char == ' ' or char == '\n':
            texto_tratado.append(char)
        else:
            texto_lixo.add(char)

    texto_tratado = (''.join(texto_tratado)).replace('\n',' ').replace('  ',' ')
    return texto_tratado, ''.join(texto_lixo)

# PASSO 2 - Palavras pequenas
#def limpa_palavras_pequenas(texto_file, file_pequenos):
def limpa_palavras_pequenas(texto_file, palavras_pequenas):
    """PASSO 2 - Palavras pequenas"""

    texto_limpo, texto_lixo = [], set()

    for char in texto_file.split(' '):
        if len(char) > 3 or char in palavras_pequenas:
            texto_limpo.append(char)
        else:
            texto_lixo.add(char)

    return ' '.join(texto_limpo), ' '.join(texto_lixo)

# PASSO 3 - Acentos
def limpa_sem_acentos(texto_file):
    """PASSO 3 - Acentos"""

    texto = texto_file.split(' ')
    texto_limpo, texto_lixo = [], set()

    for char in texto:
        limpo = True
        normalized = unicodedata.normalize('NFKD', char)
        palavra = []
        for c in normalized:
            #if not unicodedata.combining(c) or c == '̧':
            if not unicodedata.combining(c):
                palavra.append(c)
            else:
                limpo = False
        texto_limpo.append( ''.join(palavra) )
        if not limpo:
            texto_lixo.add(char)

    return ' '.join(texto_limpo), ' '.join(texto_lixo)

# PASSO 4 - ARCAÍSMO
def transforma_texto_arcaismo(texto_file, file_arcaismo):
    """PASSO 4 - ARCAÍSMO"""
    texto = texto_file.split(' ')
    texto_tratado, texto_lixo = [], []

    for char in texto:
        nao_arc = True
        for arcaismo in file_arcaismo:  
            if char.lower() in arcaismo.split(' '):
                texto_lixo.append(char)
                texto_tratado.append(arcaismo.split(' ')[-1])
                nao_arc = False
                break
        if nao_arc:
            texto_tratado.append(char)

    return ' '.join(texto_tratado), ' '.join(texto_lixo)

# PASSO 4 5 - Stopwords
def limpa_stopwords(texto_file, stopwords):
    """PASSO 4 5 - Stopwords"""

    lista = texto_file.split(' ')
    texto_limpo, texto_lixo = [], set()# PASSO 1 - Caracteres especiais

    for char in lista:
        if char[0].isupper() and char in stopwords:
            texto_limpo.append(char)
        elif char not in stopwords:
            texto_limpo.append(char)
        else:
            texto_lixo.add(char)

    return ' '.join(texto_limpo), ' '.join(texto_lixo)


# PASSO 4 5 - Stopwords
def limpa_stopwords2(texto_file, stopwords):
    """PASSO 4 5 - Stopwords"""

    lista = texto_file.split(' ')
    texto_limpo, texto_lixo = [], set()

    for char in lista:
        if char.lower() not in stopwords:
            if char[0].isupper():
                char = char.lower()
                texto_limpo.append( f'{char[0].upper()}{char[1:]}' )
            else:
                texto_limpo.append(char.lower())
        else:
            texto_lixo.add(char)

    return ' '.join(texto_limpo), ' '.join(texto_lixo)


# PASSO 6, 8 - Substantivos
def limpa_substantivos(texto_file, file_substantivos):
    """PASSO 6, 8 - Substantivos"""
    texto = texto_file.split(' ')
    texto_limpo, texto_lixo = set(), []

    for char in texto:
        nao_sub = True
        for substant in file_substantivos:
            if char.lower() in substant.split(' '):
                texto_limpo.add(substant.split(' ')[0])
                nao_sub = False
                break
        if nao_sub:
            texto_lixo.append(char)

    return ' '.join(texto_limpo), ' '.join(texto_lixo)


# PASSO 7 - Verbos
def limpa_texto_verbo(texto_file, file_verbo):
    """PASSO 7 - Verbos"""

    texto_tratado, texto_lixo = set(), []
    for texto in texto_file.split(' '):
        nao_verbo = True
        for verbo in file_verbo:
            verbo = verbo + " "
            if verbo.find(f" {texto.lower()} ") >= 0:
                texto_tratado.add( verbo.split(' ')[0] )
                nao_verbo = False
                break
        if nao_verbo:
            texto_lixo.append(texto)

    return ' '.join(sorted(texto_tratado)), ' '.join(texto_lixo)

# PASSO 10 - ARCAÍSMO
def limpa_texto_arcaismo(texto_file, file_arcaismo):
    """PASSO 10 - ARCAÍSMO"""

    texto = texto_file.split(' ')
    texto_tratado, texto_lixo = [], []

    for char in texto:
        nao_arc = True
        for arcaismo in file_arcaismo:  
            if char.lower() in arcaismo.split(' '):
                texto_tratado.append(arcaismo.split(' ')[-1])
                nao_arc = False
                break
        if nao_arc:
            texto_lixo.append(char)

    return ' '.join(set(texto_tratado)), ' '.join(set(texto_lixo))


# PASSO 10.1 - Nomes proprios
def pega_nomes_proprios(texto_file, file_nomes):
    """PASSO 10.1 - Nomes proprios"""

    texto_limpo, texto_lixo = [], set()

    for char in texto_file.split(' '):
        if char.lower() in file_nomes:
            texto_limpo.append(char)
        else:
            texto_lixo.add(char)

    return ' '.join(texto_limpo), ' '.join(texto_lixo)


# PASSO 11 - JOIN
def limpa_texto_final(file_texto, file_substantivos, file_verbo, file_nomes, file_arcaismo):
    """# PASSO 11 - JOIN"""

    file_limpo = f'{file_substantivos} {file_verbo} {file_nomes} {file_arcaismo}'

    file_lixo = ' '.join( char for char in file_texto.split(' ') if char.lower() not in file_limpo)
    file_lixo =  ' '.join(set(file_lixo.split(' ')))
    return ' '.join(sorted(list(set(file_limpo.split(' '))))), file_lixo


def save_file(file, tipo, texto):
    ff = file.split('.')
    txt = ff[-1]
    ff[-1] = tipo
    file = '_'.join(ff) + '.' + txt

    if os.path.exists(file):
        os.remove(file)

    with open(file , 'w', errors='ignore') as fs:
        fs.write(texto)
