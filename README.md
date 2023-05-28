# udm_param_tuto
# udm_param_tuto

Ce package a pour but d'illustrer l'utilisation du parameter server de ROS.

## Installation
Pour installer ce package, dans le dossier source de votre catkin workspace faire un clone du package:
On supposera que votre catkin workspace s'appelle catkin_ws et se situe dans votre home, remplacer par le bon chemin suivant l'oragnisation de vos dossiers.
```sh
cd catkin_ws/src
git clone https://www.github.com/kramoth/udm_param_tuto.git
```

Puis compiler et sourcer le setup.bash
```sh
catkin build
source ~/catkin_ws/devel/setup.bash
```

## Utilisation

### En utilisant rosrun

#### Publisher
Dans un premier terminal lancer le serveur ROS

```sh
roscore
```

Dans un second terminal
```sh
source ~/catkin_ws/devel/setup.bash
rosrun udm_param_tuto publisher.py _message:="hello world"
```
Dans un troisieme terminal
```sh
rostopic echo /published_topic
```
En modifiant _message le message publie sera modifie

#### Subscriber
Dans un premier terminal lancer le serveur ROS

```sh
roscore
```
Dans un second terminal
```
rosparam set /is_displayed:="true"
source ~/catkin_ws/devel/setup.bash
rosrun udm_param_tuto subscriber.py
```
Dans un troisieme terminal
```sh
rostopic pub /subscribed_topic std_msgs/String "data: 'hi'" 
```

Modifier la valeur du parametre global /is_displayed et relancer le noeud subscriber

### Avec roslaunch

Dans  un terminal
```sh
source catkin_ws/devel/setup.bash
roslaunch udm_param_tuto param_tuto.launch
```
