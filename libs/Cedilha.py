# -*- coding: utf-8 -*-
import unicodedata
import os
import re

palavra = 'anunciaÇção'
print(palavra)
palavra=(re.sub('ç','c',palavra))
palavra=(re.sub('Ç','c',palavra))
print(palavra)