# Korpus mit Schubladen – Projektnotizen

Schubladenkorpus aus Eichen-Leimholz, von Hand gebaut, für unter das Pult (Rückwand sichtbar).
FreeCAD-Modell: `Korpus.FCStd` – alle Masse kommen aus dem **Spreadsheet** und lassen sich dort ändern.

Stand: 22.10.2026

---

## 1. Hauptmasse

| Wert (Spreadsheet) | Mass | Bemerkung |
|---|---|---|
| `TotalHeight` | 580 mm | Gesamthöhe inkl. Füsse |
| `FeetHeight` | 40 mm | Höhe des Sockels (siehe Abschnitt 7) |
| `BodyHeight` | 540 mm | Korpushöhe, wird berechnet (`TotalHeight − FeetHeight`) |
| `BodyWidth` × `BodyDepth` | 400 × 400 mm | |
| `Wall` | 18 mm | Plattenstärke = Eichen-Leimholz aus dem Baumarkt (Bauhaus/Jumbo) |
| `DrawerCount` | 4 | |
| `DrawerGap` | 3 mm | Fuge ringsum, überall gleich |
| `DrawerHeight` | 122.25 mm | Fronthöhe, wird berechnet |

- Lichte Öffnung: 364 × 504 mm
- Schubladenfronten: 358 × 122.25 × 18 mm, einliegend, bündig mit der Korpusvorderkante
- Innentiefe bis Rückwand: 382 mm → für die Schubladenkästen berücksichtigen

## 2. Material & Grundsätze

- **Eichen-Leimholz 18 mm** für alles. Auf 15 mm hobeln wurde verworfen: zu viel Handarbeit, und die Faser wechselt bei Leimholz von Lamelle zu Lamelle.
- **Holzbewegung:** Quer zur Faser arbeitet Eiche um etwa 1 % zwischen Winter und Sommer. Längs zur Faser bewegt sie sich praktisch nicht.
- **Faserrichtung:**
  - Seiten: Faser senkrecht.
  - Ober- und Unterseite: Faser links–rechts.
  - Schubladenfronten: Faser waagrecht.
  - Rückwand: Faser **senkrecht**.

## 3. Fugen

- **3 mm** ringsum: zum Korpus und zwischen den Schubladen.
- **Begründung:**
  - Die Fronten quellen in der Höhe, quer zur Faser, um bis zu etwa 1 mm pro Front, insgesamt bis zu etwa 4 mm auf 5 Fugen.
  - Die Öffnung bleibt gleich hoch, weil die Seiten senkrechte Faser haben.
  - Bei 3 mm bleibt auch im feuchten Sommer genug Luft. Weniger als 2.5 mm ist nicht empfehlenswert.
- **Seitliche Fugen:** Sie sind in der Breite unkritisch, weil dort alles längs zur Faser läuft.
- **Einpassen:** im trockenen Winter mit etwas mehr Luft, im feuchten Sommer knapper.

## 4. Korpus-Konstruktion

- Unterseite und Oberseite laufen über die ganze Breite, die Seiten stehen dazwischen.
- **Im Modell:**
  - Die Oberseite ist ein Link der Unterseite, die rechte Seite ein Link der linken Seite.
  - Beide Links sind um 180° um die Tiefenachse gedreht. Dadurch liegen die Nuten auch beim Gegenstück innen, und Änderungen an der Unterseite bzw. der linken Seite gelten automatisch für beide Teile.

### Eckverbindung: stumpf mit Dübeln (entschieden)

| Wert (Spreadsheet) | Mass | Bemerkung |
|---|---|---|
| `DowelDiameter` × `DowelLength` | 8 × 35 mm | Riffeldübel |
| `DowelDepthPanel` | 12 mm | Lochtiefe in Ober- und Unterseite, 6 mm Restmaterial |
| `DowelDepthSide` | 25 mm | Lochtiefe im Hirnholz der Seite, berechnet (`DowelLength − DowelDepthPanel + 2 mm`). Die 2 mm Luft nehmen überschüssigen Leim auf. |
| `DowelCount` | 6 | pro Ecke |
| `DowelFromFront` / `DowelFromBack` | 30 / 50 mm | Abstand der Dübelmitte zur Vorder- bzw. Hinterkante. Hinten genug Abstand zur Rückwand-Nut. Ergibt ein Raster von 64 mm. |
| `DowelInset` | 9 mm | `= Wall / 2`, mittig in der Seite |

