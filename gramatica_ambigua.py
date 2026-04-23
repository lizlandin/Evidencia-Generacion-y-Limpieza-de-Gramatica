import nltk
from nltk import CFG
from nltk import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

# Define a context-free grammar
grammar = CFG.fromstring("""
    
    Sentence -> Sentence Conj Sentence | SimpleSentence
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

# Input sentence to be parsed
sentence = "나(yo) 는 피자(pizza) 를 먹다(comer) 그리고(y) 그(él) 는 커피(café) 를 마시다(beber) 그리고(y) 우리(nosotros) 는 음악(música) 를 듣다(escuchar)"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()

#python3 .vscode/gramatica.py
