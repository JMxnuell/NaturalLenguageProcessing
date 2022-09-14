import stanza

nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')
doc = nlp('Los trabajadores trabajan mucho.')

for sentence in doc.sentences:
    print(*[f'word: {word.text + " "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