- **Begründung:**
  - Seitlich sieht man oben und unten je einen 18 mm Hirnholzstreifen von Ober- und Unterseite. Das ist schlicht und ehrlich, typisch Shaker.
  - Alle vier Teile arbeiten in der Tiefe, also gleich gerichtet. Die Dübelreihe läuft von vorne nach hinten und bewegt sich mit.
  - Mit Bohrmaschine und einer selbstzentrierenden Dübellehre gut machbar.
- **Verleimen in zwei Etappen** (möglich, weil die Rückwand-Nut in den Seiten durchläuft):
  1. Unterseite und beide Seiten verleimen und rechtwinklig spannen, z.B. mit einer trocken eingesetzten Hilfsplatte oben.
  2. Die Rückwand von oben in die Nuten der Seiten einschieben, bis sie in der Nut der Unterseite sitzt. Nicht verleimen (siehe Abschnitt 5).
  3. Die Oberseite senkrecht auf Dübel und Rückwand-Feder aufsetzen und verleimen.
  - So sind nie mehr als zwei Ecken gleichzeitig unter Zeitdruck.
- **Im Modell:**
  - Die Dübellöcher sind in der Unterseite und der linken Seite modelliert, als Pocket mit Linear-Muster.
  - Oberseite und rechte Seite übernehmen sie über die Links.
  - Die Dübel selbst sind nicht dargestellt.
- **Verworfene Varianten:**
  - **Gehrung:** Die 400 mm lange Hirnholz-Gehrung wäre das riskanteste Detail am Möbel.
    - Eine Eselsohr-Stosslade müsste eine Hobelbahn von 450–500 mm haben, und die schweren Seiten würden schräg wegragen.
    - Schon ein Fehler von 0.5° pro Teil ergibt ca. 0.4 mm Spalt.
    - Eine reine Gehrung hält kaum (Hirnholz auf Hirnholz) und bräuchte eine Verstärkung. Eine Feder in der 45°-Fläche ist von Hand heikel, und Leimklötze innen ragen in den Schubladenraum.
  - **Gehrung mit eingesetzten Keilen** (*mitre keys*): Im Muster angeschaut, optisch nicht gefallen.
  - **Halbverdeckte Zinken** bzw. **Zinken mit Gehrungsabschluss** (*mitred through dovetail*): schön, aber viel Arbeit. Vier Ecken auf einmal zusammenzubringen ist anspruchsvoll; schon die offenen Zinken am Schuhgestell waren es.

### Kanten vorne
- Die **äusseren** Vorderkanten des Korpus sind mit **Radius 3 mm** gerundet (`FrontRadius`). Die Rundung läuft rundum wie ein Bilderrahmen, auch über die kurzen Stirnkanten von Ober- und Unterseite.
- Alle übrigen Kanten nur ca. 1 mm brechen (im Modell nicht dargestellt).
- **Verworfene bzw. alternative Varianten:**
  - Fase 6 mm unter 45°, aussen: wirkt schlanker, aber modern. Wurde zugunsten der Rundung verworfen.
  - Auslaufende Fase (Stopfase) wie bei Arts & Crafts / Gimson: noch nicht ausprobiert.
- **Von Hand runden:**
  1. 3 mm mit dem Bleistift anreissen.
  2. Eine 45°-Fase hobeln.
  3. Die Fasenkanten nochmals leicht brechen, so dass ein Achteck entsteht.
  4. Mit Ziehklinge oder Schleifpapier auf einem Korkklotz verrunden.
  - Immer zuerst die Hirnholzkanten bearbeiten, dann die Längskanten.

## 5. Rückwand – abgeplattete Füllung (Variante B, ohne Absatz)

Sichtbare Rückwand aus dem gleichen Eichen-Leimholz, schwimmend in einer Nut.

| Wert | Mass | Bemerkung |
|---|---|---|
| `BackpanelThickness` | 18 mm | volle Plattenstärke im Spiegel |
| `BackpanelTongue` | 8 mm | Feder, also der verdünnte Rand. Gleich der Nutbreite. |
| `BackpanelNut` | 8 mm | Nuttiefe |
| `BackpanelPlay` | 2 mm | Spiel im Nutgrund pro Seite, für die Holzbewegung |
| `BackpanelBevel` | 40 mm | Breite der Abplattung, von der Nutkante bis zum Spiegel |
| `BackpanelSpacing` | **0 mm** | Spiegel **bündig** mit der Hinterkante des Korpus |

