# DataExploration-KLU
***
## Introduction
Das Projekt Karl Lauterbach Researchs besteht aus vier Mitglieder: <br/>
Florian Frey, Frederick Neugebauer, Anh Vu, Olena Lavrikova.<br/>
Das Projektteam beschäftigt sich mit der Stimmungsanalyse auf Twitter Daten. Das Ziel ist die Benutzerreaktionen zu untersuchen. 
Dabei soll ein Algorithmus entwickelt werden, der die Gesamtstimmung erkennt und zusammenfasst. Wir beschäftigen uns mit Twitter Reaktionen zu den bekannten Spielen XXX und XXX.  

## Installation

```
import zipfile
import pandas as pd
# import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download('punkt')
# nltk.download('omw-1.4')
# nltk.download('stopwords')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

```

## Quellcode Ausführung
