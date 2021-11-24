# M242_LB3
von Till und Sangeeth

Hier ist die Dokumentation zum Modul 242 von Sangeeth Sivakumara und Till Gehlhaar

# Inhalt

* [Unser Wissenstand]()
* [Wichtige Lernschritte]()
* [Persönliche Lernentwicklung]()
* [Reflexion]()
* [TechDoc]()

# Unser Wissenstand

## Till

Mit IOT und MCUs habe ich in der Praxis eher weniger Erfahrung. Raspberry pis habe ich schon in der Schule und Privat verwendet und auch schon Sensoren und Aktoren damit angesteuert aber dies war schon vor längerer Zeit. Das Intresse an Iot hatte ich schon länger aber habe mich bis jezt nie in die sache reingestürzt. 

## Sangeeth

Wir hatten in der Schule bereits ein Modul in welchen wir einen Raspberry Pi verwendet haben. Dort haben wir bereits ein kleines Projekt mit einem RFID-Scanner umgesetzt, jedoch war dies im ersten Lehrjahr und ich habe nicht mehr sehr viel davon in Erinnerung behalten. Ansosntne habe ich was IoT, Sensoren udn Aktoren angeht wenig erfahrung. Allerdings bin ich wenn es um Services geht besser aufgestellt, da ich in der Freizeit selber gerne Web-Services entwickle und mich mit dem Thema beschäftige. Ebenfalls habe ich auch schon öfters in Modulen in denen es Möglichg war Web-services entwickelt und, oder konzipiert da mich diese Thema sehr stark interessiert.

# Wichtige Lernschritte

## Till

Ich habe gelernt wie man Mikroprozessoren in der Praxis einsetzen kann um einem die Arbeit zu vereinfachen oder wichtige informationen zu liefern, ich kann mir nun besser vorstellen wie ich sie einsetzen könnte oder wo sie industriell verwendet werden. Wie das IOT Board funktioniert und anzusteuern ist, das konfigurieren fiel mir nach eingem ausprobieren des Boards immer leichter.

## Gehlhaar

Ich habe am meisten beim Programmieren der Applikation für den Mikroprozessor gelernt. Da ich nur Erfahrung in C# hatte und mir C++ erst einaml für ein par Stunden angeschaut hatte, konnte ich in diesem Modul mein Wissen was C++ betrifft vertiefen. Das was mich am meisten überrascht hat, aber im Nachinein natürlich völlig logisch ist, ist, dass ich das Zertifikat für einen HTTPS Request dem Mikroprozessor übergeben muss, da dieser wie die meisten Betriebssysteme keinen Vorinstallierten Zertifikatsspeicher hat. Ebenfalls konnte ich noch nie einen Load-Balancer konfigurieren und habe somit auch damit in diesem Modul meine ersten Erfahrungen damit gemacht.


# Persönliche Lernentwicklung

## Till

Ich habe vorallem gelernt mit Mikroprozessoren funktionieren und ich sie ansteuern kann sowie für was sie eigentlich verwendet werden neben hobby basteleien.
Da ich kaum Programmiere habe ich bei der änderung von Programmen für das Iot Board einiges neues gelernt.

## Sangeeth

Ich habe in diesem Modul vieles über Mikroprozessoren gelernt, dazu gehören:

- Mikroprozessor vs CPU
- Programmieren eines Mikroprozessors
- Anwendungsgebiete von Mikroprozessoren
- Man kann selbst Mikroprozessoren designen und drucken lassen
- Mikroprozessoren haben keinen Certificate-Store 🙄

Auch habe ich etwas über nginx gelernt, obwohl ich diesen Dienst schon lange benutze:

- Nginx als Load balancer

Auch konnte ich noch einiges über das Prinzip Laod Balancer lernen:

- Prinzipien wie Round-Robin, least connected
- IP Hash bei Laod Balancing
- Sessionhandling einer Applikation muss beim load-balancing angepasst werden

# Reflexion

## Till

Ich fand es spannend mal mit solchen Board zu arbeiten. Werde definitif in Zukunft etwas mehr mit IOT Geräten arbeiten jedoch aktuell eher im Privatem rahmen. 
Das das ganze Modul von zuhause aus gemacht werden musste hat etwas bedrückt.
Ich konnte einiges neues in diesem Modul lernen.


## Sangeeth

Ich denke, ich bin allgemein gut mit meinen Arbeiten für das Modul vorangekommen, hätte aber wahrscheinlich etwas früher die Bewertungskriterien anschauen sollen, da mir aufgefallen ist, dass ich vieles nicht dokumentiert hatte was wir dokumentiert hätten haben sollen. Somit mussten wir vieles 2-Mal machen, da wir es nicht dokumentiert gehabt haben. Ansonsten haben wir gut zusammengearbeitet und sind gut vorangekommen.

# Unser Service

Wir haben uns dafür entschieden einen Temperatur-Alarm mit dem IoT-Board umzusetzen. Das bedeutet, dass wir die Temperatur mittels des Sensors auf dem Board lesen und dann per REST API an eine Web-App übermitteln wollen.

Die Web-App ist für das logging der Einträge verantwortlich. Ausserdem kann über die Web-App ein Temperaturberich festgelegt werden. Bei allen Temperaturen, die ausserhalb dieses Bereiches liegen, wird "Alarm" geschalgen.

Der Alarm, zeigt sich ersten indem die Temperaturanzeige in der Web-App Rot angezegit wird und zweitens auf dem Board ein entsprechendes LED eingeschaltet wird. Ebenfalls wird auch auf dem OLED-Display eine NAchricht ausgegeben die zeigt, was der Feherl nun genau bedeutet.

Weitere Informationen zu den Error-States finden Sie [hier](https://github.com/SayHeyD/M242/tree/main/IoTKitv3#Error-States).

