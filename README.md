# Pipette.py

Ce projet est un outil de bureau permettant de sélectionner un pixel de l'écran et de récupérer son code couleur dans le presse-papier. Disponible que sur Windows à cause du module "ctypes".


## Installation

Cet outil ne fonctionne que sous Windows. Voici les étapes à suivre pour installer la pipette :
- Déposez le projet en entier dans un dossier de votre ordinateur
- Installez Python 3 et pip sur internet
- Exécutez le fichier "install.bat"
- Laissez le script installer les modules nécessaires
- Une fois les modules installés, vous pouvez fermer la fenêtre lancé par le script
- Vous êtes désormais en mesure d'utiliser "pipette.bat"

Si l'installation de Python 3 ou de pip ne s'est pas bien réalisé, "install.bat" vous l'indiquera dans la fenêtre qui a été ouverte. Dans ce cas là, réinstallez correctement Python 3 et/ou pip.
Si "pipette.bat" retourne une erreur, réessayez de relancer le script ou de réinstaller les modules avec "install.bat".
Si malgré tout ça "pipette.bat" retourne toujours une erreur ou l'outil ne fonctionne pas comme prévu, procurez-vous la version la plus récente disponible en suivant ce lien : [https://github.com/chikatetsu/Pipette](https://github.com/chikatetsu/Pipette)


## Utilisation

Lancez le fichier "pipette.bat". Une fenêtre s'affiche vous demandant d'appuyer sur "Shift" pour récupérer la couleur sous la souris. À chaque appuie sur la touche "Shift", le code hexadécimal de la couleur sélectionné s'affiche dans la fenêtre.
ATTENTION : Pour faciliter l'utilisation de l'outil, le code couleur est conservé dans le presse-papier. Veuillez prendre en compte ce fait en considération afin de ne pas perdre les données précédemment copié dans le presse-papier.
La couleur désormais sélectionné est facilement collable avec "Ctrl+V" ou "Clic droit" puis "Coller". Un historique des couleurs sélectionné est aussi affiché dans la fenêtre de "pipette.bat". Cette historique est perdu une fois que la fenêtre de "pipette.bat" est fermé.
