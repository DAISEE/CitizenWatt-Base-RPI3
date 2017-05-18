# CitizenWatt for Raspberry Pi 3

Adaptations pour fonctionner l'application CitizenWatt sur Raspberry Pi 3.  
_Work in progress_ : https://hackpad.com/DAISEE-Installation-CitizenWatt-sur-RPi3-ooSfcWLcyl8    

## Listes des changements  :
* Installation manuelle des packages (mode debug, le temps de stabiliser)  
  
* Ajout de la compilation du package **citizenwatt-visu**  
  
* Compilation d'une librairie RF24 en remplacement du package **librf24-dev**   
Utilisation de la librairie [TMRh20](https://github.com/TMRh20/RF24)  
documentation : http://tmrh20.github.io/RF24/RPi.html  

* Remplacement du programme **receive.cpp** par **receive.py**  
impact : utilisation de la [version PINE64+ du **process.py**](https://github.com/DAISEE/CitizenWatt-Base-PINE64/blob/master/process.py) (écriture des data dans un fichier log)  

## Version pour capteur de courant de type 'invasif'
* La branche '[ina219](https://github.com/DAISEE/CitizenWatt-Base-RPI3/tree/ina219)' comprend les adaptations pour fonctionner avec le capteur de courant [INA219](https://www.adafruit.com/product/904), connecté directement au Raspberry Pi (interface I²C).  
Elle s'appuie sur la librairie [chrisb2/pi_ina219](https://github.com/chrisb2/pi_ina219)
* La branche '[acs712](https://github.com/DAISEE/CitizenWatt-Base-RPI3/tree/acs712)' comprend les adaptations pour fonctionner avec le capteur de courant de type [ACS712](http://www.allegromicro.com/en/Products/Current-Sensor-ICs/Zero-To-Fifty-Amp-Integrated-Conductor-Sensor-ICs/ACS712.aspx), connecté via un Arduino au Raspberry Pi (port serial).  
Le code utilisé par l'Arduino est adapté du [code proposé](http://wiki.mchobby.be/index.php?title=SENSEUR-COURANT-ACS712#Code) par MCHobby.

## Version pour smartplug
La branche '[smartplug](https://github.com/DAISEE/CitizenWatt-Base-RPI3/tree/smartplug)' comprend les adaptations pour fonctionner avec le [Smartplug Bluetooth Awox SMP-B16-FR](https://github.com/sourceperl/smartplugctl).  