- **Rückwand:** 376 × 516 × 18 mm.
  - Die Feder (8 mm) liegt **innen bündig**.
  - Aussen steigt die Abplattung über 40 mm von 8 auf 18 mm an, das sind etwa 14°.
- **Nut:** 8 × 8 mm, mit 10 mm Material bis zur Hinterkante.
  - In den Seiten läuft sie **durch**; die Enden sind durch Ober- und Unterseite verdeckt.
  - In Ober- und Unterseite ist sie **gestoppt**, damit sie aussen nicht sichtbar ist.
- **Nicht verleimen.** Höchstens ein Leimpunkt oder Stift in der Mitte oben und unten, damit die Rückwand zentriert bleibt.
- Die Rückwand muss **beim Verleimen des Korpus** eingesetzt werden.

### Bündiger Spiegel – worauf achten
- Ein bündiger Spiegel verzeiht nichts. 1 mm Versatz oder eine leicht gewölbte Platte sehen sofort wie ein Fehler aus.
- Faustregel: **entweder klar bündig oder klar zurückgesetzt (≥ 4–5 mm)**, nichts dazwischen.
- **Alternative `BackpanelSpacing = 5 mm`:** Diese Variante **verzeiht mehr**.
  - Kleine Abweichungen in Plattendicke, Nutposition oder Wölbung fallen bei einem klaren Rücksprung kaum auf.
  - Hinter der Nut bleiben dann 15 statt 10 mm Material, das ist robuster.
  - Optisch wirkt die Füllung zurückgesetzt, am Rand ist sie 15 mm tief.
  - Im Modell genügt es, den Wert im Spreadsheet zu ändern.
- **Tipp:** Zuerst die Rückwand fertig abplatten. Dann die Nutposition **direkt an der fertigen Platte** anreissen, nicht nach Plan. So gleichst du die tatsächliche Dicke aus.
- Nach dem Verleimen lässt sich der Spiegel nicht mehr bündig nachhobeln, weil die Rückwand schwimmt.

### Herstellung
- **Abplattung:** mit Simshobel bzw. Blockhobel. Zuerst die Hirnholzkanten oben und unten, dann die Längskanten; so verschwinden Ausrisse an den Ecken.
- **Nuten:** mit dem Nuthobel.
  - Die gestoppten Nuten in Ober- und Unterseite brauchen Vorarbeit: die Enden zuerst mit dem Stechbeitel ausstechen, damit der Hobel einen Auslauf hat.
  - Quer zur Faser braucht der Nuthobel Vorschneider.

## 6. Griffe

### Favorit: Flache Eichenleiste, mit Eisenacetat geschwärzt
- **Form:**
  - 120 mm lang, 15 mm hoch, 12 mm vorstehend.
  - Die Unterseite ist unter ca. 30° gegen die Front abgeschrägt, so dass die Finger von unten greifen.
  - 8 mm Leimfläche an der Front.
  - Vordere Längskanten mit r ≈ 1.5 mm gerundet.
- **Lage:** mittig auf der Front (`HandleFromTop`). Für das obere Drittel `HandleFromTop` auf ca. 30 mm setzen.
- **Befestigung:** vollflächig verleimt, zusätzlich 2 Schrauben von hinten. Die Faser läuft gleich wie bei der Front, es gibt also kein Problem mit der Holzbewegung.
  - **Die Griffe anbringen, bevor die Front am Schubladenkasten befestigt wird.**
- **Herstellung:**
  1. Einen langen Eichenstab hobeln, ca. 550 mm für 4 Griffe plus Reserve. Das kann ein Reststück der Leimholzplatte sein.
  2. Die Schräge auf der ganzen Länge mit dem Hobel anarbeiten.
  3. Die Kanten brechen.
  4. Ablängen und die Enden sauber machen.

