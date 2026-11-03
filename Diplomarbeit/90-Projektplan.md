# Projekthandbuch
\textauthor{Leitner Nico}

## Änderungsverzeichnis (Projekthandbuch)

| Version | Datum | Status | Beschreibung der Änderung | Autor/in |
| :--- | :--- | :--- | :--- | :--- |
| **1.0** | 2026-06-17 | Freigegeben | **Erstveröffentlichung des Projekthandbuches** | [Leitner] |
| **1.1** | 2026-10-30 | Freigegeben | **Finalisierung und Klarere Formulierungen zu neuen Zielen** | [Leitner] |
| **1.2** | 2026-11-03 | Freigegeben | **Überarbeitung der Anwendungsfälle und Bereinigung der Projektplanvorlage** | [Leitner] |


## Entwicklungsplan

### Projektauftrag

In dieser Diplomarbeit wird der humanoide Roboter PiB (Printable Intelligent Bot) aufgebaut und in Betrieb genommen. Dazu werden die Hardware montiert, die Software mit dem Robot Operating System (ROS) eingerichtet und die Motorik angesteuert. PiB soll den nicht mehr mit Updates versorgten Roboter Pepper als Plattform für den Unterricht, zukünftige Diplomarbeiten und Präsentationen an der HTL Leoben ergänzen.

#### Projektziele

* Hardwarekomponenten aufbauen und zusammensetzen
* PiB-Software und ROS einrichten
* Motorik des Roboters ansteuern
* Bis zu vier Unterrichtseinheiten entwickeln, die grundlegende Prinzipien des Roboters vermitteln

#### Nicht-Ziele

* Gestaltung eines eigenen Logos für den Roboterkörper
* Upgrade auf eine neuere PiB-Version

#### Projektnutzen

PiB schafft an der HTL Leoben eine praktisch nutzbare Plattform für den Robotikunterricht und für zukünftige Diplomarbeiten. Als vorführbarer Open-Source-Roboter macht er technische Inhalte bei Schulveranstaltungen und öffentlichen Präsentationen anschaulich.

#### Projektauftraggeber/in

HTL Leoben

#### Aktueller Projektstatus

Der Gesamtstatus des Projekts liegt aktuell bei "In Arbeit". Stand: 03. November 2026.

Kopf und Oberkörper sind bereits fertiggestellt. Der aktuelle Arbeitsschwerpunkt liegt auf dem Aufbau der Arme; danach folgen die softwareseitige Inbetriebnahme mit ROS, die Ansteuerung der Motorik und die Erstellung von bis zu vier Unterrichtseinheiten.

#### Projekttermine

| Termin     | Inhalt                                      |
|-----------:|:--------------------------------------------|
| 2026-09-30 | Software-Fundament eingerichtet              |
| 2026-10-12 | Kopf & Nacken aufgebaut und kalibriert      |
| 2026-11-03 | Oberkörper montiert                         |
| 2026-12-20 | Hand & Unterarm montiert                    |
| 2027-02-05 | Schulter & Ellbogen aufgebaut               |
| 2027-03-20 | Endmontage (Final Assembly) abgeschlossen  |
| 2027-05-01 | Abschlusspräsentation / Projektdokumentation |

: Projektterminübersicht

#### Projektkosten

Die nachstehende Kostenübersicht dokumentiert den aktuellen Stand der Material-, Druck- und Personalkosten des Projekts. Die Materialkosten werden von der HTL Leoben bereitgestellt; die erfassten Personalkosten zeigen die im Rahmen der Diplomarbeit aufgewendete Arbeitszeit.

| Kategorie & Unterpunkte | Menge / Einheit | Zeitaufwand | Kosten |
|:------------------------|:---------------:|:-----------:|------:|
| Materialkosten | - | - | 4.378,91 € |
| pib.EduBox (non printable parts) | 1 | x | 4.145,00 € |
| PETG White | 5kg | x | 129,95 € |
| PETG Black | 3kg | x | 103,96 € |
| Druckkosten | - | - | 439,43 € |
| Energie | 76,95 kWh | 325h | 26,93 € |
| Personalzeit | ~75 Prints | 18,75h | 412,50 € |
| Personalkosten | - | - | 8.840,00 € |
| Leitner Nico (PM) | 220h | 22€/h | 4.840,00 € |
| Jerebitsch Andre | 200h | 20€/h | 4.000,00 € |
| Gesamtkosten | - | - | 13.658,34 € |

