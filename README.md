# turtle_regulation_Hurreesing_Jotee

# TP1 Note : Régulation

## Installation
Pour installer ce package, dans le sdossier source de votre catkin workspace, faites un clone de ce package. Si votre catkin workspace s'appelle my_ws, par exemple et se situe dans votre home, utilisez les commandes comme suit:

```
cd my_ws/src
git clone https://github.com/ghurreesing/turtle_regulation_Hurreesing_Jotee.git
```

Ensuite, vous le compilez et sourcez le setup.bash

```
catkin build
source ~/my_ws/devel/setup.bash
```

## Partie 1 : Régulation en cap

### Tester le comportement du noeud avec les différentes valeurs Kp

**Cas 1: Kp forts - valeurs 60 et 50**
Avec les valeurs 50 et 60, la vitesse angulaire du noeud augmente comme l'erreur 'e' augmente aussi comme démontré dans la formule, basée sur la proportionalité de e et Kp dans la formule u = Kp * e. _Alors, les valeurs forts du Kp augmentent la vitesse angulaire du noeud_.

**Cas 2: Kp faibles - valeurs 1, 3 et 5**
La vitesse angulaire du noeud diminue de plus en plus quand on change de valeur 5 à 3 à 1 comme l'erreur 'e' diminue aussi, étant proportionnelle à Kp dans la formule u = Kp * e. _Alors, les valeurs faibles du Kp diminuent la vitesse angulaire du noeud_.

### Utilisation

**Avec Rosrun**
Dans un terminal, vous lancez le serveur avec la commande roscore.
```
roscore
```
Dans un autre terminal, vous faites:
```
rosrun turtlesim turtle_node
```
Vous ouvrez un terminal de nouveau et faites les commandes suivantes:
```
source ~/my_ws/devel/setup.bash
rosrun turtle_regulation_Hurreesing_Jotee set_way_point.py 
```

## Partie 2 : Régulation en distance

Si vous n'avez pas mis fin au lancement de votre serveur avec roscore, vous pouvez exécuter cettte partie avec les commandes qui suivent sans refaire un roscore:

```
source ~/my_ws/devel/setup.bash
rosrun turtle_regulation_Hurreesing_Jotee set_way_point.py
```

**Cas 1: Kpl forts - valeurs 30 et 50**
La vitesse linéaire du noeud augmente lorsqu'on change de valeur 30 à 50 à 1 comme l'erreur 'e1' augmente aussi, étant proportionnelle à Kp dans la formule v = Kpl * e1. _Donc, les valeurs forts du Kpl augmentent la vitesse linéaire du noeud._

**Cas 2: Kpl faibles - valeurs 2, 3, 4 et 5**
En utilisant les valeurs de 2, 3, 4 à 5, la vitesse linéaire du noeud dimininue comme l'erreur 'e1' diminue aussi comme démontré dans la formule, basée sur la proportionalité de e et Kp dans la formule v = Kpl * e1. _Alors, les valeurs faibles du Kpl diminuent la vitesse linéaire du noeud_.