### Eisenacetat (Eiche schwärzen)
- **Ansetzen:** Feine Stahlwolle (z.B. 0000), **entfettet**, in Haushaltsessig legen. Das Glas nur locker abdecken, nicht verschliessen, weil Gas entsteht. Ein paar Tage stehen lassen, dann abfiltern.
- **Wie es wirkt:** Die Lösung reagiert mit der **Gerbsäure der Eiche**. Das Holz wird tief grau bis schwarz, und zwar im Holz selbst. Die Maserung bleibt sichtbar.
- **Mehrere Durchgänge** machen es dunkler. Ein Tee-Vorstrich (Schwarztee, ebenfalls gerbsäurehaltig) verstärkt die Wirkung.
- **Zuerst an einem Reststück testen!** Der Ton hängt vom Holz, von der Konzentration und von der Einwirkzeit ab.
- **Vor dem Ölen** vollständig trocknen lassen. Die Griffe am besten **vor der Montage** schwärzen, damit nichts auf die helle Front gelangt.
- **Funktioniert nicht bei Buche**, weil sie kaum Gerbsäure hat.

### Weitere Varianten (im Modell bzw. besprochen)
| Variante | Status | Bemerkung |
|---|---|---|
| Flache Leiste aus Eiche, geschwärzt (Favorit) | im Modell als «Griff Eiche geschwärzt» | siehe oben |
| Flache Leiste aus Nussbaum | gleiche Form wie oben, nur anderes Holz | Nussbaum-Reste gibt es günstig in Schreinereien |
| Gedrechselter Knopf, gekauft, Ø 25 mm | im Modell als «Knopf Nussbaum» | klassisch Shaker, bei 358 mm Frontbreite **ein** Knopf mittig. Masse an den gekauften Knopf anpassen. |
| Leiste aus Eiche natur | Alternative | ruhig und einheitlich, passt sehr gut zu Shaker |
| Buche gedämpft | eher nicht | ähnlich hell wie Eiche, rosa Unterton, zu wenig Kontrast; wirkt «knapp daneben» |
| Brückengriff mit Füssen | verworfen | |
| Griffausschnitt Oberkante, Bogen bzw. rechteckig | verworfen | |
| Eingesetzte Nussbaum-Griffkante | nicht weiterverfolgt | sehr elegant, aber anspruchsvolle Passarbeit |

Im FreeCAD-Baum unter **Schublade** lassen sich Griff und Knopf mit der **Leertaste** ein- und ausblenden. Das Array übernimmt das für alle Schubladen.

## 7. Sockel (Unterbau)

Inspiration: Teak-Kommode von Børge Mogensen (60er-Jahre). Der Sockel ist nach innen versetzt, aus dem gleichen Material wie der Korpus, die Ecken leicht gerundet.

| Wert (Spreadsheet) | Mass | Bemerkung |
|---|---|---|
| `FeetHeight` | 40 mm | Sockelhöhe. 75 mm wirkte zu mächtig. |
| `PlinthInsetFront` | 20 mm | Rücksprung vorne (Schattenfuge, Korpus wirkt leichter) |
| `PlinthInsetSide` | `= PlinthInsetBack` (10 mm) | Rücksprung seitlich, gleich wie hinten |
| `PlinthInsetBack` | `= BackpanelSpacing + BackpanelThickness − BackpanelTongue` (10 mm) | = Material hinter der Rückwand-Nut. Das hintere Sockelteil fluchtet mit der hinteren Nutwand und stützt die Unterseite dort, wo sie nur 10 mm dick ist. Bei `BackpanelSpacing = 5 mm` werden es automatisch 15 mm. |
| `PlinthRadius` | 6 mm | senkrechte Aussenecken gerundet |
| `PlinthThickness` | `= Wall` | 18 mm Eichen-Leimholz |

- Sockelrahmen aussen: 380 × 370 × 40 mm (Breite × Tiefe × Höhe).
- Wie bei Mogensen ist er vorne stärker zurückgesetzt als seitlich und hinten. **Nicht ganz bündig** (0 mm) machen: Wie beim Spiegel der Rückwand verzeiht bündig nichts.
- Faser bei allen vier Teilen waagrecht. Sie arbeiten daher nur in der Höhe (ca. 0.4 mm auf 40 mm); die Ecken bleiben geschlossen.
- **Im Modell** (Gruppe «Sockel»):
  - Vier Rahmenteile mit Gehrung. «Sockel hinten» ist ein Link von «Sockel vorne», «Sockel rechts» ein Link von «Sockel links», jeweils um 180° bzw. 90° gedreht. Änderungen gelten automatisch für beide Teile.
  - Leimklötze in den vier Ecken, Festpunkte in der Mitte der Seiten, vier Nutklötze mit Schlitzen in den Teilen vorne und hinten. Alle Masse im Spreadsheet (Zeilen 27–43).

