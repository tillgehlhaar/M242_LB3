# M242_LB3
von Till und Sangeeth

Hier ist die Dokumentation zum Modul 242 von Sangeeth Sivakumaran und Till Gehlhaar

# Inhalt

* [Unser Wissenstand](https://github.com/tillgehlhaar/M242_LB3/blob/main/README.md#unser-wissenstand)
* [Wichtige Lernschritte](https://github.com/tillgehlhaar/M242_LB3/blob/main/README.md#wichtige-lernschritte)
* [Reflexion](https://github.com/tillgehlhaar/M242_LB3/blob/main/README.md#reflexion)
* [Unser Service](https://github.com/tillgehlhaar/M242_LB3/blob/main/README.md#unser-service)
* [Installations Anleitung](https://github.com/tillgehlhaar/M242_LB3/blob/main/README.md#installations-anleitung)

# Unser Wissenstand

## Till

Mit IoT geräten und vorallem MCUs hatte ich bisher eigneltich noch gar nichts zu tuen. Ich habe in einem anderen Modul bereits einmalig mit einem Raspberry Pi gearbietet. Das wars aber auch schon. Verschiedene Iot geräte nutze ich täglich im Smarthome bereich. Mit Cloud Services hatte ich beriets häufiger zu tuen. 

## Sangeeth

Wir hatten in der Schule bereits ein Modul in welchen wir einen Raspberry Pi verwendet haben. Dort haben wir bereits ein kleines Projekt mit einer Kamera und einem Bewegungssensor umgesetzt, jedoch war dies im zweiten Lehrjahr. Ansosntne habe ich was IoT, Sensoren udn Aktoren angeht wenig Erfahrung. Allerdings bin ich wenn es um Services geht besser aufgestellt, da ich im Betrieb so sachen mache.

# Wichtige Lernschritte

## Till

Ich habe gelernt wie man Mikroprozessoren in der Praxis einsetzen kann um einem die Arbeit zu vereinfachen oder wichtige informationen zu liefern, ich kann mir nun besser vorstellen wie ich sie einsetzen könnte oder wo sie industriell verwendet werden. Wie das IOT Board funktioniert und anzusteuern ist, das konfigurieren fiel mir nach eingem ausprobieren des Boards immer leichter.

## Sangeeth

Am meisten gelernt habe ich bei der Programmierung der Anwendung für den Mikroprozessor. Da ich nur Erfahrung mit C# hatte und mich nur ein paar Stunden mit C++ beschäftigt hatte, konnte ich in diesem Modul mein Wissen über C++ vertiefen. 

# Reflexion

## Till

Das Modul war sehr Spannend. Es hatte Spassgemacht auch mal mit etwas neuem zu arbeiten was ich bisher nicht kannte. Am ersten Tag des Moduls hatte ich gefehlt. Dadurch habe ich viel verpasst. Sangeeth konnte mir aber gut helfen und er hat mir einiges gezeigt. Ich habe viel herumprobiert. Die Dokumentation haben wir etwas vernachlässigt, was man teilweise auch sehen kann. 


## Sangeeth

Ich denke, ich bin allgemein gut mit meinen Arbeiten für das Modul vorangekommen, hätte aber wahrscheinlich etwas früher die Bewertungskriterien anschauen sollen, da mir aufgefallen ist, dass ich vieles nicht dokumentiert hatte was wir dokumentiert hätten haben sollen. Somit mussten wir vieles 2-Mal machen, da wir es nicht dokumentiert gehabt haben. Ansonsten haben wir gut zusammengearbeitet und sind gut vorangekommen.

# Unser Service

Wir haben uns dafür entschieden den Feuchtigkeits unt Temparaturs wert mit dem IoT hub zu Messen. Dieser sendet die Daten an einen MQTT Broker. Dieser MQTT Broker ist auf einer lokalen VM Installiert. Per Python Script werden die Daten vom MQTT Broker in eine SQL Datenbank geschrieben welche sich in der Cloud befindet. Mittels Grafan Cloud werden die Daten ausgelesen und Dargestellt. 

## Netzwerkplan

![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/Netzwerkplan.png)

## Grafan Interface

![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/Grafana.png)

# Installations Anleitung

1. Als erstes Git Repository in Lokalen Ordner Clonen.
 
![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/RepoClone.png)

2. Mittels geclontem Vagrant File lokale VM erstellen welche als MQTT Host Dient. (MQTT wird autmaitsch mit Installiert)

![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/VagrantUP.png)

3. Im Mbed Studio neues Programm Importieren. URL: (https://github.com/tillgehlhaar/M242_LB3/tree/main/mqtt)
 
![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/MbedImport.png)

4. Nun muss noch folgendes Script auf den MQTT host kopiert werden. Am besten ins directory: logger
 
![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/PythonScript.png)

In diesem Python Script ist angegeben an welchen DB Server und mit welchen Zugangsdaten sich der MQTT connected. Das Script erstellt auf dem Datenbankserver eine neue Datenbank mit den nötigen Tabellen. Danach werden die Daten entsprechend übermittelt und in die Tabellen geschrieben. 

5. Auf der VM müssen nun noch folgende Befehle abgesetzt werden:
   * cd logger/
   * sudo nano mqtt_to_mysql.py
   * python3 mqtt_to_mysql.py

6. Den Datenbankserver haben wir in der Cloud. Wir haben bei (https://www.freesqldatabase.com/) ein Gratis Account erstellt und somit zugang einer Gratis DB erhalten. Man kriegt dann ein Server Adrese mit Benutzer und Passwort welche wir entsprechend im PythonScript verwenden.  
 
![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/MySQL.png)

7. Mittel dem Online Tool Grafana haben wir ein Dashboard erstellt welches die Daten aus der Datenbank hohlt und schlussendlich Darstellt. Die Datenbank wurde folgendermassen eingebunden. 

![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/GrafanaConfig.png)





