# CitizenWatt for Raspberry Pi 3

Adaptations pour fonctionner l'application CitizenWatt sur Raspberry Pi 3.  
_Work in progress_ : https://hackpad.com/DAISEE-Installation-CitizenWatt-sur-RPi3-ooSfcWLcyl8    

## Listes des changements  :
* Installation manuelle des packages (mode debug, le temps de stabiliser)  
  
* Ajout de la compilation du package **citizenwatt-visu**  
  
* Remplacement du programme **receive.cpp** par **receive.py**  
impact : utilisation de la [version PINE64+ du **process.py**](https://github.com/DAISEE/CitizenWatt-Base-PINE64/blob/master/process.py) (écriture des data dans un fichier log)  
  
* Utilisation de l'[**Awox SmartPLUG**](http://www.awox.com/awox_product/smartplug/) (connexion BlueTooth) à la place du capteur CitizenWatt  
Utilisation du script [sourceperl/smartplugctl](https://github.com/sourceperl/smartplugctl)  
