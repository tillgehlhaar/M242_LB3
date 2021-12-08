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

Wir hatten in der Schule bereits ein Modul in welchen wir einen Raspberry Pi verwendet haben. Dort haben wir bereits ein kleines Projekt mit einem RFID-Scanner umgesetzt, jedoch war dies im ersten Lehrjahr und ich habe nicht mehr sehr viel davon in Erinnerung behalten. Ansosntne habe ich was IoT, Sensoren udn Aktoren angeht wenig erfahrung. Allerdings bin ich wenn es um Services geht besser aufgestellt, da ich in der Freizeit selber gerne Web-Services entwickle und mich mit dem Thema beschäftige. Ebenfalls habe ich auch schon öfters in Modulen in denen es Möglichg war Web-services entwickelt und, oder konzipiert da mich diese Thema sehr stark interessiert.

# Wichtige Lernschritte

## Till

Ich habe gelernt wie man Mikroprozessoren in der Praxis einsetzen kann um einem die Arbeit zu vereinfachen oder wichtige informationen zu liefern, ich kann mir nun besser vorstellen wie ich sie einsetzen könnte oder wo sie industriell verwendet werden. Wie das IOT Board funktioniert und anzusteuern ist, das konfigurieren fiel mir nach eingem ausprobieren des Boards immer leichter.

## Sangeeth

Ich habe am meisten beim Programmieren der Applikation für den Mikroprozessor gelernt. Da ich nur Erfahrung in C# hatte und mir C++ erst einaml für ein par Stunden angeschaut hatte, konnte ich in diesem Modul mein Wissen was C++ betrifft vertiefen. Das was mich am meisten überrascht hat, aber im Nachinein natürlich völlig logisch ist, ist, dass ich das Zertifikat für einen HTTPS Request dem Mikroprozessor übergeben muss, da dieser wie die meisten Betriebssysteme keinen Vorinstallierten Zertifikatsspeicher hat. Ebenfalls konnte ich noch nie einen Load-Balancer konfigurieren und habe somit auch damit in diesem Modul meine ersten Erfahrungen damit gemacht.

# Reflexion

## Till

Das Modul war sehr Spannend. Es hatte Spassgemacht auch mal mit etwas neuem zu arbeiten was ich bisher nicht kannte. Am ersten Tag des Moduls hatte ich gefehlt. Dadurch habe ich viel verpasst


## Sangeeth

Ich denke, ich bin allgemein gut mit meinen Arbeiten für das Modul vorangekommen, hätte aber wahrscheinlich etwas früher die Bewertungskriterien anschauen sollen, da mir aufgefallen ist, dass ich vieles nicht dokumentiert hatte was wir dokumentiert hätten haben sollen. Somit mussten wir vieles 2-Mal machen, da wir es nicht dokumentiert gehabt haben. Ansonsten haben wir gut zusammengearbeitet und sind gut vorangekommen.

# Unser Service

Wir haben uns dafür entschieden den Feuchtigkeits wert mit dem IoT hub zu Messen. Dieser sendet die Daten an einen MQTT Broker. Dieser MQTT Broker ist auf einer lokalen VM Installiert. Per Python Script werden die Daten vom MQTT Broker in eine SQL Datenbank geschrieben welche sich in der Cloud befindet. Mittels Grafan Cloud werden die Daten ausgelesen und Dargestellt. 

## Netzwerkplan

![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/Netzwerkplan.png)

## Grafan Interface

![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/Grafana.png)

# Installations Anleitung


![alt text](https://github.com/tillgehlhaar/M242_LB3/blob/main/RepoClone.png)


