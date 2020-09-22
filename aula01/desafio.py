"""
 rot 13 é uma forma clássica de cifrar uma mensagem - consiste em coletar cada caractere
 de uma mensagem e substituí-lo pelo caractere 13 posições à frente. por exemplo:
     a letra 'a' seria convertida em 'n' 
     a letra 'b' seria convertida em 'o'
     e assim por diante...
     Considerando o alfabeto que conhecemos e incluindo os algarismos de 0 até 9:
         - faça uma requisição que colete a mensagem cifrada no seguinte endereço: 
             -> https://python521.herokuapp.com/desafio
         - utilizando a lógica do rot13, decodifique a mensagem que está no campo 'data' do json recebido 
"""

#import requests

#url = "https://python521.herokuapp.com/desafio"

#response = requests.get(url)

#char = response.json()['data']

rot13 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def rot13_decrypt(char):
    new_char = ''
    for c in char.lower():
        if c == ' ':
            new_char += ' '
            continue
        v = rot13.index(c)
        new_char += rot13[v - 13]
    
    return(new_char)


def rot13_encrypt(char):
    new_char = ''
    for c in char.lower():
        if c == ' ':
            new_char += ' '
            continue
        v = rot13.index(c)
        if (v + 13) > (len(rot13) - 1):
            new_char += rot13[((v + 13) - (len(rot13) - 1)) - 1]
            continue
        new_char += rot13[v + 13]
    
    return(new_char)
