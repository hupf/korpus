# Korpus mit Schubladen – Projektnotizen

Schubladenkorpus aus Eichen-Leimholz, von Hand gebaut, für unter das Pult (Rückwand sichtbar).
FreeCAD-Modell: `Korpus.FCStd` – alle Masse kommen aus dem **Spreadsheet** und lassen sich dort ändern.

Stand: 10.10.2026

---

## 1. Hauptmasse

| Wert (Spreadsheet) | Mass | Bemerkung |
|---|---|---|
| `TotalHeight` | 580 mm | Gesamthöhe inkl. Füsse |
| `FeetHeight` | 75 mm | Höhe der Füsse (Füsse noch nicht modelliert) |
| `BodyHeight` | 505 mm | Korpushöhe |
| `BodyWidth` × `BodyDepth` | 400 × 400 mm | |
| `Wall` | 18 mm | Plattenstärke = Eichen-Leimholz aus dem Baumarkt (Bauhaus/Jumbo) |
| `DrawerCount` | 4 | |
| `DrawerGap` | 3 mm | Fuge ringsum, überall gleich |
| `DrawerHeight` | 113.5 mm | Fronthöhe, wird berechnet |

- Lichte Öffnung: 364 × 469 mm
- Schubladenfronten: 358 × 113.5 × 18 mm, einliegend, bündig mit der Korpusvorderkante
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

- **Rückwand:** 376 × 481 × 18 mm.
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

## 7. Stil

- **Richtung:** Shaker bzw. skandinavisch-handwerklich: abgeplattete Füllung, gerundete Kanten, schlichte Fronten.
- **Inspiration:**
  - Cotswold School / Arts & Crafts (Gimson, Barnsley): Eiche, Füllungen, handwerkliche Fasen.
  - Dänische Moderne (Kaare Klint, Børge Mogensen).
  - Biedermeier.
  - Schweizer Bauernmöbel (Rahmen und Füllung).
  - Max Bill: Ulmer Hocker (sichtbare Verbindung als Gestaltung).
- **Faustregel für Kontrasthölzer:** entweder das gleiche Holz oder ein deutlicher Kontrast.

## 8. Offene Punkte

- [ ] **Schubladen konstruieren** (später). Innentiefe max. ca. 380 mm.
  - **Kasten:**
    - Material: Eiche 18 mm ist eher schwer. Möglich sind dünnere Zargen, z.B. 10–12 mm Eiche oder ein leichteres Holz.
    - Eckverbindungen: Zinken (klassisch von Hand: vorne halbverdeckt, hinten offen), Nut und Feder, Falz mit Dübeln.
    - Boden: in einer Nut schwimmend, Faser von links nach rechts, damit er nach hinten ausweichen kann. Alternativ Sperrholz.
    - Verbindung von Front und Kasten: Ist die Front selbst die Vorderwand, oder wird sie auf einen Kasten aufgesetzt?
    - Platz für die Finger hinter dem Griff beachten (bei aufgesetzten Griffen unkritisch).
  - **Führung:**
    - Holz auf Holz: Die Schublade läuft auf dem Boden bzw. auf Laufleisten, seitlich geführt. Klassisch, still, kein Beschlag nötig. Braucht genaue Passarbeit und Wachs.
    - Seitliche Gleitleisten: Eine Leiste an der Korpusseite greift in eine Nut in der Schubladenzarge, oder umgekehrt. Gut von Hand machbar, auch mit dem Nuthobel.
    - Metallauszüge (Kugel- oder Vollauszüge): leichtgängig, Vollauszug möglich. Sie brauchen seitlich meist 12.5 mm Platz pro Seite und sind sichtbar, wenn die Schublade offen ist.
    - Kippsicherung bzw. Anschlag: Wie weit lässt sich die Schublade ausziehen, wo stoppt sie beim Schliessen?
- [ ] **Eckverbindung des Korpus** festlegen (z.B. Zinken, Dübel, Lamellos …).
- [ ] **Unterbau (75 mm Höhe, `FeetHeight`)** entscheiden, gestalten und modellieren. Möglichkeiten:
  - **Rollen:** praktisch unter einem Pult, weil sich der Korpus verschieben lässt. Bremsrollen wählen. Die Bauhöhe der Rollen bestimmt `FeetHeight`. Die Unterseite muss die Schraubpunkte tragen.
  - **Sockel:** ein zurückgesetzter Rahmen aus Eiche, z.B. 20–30 mm hinter der Vorderkante. Wirkt ruhig und «schwebend», ist stabil und schützt vor Staub darunter.
  - **Füsse:** vier einzelne Füsse aus Eiche, gerade, leicht konisch oder schräg gestellt. Wirkt leicht und möbelhaft (Shaker / dänisch).
  - **Kufen:** zwei Leisten links und rechts von vorne nach hinten. Schlicht, handwerklich, einfach zu bauen.
  - Klären: Soll der Korpus mobil sein? Wie viel Platz bleibt unter dem Pult (Gesamthöhe 580 mm)?
- [ ] **Oberfläche:** Öl oder Hartwachsöl. Mit den geschwärzten Griffen an einem Reststück testen.
- [ ] Testbrett anfertigen: Rundung 3 mm, Abplattung, Eisenacetat.
- [ ] Rendering (später): Export nach Blender, Eichentextur pro Teil in Faserrichtung ausrichten.
- [ ] Entscheid Griff: Eiche geschwärzt, Nussbaum oder gekaufter Knopf.