: Projektkostenübersicht

Die Gesamtprojektkosten betragen somit 13.658,34 €.

#### Projektrisiken

Die wesentlichen Projektrisiken und Gegenmaßnahmen sind:

| Risiko         | EW  | Auswirkungen     | Maßnahmen     |
|:--------------:|:---:| :----------------|:--------------|
| Fehldruck beim 3D Print | 5-10% | Neuer Druck, erhöhter Filament und Energieverbrauch, Zeit Plan/Ist Abweichungen | Regelmäßige Wartung des 3D Druckers |
| 3D Drucker fällt aus | 20% | Zeitliche Abweichung für den Druck | Problemquelle Fixen, Mehr Auslastung auf anderen 3D Drucker |
| Ungenaue Schätzungen | 30% | Ungenaue Schätzungen führen zu Problem bezüglich Terminen und Budget. | Schätzungen mit Fachkollegen absprechen|
| Verzögerungen beim Aufbau von Hard- und Software | 10% | Prototyp wird nicht rechtzeitig zur Endpräsentation fertig | Früh genug anfangen |

: Projektrisiken

### Projektteam und Verantwortlichkeiten

#### Projektbeteiligte

| Vorname     | Nachname     | Organisation | Kontaktinfos      |
|:------------|:-------------|:-------------|:------------------|
| André       | Jerebitsch   | HTL Leoben   | 220062@o365.htl-leoben.at  |
| Nico        | Leitner      | HTL Leoben   | 220086@o365.htl-leoben.at, +436766662903  |

: Projektbeteiligte

#### Projektrollen

| Projektrolle           | Rollenbeschreibung     | Name              |
|------------------------|------------------------|-------------------|
| Projektleiter | Verantwortlicher für Einhaltung des Projektrahmens | Nico Leitner |
| Auftraggeber | Auftraggeber der internen Diplomarbeit | HTL Leoben |
| Betreuer | Schulischer Betreuer | G. Hutter |

: Projektrollen

### Änderungsmanagement

Änderungen an Meilensteinen oder Projektumfang werden mit dem Betreuer und den betroffenen Projektbeteiligten abgestimmt. Wesentliche Entscheidungen werden im Änderungsverzeichnis dieses Projekthandbuchs festgehalten; ergänzende Arbeitsschritte und technische Änderungen werden im GitHub-Repository dokumentiert.

## Meilensteine

### 1. 2026-09-30: Software-Fundament eingerichtet

- 1.a Basis-Software für den pib (Betriebssystem und Kern-Pakete) ist aufgesetzt
- 1.b ROS-Umgebung (Robot Operating System) ist erfolgreich initialisiert
- 1.c Erste Verbindungstests zum Steuerungsboard sind positiv verlaufen
- Status: erreicht

### 2. 2026-10-12: Kopf & Nacken aufgebaut und kalibriert

- 2.a Alle 3D-Druckteile für das Gehäuse des Kopfes und die Nackenmechanik sind gedruckt sowie die Elektronikkomponenten geliefert
- 2.b Mechanischer Aufbau des Kopfes sowie der Nackenmechanik ist abgeschlossen
- 2.c Erste Inbetriebnahme der Servomotoren im Kopfsegment ist erfolgt
- 2.d Kalibrierung der Motoren für die Blick- und Kopfbewegungen ist erfolgreich durchgeführt
- Status: erreicht

### 3. 2026-11-03: Oberkörper montiert

- 3.a Die großformatigen Gehäuseteile und inneren Skelett-Strukturen für den Torso sind vollständig gedruckt und einsatzbereit
- 3.b Mechanischer Zusammenbau des Torsos ist abgeschlossen
- 3.c Die stabile Trägerplattform für die Aufnahme von Kopf und Armen ist fertiggestellt
- Status: erreicht