| Teil | Anzahl | Mass (aussen) | Bemerkung |
|---|---|---|---|
| Sockel vorne/hinten | 2 | 380 × 40 × 18 mm | `PlinthLengthFront`, beidseitig Gehrung, je 2 Schlitze |
| Sockel seitlich | 2 | 370 × 40 × 18 mm | `PlinthLengthSide`, beidseitig Gehrung |
| Leimklotz Ecke | 4 | 18 × 18 × 36 mm | 2 mm Luft oben und unten (`PlinthBlockGap`), berührt den Korpus nicht |
| Festpunkt | 2 | 18 × 30 × 20 mm | oben bündig, an die Seite geleimt, an die Unterseite geschraubt. Loch Ø 4.5 mm mit Ansenkung Ø 10 × 8 mm von unten, Schraube 4 × 25 (ca. 13 mm in der Unterseite) |
| Nutklotz | 4 | 18 × 40 × 14 mm | Lippe 8 × 5 mm, 1 mm Anzug, 3 mm Luft im Nutgrund. Loch Ø 4.5 mm mit Senkung 90° von unten, Senkkopfschraube 4 × 25 (ca. 11 mm in der Unterseite) |

### Eckverbindung
- **Favorit: Gehrung mit Leimklotz.**
  - **Sägen:** mit der Tauchsäge an der Führungsschiene, auf 45° geschwenkt, ca. 0.5 mm Übermass.
    - Zuerst den Winkel an vier Probestücken prüfen und trocken zusammenstellen. Der 45°-Anschlag der Säge ist selten ganz genau, und jeder Fehler kommt an jeder Ecke doppelt vor.
    - Alle vier Teile nebeneinander unter die Schiene spannen, beidseitig ein Opferstück. So liegt die Schiene satt auf, und die gegenüberliegenden Teile werden gleich lang.
    - Ausrisse: Bei geschwenkter Säge schützt der Splitterschutz nicht ganz. Am Probestück prüfen, welche Seite sauber bleibt, und die Sichtseite dorthin legen.
  - **Nachstossen:** auf einer **Eselsohr-Stosslade** (*donkey ear shooting board*). Das Teil liegt flach am 90°-Anschlag, der Hobel läuft auf einer 45°-Rampe. Die Gehrungsfläche ist nur 25.5 mm breit, das passt gut.
    - Eine normale Stosslade mit 45°-Anschlag (Teil hochkant) geht hier nicht, weil der Hobel dann 40 mm Höhe schneiden müsste. Real schafft er nur ca. 25–30 mm.
    - Stossen, bis die vier Ecken trocken dicht schliessen. Liefert die Säge schon dichte Ecken, kann man es auslassen.
  - Die Rundung r = 6 nimmt aussen an der Gehrung ca. 1.8 mm weg. Ein Haarspalt ganz an der Spitze verschwindet beim Runden.
  - Innen in jede Ecke einen Leimklotz leimen, Langholz an Langholz. Das reicht bei einem Sockel, der unten am Korpus hängt.
  - Mit einem Spannband alle vier Ecken auf einmal verleimen.
  - Erst nach dem Verleimen die Ecken auf r = 6 mm runden (Fase → Achteck → verrunden, wie am Korpus).
- **Alternative: Gehrung mit Feder.**
  - Feder 4–5 mm dick und ca. 16 mm breit, je 8 mm in jedes Teil. Die Nut läuft über die ganze Höhe durch (unten unsichtbar, oben vom Korpus verdeckt).
  - Faser der Feder **quer zur Fuge** (waagrecht): So ist sie stabil und arbeitet gleich wie der Sockel. Dazu eine 16 mm breite Scheibe vom Brettende absägen und in Streifen auftrennen.
  - Von Hand: Nutwände mit Streichmass anreissen, mit der Feinsäge einsägen, mit Stechbeitel oder Grundhobel ausräumen.
  - Die Rundung kürzt die Gehrung aussen nur um ca. 2.5 mm und trifft die Feder nicht.
