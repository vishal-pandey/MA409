# -*- coding: utf-8 -*-
"""ceaser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FnQxROoJ27c7mVL4M2wWyD-NSOa0pJaT

## Encoding and Decoding using Ceaser
"""

def add(a,b):
    return a+b

add(3,4)

P = " abcdefghijklmnopqrstuvwxyz"
C = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY=3
#p - plaintext
def enc(p):
    c=""
    for x in p:
        pi=P.find(x)
        ci= (pi+KEY) % 27
        c = c + C[ci]
    return c

def dec(c):
    p=""
    for x in c:
        ci=C.find(x)
        pi= (ci-KEY) % 27
        p = p + P[pi]
    return p

enc("hello")

enc("hello dear why are not meeting near sarovar")

dec("KHOORCGHDUCZKACDUHCQRWCPHHWLQJCQHDUCVDURYDU")

