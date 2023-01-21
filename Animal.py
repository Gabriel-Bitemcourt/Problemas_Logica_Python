tipo_um = input()
tipo_dois = input()
tipo_tres = input()

if tipo_um == 'vertebrado' and tipo_dois == 'ave' and tipo_tres == 'carnivoro':
    animal = 'aguia'
if tipo_um == 'vertebrado' and tipo_dois == 'ave' and tipo_tres == 'onivoro':
    animal = 'pomba'
if tipo_um == 'vertebrado' and tipo_dois == 'mamifero' and tipo_tres == 'onivoro':
    animal = 'homem'
if tipo_um == 'vertebrado' and tipo_dois == 'mamifero' and tipo_tres == 'herbivoro':
    animal = 'vaca'
if tipo_um == 'invertebrado' and tipo_dois == 'inseto' and tipo_tres == 'hematofago':
    animal = 'pulga'
if tipo_um == 'invertebrado' and tipo_dois == 'inseto' and tipo_tres == 'herbivoro':
    animal = 'lagarta'
if tipo_um == 'invertebrado' and tipo_dois == 'anelideo' and tipo_tres == 'hematofago':
    animal = 'sanguessuga'
if tipo_um == 'invertebrado' and tipo_dois == 'anelideo' and tipo_tres == 'onivoro':
    animal = 'minhoca'
    
print(animal)
