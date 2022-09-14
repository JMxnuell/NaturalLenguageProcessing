import stanza
nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')

texto = """Ocupando sus lugares en el cohete, Neil Armstrong, Edwin Aldrin y 
Michael Collins compartían un vacío en el estómago. Esto era para lo que habían 
entrenado. Estaban listos. Pero la sombra del incendio del Apolo 1 acechaba en 
algún lugar remoto de sus mentes. Era inevitable."""
print(texto)
doc = nlp(texto)

print(*[f'token: {token.text}' for sentence in doc.sentences for token in sentence.tokens], sep='\n')

print(*[f'p: {tok.text+" "}\tlemma: {tok.lemma}' for sent in doc.sentences for tok in sent.words], sep='\n')
