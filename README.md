# DataExploration-KLU

> Data Exploration Projekt im 4. Semester im Kurs WWI 20 DSB an der DHBW Mannheim.

Gruppenmitglieder:

- Anh Vu
- Florian Frey
- Frederick Neugebauer
- Olena Lavrikova

---

## Introduction

Das Projektteam beschäftigt sich mit der Stimmungsanalyse auf Tweets zu Videospielen. Das Ziel ist die Benutzerreaktionen zu untersuchen.
Dabei soll ein Modell trainiert werden, welches die Gesamtstimmung erkennt und zusammenfasst.

## Content

Das Repository beinhaltet die Abschlusspräsentation sowie die Dokumentation in PDF-Format. Alle benötigten Datensätze sind in einem Zip-Archiv vorhanden. Weitere Elemente und die Code-Dateien werden im Folgenden näher erläutert.

## Requirements

Es wird eine funktionierende Python 3.x Installation benötigt.
Mit folgendem Befehl können im Terminal, welche das Verzeichnis ausgewählt hat, die benötigten Module installiert werden: `pip install -r requirements.txt`

## Code

Den Quellcode kann in einem Jupyter Notebook ausgeführt werden.
Dieses startet man mit dem Befehl `jupyter notebook` im Terminal oder mit der entsprechenden Erweiterung in Visual Studio Code oder einer anderen Entwicklungsumgebung.

#### **twitter_search_request.ipynb**

Hier werden die API-Requests definiert und ausgeführt. Die Antworten der API werden in einem Verzeichnis _/api_responses_ gespeichert (von Git ignoriert, um Spam zu vermeiden). Eine Beispielresponse ist im Repository als _example_response.json_ zu finden.

#### **tweets_to_excel.ipynb**

Alle Responses im _/api_responses_ Verzeichnis werden hier in eine Excel-Datei zusammengeführt, um sie Labeln und Analysieren zu können.

#### **training_multiclass.ipynb**

Diese Datei beinhaltet den Hauptteil unseres Quellcodes. Hier wird das Datapreprocessing durchgeführt und das Modell auf einem Trainingsdatensatz von Kaggle trainiert und getestet. Anschließend wird es auf unsere Tweets angewendet, um Ergebnisse zu erzielen.

#### **(training_binary.ipynb)**

Erster Versuch des Trainings eines Modells auf einem binären Datensatz. Ähnlich zu dem Training auf dem Multiclass-Datensatz, aber das trainierte Modell wird nicht weiter verwendet.
