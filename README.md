# Lady Blackbird, une traduction française

Ceci est une traduction personnelle (et qui je l'espère deviendra collective) du jeu de rôle [Lady Blackbird](http://www.onesevendesign.com/ladyblackbird/), par John Harper.

Pour contribuer, vous pouvez [forker ce dépôt sur Github](https://github.com/brunobord/lady-blackbird-fr), ajouter vos modifications sur une branche particulière, et m'adresser des Pull Requests.

Bientôt... on pourra voir le résultat en HTML via les Github Pages. Sois patient.

## Utilisation en local

Prérequis :

* [Sphinx](http://sphinx.pocoo.org),
* [Fabric](http://docs.fabfile.org/) (optionnel, uniquement si on veut avoir un rendu en local)

Cloner le dépôt :

    $ git clone https://github.com/brunobord/lady-blackbird-fr.git

Construire le site en HTML :

    $ make html

Le contenu généré est dans `_build/html`

Pour le voir dans toute sa splendeur :

    $ fab serve

Si on ne dispose pas de Fabric, on peut utiliser tout serveur Web statique imaginable (Apache, Nginx, adsf...)

