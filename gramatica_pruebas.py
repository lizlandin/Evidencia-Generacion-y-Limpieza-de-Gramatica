import nltk
from nltk import CFG
from nltk import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

grammar = CFG.fromstring("""
    
    Sentence -> Tail N_Sentence
    N_Sentence -> Conj Tail N_Sentence | 
    Tail -> SimpleSentence
    SimpleSentence -> SubjP ObjP Verb
    
    SubjP -> Pron SubjMarker
    ObjP -> Noun ObjMarker
                         
    Pron -> '나(yo)' | '너(tú)' | '그(él)' | '그녀(ella)' | '우리(nosotros)' 
    SubjMarker -> '는'
    
    Noun -> '피자(pizza)' | '커피(café)' | '영화(película)' | '카메라(cámara)' | '음악(música)'
    ObjMarker -> '를'
    
    Verb -> '먹다(comer)' | '보다(ver)' | '좋아하다(gustar)' | '가지다(tener)' | '듣다(escuchar)' | '마시다(beber)'
    Conj -> '그리고(y)' | '또는(o)' | '하지만(pero)'
""")

# Create a parser with the defined grammar
parser = nltk.ChartParser(grammar)

# Entrada de la cadena que se quiere probar

sentence = input("Ingresa una oración: ")

# Tokenize the sentence
tokens = sentence.split()

# Parsear la oración y verificar si es aceptada o rechazada
try:
    trees = list(parser.parse(tokens))
    
    if trees:
        print("\n✔ La cadena es ACEPTADA\n")
        for tree in trees:
            tree.pretty_print()
    else:
        print("\nx La cadena es RECHAZADA\n")

except:
    print("\n Error al analizar la cadena\n")


#python3 .vscode/gramatica_pruebas.py