### 4. 2026-12-20: Hand & Unterarm montiert

- 4.a Alle filigranen Fingerglieder, Handflächen- und Unterarm-Strukturen sind fertig gedruckt sowie Sehnen und Motoren bereitgestellt
- 4.b Die einzelnen pib-Finger sind zusammengebaut und funktionell getestet
- 4.c Die Handkonstruktion ist fertiggestellt
- 4.d Der Unterarm ist mechanisch aufgebaut und mit der Hand zusammengeführt
- Status: aktuell in Bearbeitung; Schwerpunkt liegt auf dem Aufbau der Arme

### 5. 2027-02-05: Schulter & Ellbogen aufgebaut

- 5.a Alle 3D-Druckteile für die Schultergelenke, das Ellbogenschnittstellen-Gehäuse und alle Verbindungselemente sind fertig ausgedruckt
- 5.b Mehrachsige Schultergelenke (vertikal und horizontal) sind vollständig montiert
- 5.c Das Ellbogengelenk ist mechanisch aufgebaut
- 5.d Sämtliche Armsegmente sind mechanisch miteinander verbunden
- Status: geplant

### 6. 2027-03-20: Endmontage (Final Assembly) abgeschlossen

- 6.a Alle Hauptbaugruppen (Kopf, Arme und Oberkörper) sind fest miteinander verbunden
- 6.b Die komplette Verkabelung und Elektronik ist im Gehäuse sicher verlegt
- 6.c Der physische Bau des humanoiden Roboters pib ist vollständig abgeschlossen
- Status: geplant

## Anwendungsfälle

Die Anwendungsfälle beschreiben die drei zentralen Einsatzbereiche des Roboters: Unterricht, zukünftige Diplomarbeiten und Präsentationen bei Veranstaltungen.

\newpage
Bei praktischen Vorführungen wird der Roboter vorab vorbereitet und von einer verantwortlichen Person betreut.

### Unterrichtseinheit mit dem Humanoiden Roboter durchführen

#### Kurzbeschreibung
Lehrende setzen den Roboter in einer Unterrichtseinheit ein, um Grundlagen aus Robotik, Mechanik und Software anschaulich zu vermitteln. Die Unterrichtseinheiten können unterschiedliche Themen und Schwierigkeitsstufen abdecken.

#### Trigger
Eine Lehrperson plant eine Unterrichtseinheit oder einen Laborblock zu einem Thema, das anhand des Roboters praktisch veranschaulicht werden kann.

#### Vorbedingung
Der Roboter ist aufgebaut, für die geplante Vorführung betriebsbereit und wird durch eine Lehrperson beaufsichtigt.

#### Nachbedingung
Die Lernenden haben die ausgewählten Grundlagen anhand des Roboters beobachtet oder praktisch erprobt und können die gezeigten Funktionen den zugrunde liegenden Komponenten zuordnen.

#### Akteure
* Lehrperson
* Schülerinnen und Schüler

#### Standardablauf
1. Die Lehrperson wählt ein vorbereitetes Unterrichtsthema aus, zum Beispiel den mechanischen Aufbau, die Motorik oder die softwareseitige Steuerung.
2. Die Lehrperson erklärt die dazugehörigen Bauteile und Abläufe am Roboter.
3. Die Lernenden beobachten eine passende Bewegung oder Funktion und bearbeiten dazu eine praktische Aufgabe.
4. Die Lehrperson bespricht die Ergebnisse und stellt den Bezug zu den vermittelten Grundlagen her.

#### Fehlersituationen
* Der Roboter oder eine benötigte Funktion ist nicht betriebsbereit.
* Die Vorführung muss aus Sicherheits- oder Zeitgründen abgebrochen werden.

#### Systemzustand im Fehlerfall
Die Bewegung wird beendet und der Roboter bleibt ausgeschaltet oder in einem sicheren Zustand. Die Lehrperson setzt die Einheit ohne aktive Bewegung fort oder verschiebt die praktische Vorführung.

### Diplomarbeit auf Basis des Roboters durchführen