- **Alternative: Gehrfalz mit Dübel** (Spannagel, *Der Möbelbau*, S. 83).
  - Aussen nur ein kurzes Stück Gehrung, dahinter ein Falz; ein Dübel wird im 90°-Winkel durch die Verbindung geleimt.
  - Vorteil: Der Falz gibt beim Verleimen einen Anschlag, nichts verrutscht.
  - Heikel: Die kurze Gehrung an der dünnen Lippe ist die einzige sichtbare Stelle und muss genau schliessen. Der Falz quer zur Faser braucht Säge und Stechbeitel (oder einen Simshobel mit Vorschneider).
  - Die Lippe muss mindestens ca. 3–4 mm dick sein. Dann liegt die Fuge auf der Rundung (r = 6) noch in der Gehrung, und man sieht kein Hirnholz.

### Holz für die Klötze
- Reststücke vom gleichen Eichen-Leimholz. Alle Klötze sind so bemessen, dass ein Mass der Plattenstärke (18 mm) entspricht: sägen, nicht hobeln.
- **Leimklotz Ecke:** Faser **senkrecht**, damit an beiden Sockelteilen Langholz anliegt (waagrecht wäre eine Seite Hirnholz).
- **Festpunkt:** Faser von vorne nach hinten, gleich wie die Sockelseite.
- **Nutklotz:** Faser in Richtung der Lippe. Aus **einer Lamelle**, keine Leimfuge in der Lippe. Leisten 18 × 14 mm auftrennen, am Leistenende die Lippe mit der Feinsäge aussägen, ablängen, wiederholen.

### Befestigung am Korpus (Holzbewegung)
- Die Unterseite hat die Faser links–rechts und arbeitet **in der Tiefe**, um bis zu ca. 4 mm. Der Sockelrahmen bleibt in der Fläche masshaltig. Deshalb wird der Sockel **nicht verleimt**.
- **Festpunkt in der Mitte jeder Sockelseite:** Leimklotz an die Seite leimen und fest an die Unterseite schrauben. So bewegt sich der Korpus nach vorne und hinten um je ca. ±1 mm (vorne 20 ± 1, hinten 10 ± 1 mm). Bei einem Festpunkt vorne würde der Rücksprung hinten zwischen ca. 6 und 14 mm schwanken.
- **Je 2 Nutklötze vorne und hinten**, ca. 60 mm von den Ecken:
  - Nut bzw. Schlitz im Sockel: 6 mm breit, 8 mm tief, Oberkante 10 mm unter der Sockeloberkante.
  - Klotz 18 × 40 mm. Von der Auflage am Korpus bis zur Oberseite der Lippe 9 mm, also 1 mm weniger als 10 mm: So zieht die Schraube den Sockel an den Korpus.
  - **Faser im Klotz in Richtung der Lippe**, sonst bricht die Lippe ab.
  - Im Nutgrund ca. 3 mm Luft lassen (wenn im trockenen Winter montiert wird).
  - Schraube 4 × 25 mm, vorbohren. Nicht zu lang wählen, die Unterseite ist nur 18 mm dick.
  - **Runde Löcher, keine Langlöcher:** Der Nutklotz ist fest mit dem Korpus verschraubt und bewegt sich mit ihm. Die Bewegung passiert an der Lippe im Schlitz.
  - **Einzelne Schlitze** (ca. 6 × 30 mm) mit dem Stechbeitel stemmen statt einer durchlaufenden Nut. Eine durchlaufende Nut würde in den Ecken die Federnut bzw. den Leimklotz anschneiden.

## 7a. Schubladen (in Arbeit)

Front stumpf einschlagend aus Eiche 18 mm, Seiten und Hinterstück aus Buche 12 mm, Boden Sperrholz 6 mm. Aufgehängt an seitlichen Laufleisten. Alle Masse im Spreadsheet (Zeilen 56–75).

