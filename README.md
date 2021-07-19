# RKI-Data-Analyzer (DEPRECATED)

## Ende der Entwicklung

Seit April 2021 findet keine aktive Entwicklung dieses Projekts mehr statt. 

## Ziel

Die Daten zur Corona-Pandemie in Deutschland sollen grafisch aufbereitet werden.
Dabei bietet das Skirpt unterschiedliche Auswertungsmöglichkeiten für Bund,
Länder und Landkreise.

## Daten

Die Daten sind die „Fallzahlen in Deutschland“ des Robert Koch-Institut (RKI)
und stehen unter der Open Data Datenlizenz
Deutschland – Namensnennung – Version 2.0 zur Verfügung
[(Quelle)](https://www.arcgis.com/home/item.html?id=f10774f1c63e40168479a1feb6c7ca74).
Weitere Informationen zur Linzenz können [hier](https://www.govdata.de/dl-de/by-2-0)
abgerufen werden.

Die .csv Datei kann unter dem folgenden Link
heruntergeladen werden: [Link](https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0)



## Funktionsweise

- Die auszuwertende RKI Datei "RKI_COVID19.csv" muss sich im Ordner `./rki_data_analyzer/data/` befinden.
- Der Projektordner verfügt über eine *setup.py* Datei, welche vor der Ausführung von *rki_data_analyzer.py* gestartet werden sollte.
- Die Applikation *rki_data_analyzer* verfügt über ein CLI für die Steuerung.
- **--help** zeigt mögliche Eingaben

## Anpassung der Applikation

Unter `./rki_data_analyzer/` befindet sich die Datei *constants.py*.
Hier kann der Benutzer die Applikation anpassen.
Beispielsweise kann der Nutzer sich für die Darstellung von nur 5 Bundesländern entscheiden.

## Weiterentwicklung

Die Applikation befindet sich in seinen ersten Zügen.
Ich freue mich auf Kommentare, weitere Vorschläge und Verbesserungen.