#### Kurzbeschreibung
Schülerinnen und Schüler verwenden den Roboter als bestehende Hardware- und Softwareplattform, um in einer zukünftigen Diplomarbeit eine klar abgegrenzte Fragestellung zu untersuchen oder eine Erweiterung zu entwickeln.

#### Trigger
Ein Diplomarbeitsteam wählt ein Thema, für das sich der Roboter als Versuchs- oder Entwicklungsplattform eignet.

#### Vorbedingung
Das Thema ist mit der betreuenden Lehrperson abgestimmt. Das Team kennt die verfügbaren Komponenten und Schnittstellen und darf die geplanten Änderungen am Roboter durchführen.

#### Nachbedingung
Das Team hat die vereinbarte Fragestellung untersucht oder die geplante Erweiterung umgesetzt, getestet und dokumentiert. Der ursprüngliche Roboterzustand ist nachvollziehbar.

#### Akteure
* Diplomarbeitsteam
* Betreuende Lehrperson

#### Standardablauf
1. Das Team formuliert eine Fragestellung oder ein Entwicklungsziel, das auf dem Roboter aufbaut.
2. Das Team stimmt Umfang, Vorgehensweise und Erfolgskriterien mit der betreuenden Lehrperson ab.
3. Das Team untersucht die vorhandene Hardware und Software und plant die erforderlichen Änderungen.
4. Das Team setzt die Arbeit um und erprobt sie unter Aufsicht am Roboter.
5. Das Team wertet die Ergebnisse aus und dokumentiert Änderungen sowie Erkenntnisse.

#### Fehlersituationen
* Eine benötigte Schnittstelle oder Komponente steht nicht zur Verfügung.
* Eine Änderung beeinträchtigt die Funktion des Roboters oder lässt sich nicht zuverlässig testen.

#### Systemzustand im Fehlerfall
Die Erprobung wird beendet. Änderungen werden dokumentiert und, sofern möglich, zurückgenommen, sodass der Roboter wieder in einem sicheren und nachvollziehbaren Zustand ist. Das Team stimmt eine Anpassung des Umfangs mit der betreuenden Lehrperson ab.

### Roboter bei Veranstaltungen präsentieren

#### Kurzbeschreibung
Projektbeteiligte präsentieren den Roboter bei schulischen Veranstaltungen und Messen, um die Robotikarbeit der HTL Leoben zu veranschaulichen und das Interesse an technischen Ausbildungswegen zu fördern.

#### Trigger
Die HTL Leoben nimmt an einer Veranstaltung teil oder organisiert eine Präsentation für Besucherinnen und Besucher.

#### Vorbedingung
Der Roboter ist transportfähig und für die geplante Vorführung vorbereitet. Eine verantwortliche Person betreut den Aufbau und die Demonstration.

#### Nachbedingung
Besucherinnen und Besucher haben den Roboter und dessen Einsatzmöglichkeiten kennengelernt. Interessierte können sich über das Projekt und die technischen Ausbildungsangebote der HTL Leoben informieren.

#### Akteure
* Projektteam
* Besucherinnen und Besucher
* Veranstaltungsorganisation

#### Standardablauf
1. Das Projektteam baut den Roboter am Präsentationsort sicher auf und prüft die geplante Vorführung.
2. Eine betreuende Person stellt den Roboter und das Diplomarbeitsprojekt vor.
3. Das Projektteam zeigt geeignete Funktionen oder Bewegungen und erklärt deren technische Grundlagen.
4. Das Projektteam beantwortet Fragen und informiert über die Ausbildung und weitere Robotikprojekte an der HTL Leoben.
5. Nach der Präsentation wird der Roboter sicher abgeschaltet und abgebaut.

#### Fehlersituationen
* Der Roboter kann am Veranstaltungsort nicht sicher aufgebaut oder betrieben werden.
* Eine Funktion fällt während der Vorführung aus oder die Vorführung muss aus Sicherheitsgründen beendet werden.

#### Systemzustand im Fehlerfall
Die aktive Vorführung wird gestoppt und der Roboter in einen sicheren Zustand versetzt. Das Projektteam setzt die Präsentation anhand von Erklärungen und verfügbaren Unterlagen fort.