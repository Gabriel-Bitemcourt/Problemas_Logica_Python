bixo_um = str(input()).lower()
bixo_dois = str(input()).lower()
bixo_tres = str(input()).lower()

if bixo_um == 'vertebrado' and bixo_dois == 'ave' and bixo_tres == 'carnivoro':
    animal = 'aguia'
elif bixo_um == 'vertebrado' and bixo_dois == 'ave' and bixo_tres == 'onivoro':
    animal = 'pomba'
elif bixo_um == 'vertebrado' and bixo_dois == 'mamifero' and bixo_tres == 'onivoro':
    animal = 'homem'
elif bixo_um == 'vertebrado' and bixo_dois == 'mamifero' and bixo_tres == 'herbivoro':
    animal = 'vaca'
elif bixo_um == 'invertebrado' and bixo_dois == 'inseto' and bixo_tres == 'herbivoro':
    animal = 'lagarta'
elif bixo_um == 'invertebrado' and bixo_dois == 'inseto' and bixo_tres == 'hematofago':
    animal = 'pulga'
elif bixo_um == 'invertebrado' and bixo_dois == 'inseto' and bixo_tres == 'herbivoro':
    animal = 'lagarta'
elif bixo_um == 'invertebrado' and bixo_dois == 'anelideo' and bixo_tres == 'hematofago':
    animal = 'sanguessuga'
elif bixo_um == 'invertebrado' and bixo_dois == 'anelideo' and bixo_tres == 'onivoro':
    animal = 'minhoca'

print(animal)