| Teil / Wert | Mass | Bemerkung |
|---|---|---|
| Verbindung vorne | verdeckte Zinken, 3 Stück | Überblattung 6 mm, Zinkenlänge 12 mm (`DrawerLap`) |
| Verbindung hinten | offene Zinken, 3 Stück | Laufnut möglichst durch eine Schwalbe legen |
| Tiefe gesamt | 370 mm | `= InnerDepth − 12 mm`, schlägt nie an der Rückwand an |
| Seiten | 364 × 122.25 × 12 mm | inkl. 12 mm Zinkenlänge vorne; oben und unten bündig mit der Front, Fase innen oben 4 mm × 45° |
| Hinterstück | 358 × 101.25 × 12 mm | über die ganze Breite (offene Zinken); steht auf dem Boden, 7 mm tiefer als die Seiten (Luft beim Schliessen) |
| Boden | 342 × 357 × 6 mm | Nut 8 mm ab Unterkante, 5 mm tief in den Seiten, 6 mm in der Front; von hinten eingeschoben, unten ans Hinterstück geschraubt |
| Laufnut | 17 × 6 mm, 25 mm unter Oberkante | vorne 5 mm hinter der Front gestoppt (= Anschlag), hinten offen |
| Laufleiste | 8.5 × 16 × 355 mm | vorne Schraube im runden Loch (Festpunkt), hinten Langlöcher: nicht leimen, die Korpusseite arbeitet in der Tiefe |

- **Front bündig einstellen:** Die Laufnut etwas zu kurz ausstemmen und dann nachstemmen, bis die Front bündig steht.
- **Fugen:** Fronten mit leichtem Übermass bauen und mit 3-mm-Distanzplättchen in der Öffnung einpassen.
- **Schattenfuge** (nach Nutsch): Falz 3 × 4 mm aussen an der Oberkante der Front (`ShadowGapHeight` / `ShadowGapDepth`, 0 = ohne). Fuge und Falz werden als dunkles Band gelesen, kleine Ungleichmässigkeiten in Fuge und Bündigkeit fallen weniger auf. Den oberen halben Zapfen ca. 8 mm breit machen, damit der Falz keine Zinke anschneidet. **Erst nach dem Einpassen hobeln.**
- **Im Modell:** Gruppe «Schublade», wird vom Array vervielfacht. Die Laufleisten gehören dazu, obwohl sie am Korpus sitzen. Die rechte Seite und die rechte Laufleiste sind gespiegelt (`Part::Mirroring`). Die Zinken sind nicht ausgeformt; die Teile überlappen in den Verbindungen, damit die Zuschnittmasse stimmen (Zugabe für überstehende Zinken nicht enthalten).

## 8. Stil

- **Richtung:** Shaker bzw. skandinavisch-handwerklich: abgeplattete Füllung, gerundete Kanten, schlichte Fronten.
- **Inspiration:**
  - Cotswold School / Arts & Crafts (Gimson, Barnsley): Eiche, Füllungen, handwerkliche Fasen.
  - Dänische Moderne (Kaare Klint, Børge Mogensen).
  - Biedermeier.
  - Schweizer Bauernmöbel (Rahmen und Füllung).
  - Max Bill: Ulmer Hocker (sichtbare Verbindung als Gestaltung).
- **Faustregel für Kontrasthölzer:** entweder das gleiche Holz oder ein deutlicher Kontrast.

## 9. Offene Punkte

- [x] **Schubladen konstruieren:** siehe Abschnitt 7a.
  - Verworfen: klassische Führung mit Lauf-, Kipp- und Streichleisten. Die Höhe der Buchenseiten bestimmt dort die Passung, und Quellen führt zum Klemmen. Ausserdem hat der Korpus keine Traversen.
  - Verworfen: Metallauszüge.
  - Kein Auszugsstopp; die Schublade lässt sich ca. 70 % ausziehen und dann herausnehmen.
- [ ] Holz für Schubladenseiten: Buchenbohle auftrennen (evtl. in einer Schreinerei auftrennen und dickenhobeln lassen), steilste Jahrringe für die Seiten. Sperrholz 6 mm mit dem Nuthobel-Eisen abgleichen, sonst den Rand falzen.
- [ ] Zinken im Modell ausformen (optional).
- [x] **Eckverbindung des Korpus:** stumpf mit Dübeln, siehe Abschnitt 4.
- [ ] **Oberfläche:** Öl oder Hartwachsöl. Mit den geschwärzten Griffen an einem Reststück testen.
- [ ] Testbrett anfertigen: Rundung 3 mm, Abplattung, Eisenacetat.
- [ ] Rendering (später): Export nach Blender, Eichentextur pro Teil in Faserrichtung ausrichten.
- [ ] Entscheid Griff: Eiche geschwärzt, Nussbaum oder gekaufter Knopf.
