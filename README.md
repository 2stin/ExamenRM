ROUANET Matthieu

Examen v1.0

15/01/2024

Globalement, les tests sont plus concluants dans la version de Turing que dans la version de Steve.

Pour les fonctions décomposer et somme, Steve ne fait aucune vérification tandis que Steve en fait.

Steve : 
Aucune fonction ne passe

Turing :
Fonction décomposer OK
Fonction somme OK (sauf si on rentre un nombre qui n'est pas compris entre 0 et 9, mais étant donné qu'elle dépend de Décomposer, ça ne peut pas arriver)
Fonction divisible OK (sauf si on rentre du texte, mais étant donné qu'elle dépend de Somme, c'est impossible que du texte arrive)

Il y a d'ailleurs une erreur, que j'ai corrigé, dans le code de Turing :

if c>9 or c<0 or d>9 or c<0 or u>9 or u<0: 

à la place de :

if c>9 or c<0 or d>9 or d<0 or u>9 or u<0: 
