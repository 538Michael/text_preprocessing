# -*- coding: utf-8 -*-
from spacy.lang.pt.stop_words import STOP_WORDS

stop_words1 = open("./TXTs/conectivos.txt", "r")
stop_words2 = open("./TXTs/aurelio_conectivos.txt", "r")

palavras_pequenas = open("./TXTs/PEQUENAS.txt", "r")
substantivos = open("./TXTs/plural_substantivos.txt", "r")
verbos = open("./TXTs/Verbos_conjugados.txt", "r")
arcaismos = open("./TXTs/arcaismos.txt", "r")
nomes_proprios = open("./TXTs/nomes_proprios.txt", "r")


stop_words1 = stop_words1.readlines()
stop_words1 = {palavra.replace("\n", "") for palavra in stop_words1}
stop_words2 = stop_words2.readlines()
stop_words2 = {palavra.replace("\n", "") for palavra in stop_words2}
stop_words = set(list(STOP_WORDS) + list(stop_words1) + list(stop_words2))

nomes_proprios = nomes_proprios.readlines()
nomes_proprios = [nome.replace("\n", "") for nome in nomes_proprios]

palavras_pequenas = palavras_pequenas.readlines()
palavras_pequenas = [palavra.replace("\n", "") for palavra in palavras_pequenas]


arcaismos = arcaismos.readlines()
arcaismos = [palavra.replace("\n", "") for palavra in arcaismos]


substantivos = substantivos.readlines()
substantivos = [palavra.replace("\n", "") for palavra in substantivos]

verbos = verbos.readlines()
verbos = [palavra.replace("\n", "").replace("\ufeff", "") for palavra in verbos]
