# Erzeugt eine massstäbliche Nahansicht der Schubladenseite mit Zinkenteilung (SVG)
# Aufruf: python3 zinkenteilung.py [DrawerHeight]   (Standard 122.25, Wert aus dem Spreadsheet)
# Werte aus dem Spreadsheet sind unten fest eingetragen; bei Änderungen dort hier nachführen.
import os, sys
S = 4.0                                   # px pro mm
H = float(sys.argv[1]) if len(sys.argv) > 1 else 122.25   # DrawerHeight
TOP = 70
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zinkenteilung.svg")

# Werte aus dem Spreadsheet
LN = (H - 25 - 17, H - 25)            # Laufnut
RU = (LN[0] + 1, LN[1])               # Laufleiste
BN = (8, 14)                          # Bodennut
HS = (14, H - 7)                      # Hinterstück
L = 12                                # Zinkenlänge (= Seitenstärke bzw. Wall − DrawerLap)

# ---------- Regeln Zinkenteilung ----------
SLOPE = 8                             # 1:8
d = L / SLOPE                         # Schräge pro Seite über die Zinkenlänge = 1.5
PIN = 6                               # Zapfen an der schmalen Stelle (Seitenende)
MARGIN = 3                            # Rand Laufnut in der Schwalbe (an der Risslinie)

# hinten: Schwalbe über der Laufnut, oberer und unterer halber Zapfen gleich, 2 Schwalben dazwischen
top_tail = (LN[0] - MARGIN - d, LN[1] + MARGIN + d)          # Breite am Seitenende
half_back = HS[1] - top_tail[1]
t_back = (top_tail[0] - (HS[0] + half_back) - 2 * PIN) / 2
a = HS[0] + half_back
back_tails = [(a, a + t_back), (a + t_back + PIN, a + 2 * t_back + PIN), top_tail]

# vorne: halber Zapfen oben 8, unten so, dass die unterste Schwalbe die Bodennut mit 2 mm Rand fasst
HALF_TOP_FRONT = 8
half_bot_front = BN[0] - 2 - d
t_front = (H - half_bot_front - HALF_TOP_FRONT - 2 * PIN) / 3
front_tails = [(half_bot_front + i * (t_front + PIN), half_bot_front + i * (t_front + PIN) + t_front) for i in range(3)]

WOOD, WOOD2, BEECH, PINC, GREY, PLY = "#e6cfa3", "#c9a874", "#f0dcc0", "#c79a63", "#8a8a8a", "#a9bcd6"
GREEN, RED = "#1f9d6b", "#d9534f"
out = []
def Y(z): return TOP + (H - z) * S
def rect(x0, x1, z0, z1, fill, stroke="#333", dash=None, op=1, sw=1):
    dd = f' stroke-dasharray="{dash}"' if dash else ""
    out.append(f'<rect x="{min(x0,x1):.1f}" y="{Y(z1):.1f}" width="{abs(x1-x0):.1f}" height="{(z1-z0)*S:.1f}" '
               f'fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"{dd}/>')
def poly(pts, fill, stroke="#333", sw=1, op=1):
    out.append('<polygon points="' + " ".join(f"{x:.1f},{Y(z):.1f}" for x, z in pts) +
               f'" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}"/>')
def line(x0, z0, x1, z1, dash=None, col="#333", sw=1):
    dd = f' stroke-dasharray="{dash}"' if dash else ""
    out.append(f'<line x1="{x0:.1f}" y1="{Y(z0):.1f}" x2="{x1:.1f}" y2="{Y(z1):.1f}" stroke="{col}" stroke-width="{sw}"{dd}/>')
def text(x, z, s, size=12, anchor="start", col="#222", weight="normal"):
    out.append(f'<text x="{x:.1f}" y="{Y(z)+4:.1f}" font-size="{size}" text-anchor="{anchor}" fill="{col}" '
               f'font-family="Helvetica" font-weight="{weight}">{s}</text>')
def title(x, s, sub):
    out.append(f'<text x="{x}" y="28" font-size="16" font-weight="bold" font-family="Helvetica">{s}</text>')
    out.append(f'<text x="{x}" y="48" font-size="12" fill="#555" font-family="Helvetica">{sub}</text>')
def ticks(x, zs, side="right", col="#555"):
    for z in zs:
        line(x - 3, z, x + 3, z, col="#666")
        text(x + (6 if side == "right" else -6), z, f"{round(z, 2):g}", 11, "start" if side == "right" else "end", col)
def pins(px, y_end, y_base, tails, z0, z1):
    """Zapfen zwischen den Schwalben; Schwalben am Seitenende breit, an der Risslinie um d schmaler."""
    edges = [z0] + [v for t in tails for v in t] + [z1]
    for i in range(0, len(edges), 2):
        lo, hi = edges[i], edges[i + 1]
        lo_b = lo if i == 0 else lo - d       # an der Risslinie ist der Zapfen breiter
        hi_b = hi if i == len(edges) - 2 else hi + d
        poly([(px(y_end), lo), (px(y_end), hi), (px(y_base), hi_b), (px(y_base), lo_b)], PINC, sw=1)
    for lo, hi in tails:
        line(px(y_end), lo, px(y_base), lo + d, col="#333", sw=1.5)
        line(px(y_end), hi, px(y_base), hi - d, col="#333", sw=1.5)

# ---------- 1: Hinteres Ende, Aussenansicht ----------
ox = 70
def px1(y): return ox + (y - 320) * S
title(ox - 10, "1 · Hinten: offene Zinken", "Ansicht von aussen · Laufnut läuft durch die oberste Schwalbe")
rect(px1(320), px1(370), 0, H, BEECH)
rect(px1(320), px1(370), LN[0], LN[1], WOOD2)
pins(px1, 370, 358, back_tails, HS[0], HS[1])
rect(px1(320), px1(378), RU[0], RU[1], GREY, op=0.55)
line(px1(320), BN[0], px1(370), BN[0], dash="4,3"); line(px1(320), BN[1], px1(370), BN[1], dash="4,3")
line(px1(358), 0, px1(358), H, dash="2,3", col=RED)
text(px1(322), (LN[0] + LN[1]) / 2, "Laufnut", 11)
text(px1(322), 11, "Bodennut (innen)", 10, col="#555")
text(px1(322), (HS[0] + top_tail[0]) / 2, "Zapfen = Hinterstück", 10, col="#7a5530")
ticks(px1(320) - 8, [0, BN[0], BN[1], LN[0], LN[1], H], "left")
ticks(px1(378) + 8, [HS[0]] + [v for t in back_tails for v in t] + [HS[1]], "right", GREEN)

# ---------- 2: Querschnitt ----------
ox2 = 470
def px2(x): return ox2 + (x - 12) * S
title(ox2, "2 · Querschnitt, Blick nach hinten", "Korpus | Laufleiste | Seite | Boden")
rect(px2(12), px2(18), 0, H, WOOD, stroke="none"); line(px2(18), 0, px2(18), H)
pts = [(21, 0), (33, 0), (33, BN[0]), (28, BN[0]), (28, BN[1]), (33, BN[1]), (33, H - 4), (29, H), (21, H),
       (21, LN[1]), (27, LN[1]), (27, LN[0]), (21, LN[0])]
poly([(px2(x), z) for x, z in pts], BEECH, sw=1.5)
rect(px2(18), px2(26.5), RU[0], RU[1], GREY, op=0.8)
rect(px2(29), px2(55), BN[0], BN[1], PLY)
rect(px2(21), px2(55), HS[0], HS[1], "none", stroke=RED, dash="5,3")
text(px2(44), (HS[0] + HS[1]) / 2, "Hinterstück", 11, "middle", RED)
text(px2(44), (HS[0] + HS[1]) / 2 - 10, "(dahinter)", 10, "middle", RED)
text(px2(44), 20, "Boden 6", 10, "middle", "#335")
text(px2(30), (LN[0] + LN[1]) / 2, "← Laufleiste", 11)
ticks(px2(55) + 6, [0, BN[0], BN[1], LN[0], LN[1], HS[1], H], "right")

# ---------- 3: Vorderes Ende, Aussenansicht ----------
ox3 = 830
def px3(y): return ox3 + y * S
title(ox3 - 40, "3 · Vorne: verdeckte Zinken", "Ansicht von aussen · Front links, Überblattung 6")
rect(px3(0), px3(18), 0, H, WOOD)
poly([(px3(0), H - 3), (px3(4), H - 3), (px3(4), H), (px3(0), H)], "#fff")
rect(px3(6), px3(50), 0, H, BEECH)
pins(px3, 6, 18, front_tails, 0, H)
rect(px3(23), px3(50), LN[0], LN[1], WOOD2)
line(px3(6), BN[0], px3(50), BN[0], dash="4,3"); line(px3(6), BN[1], px3(50), BN[1], dash="4,3")
line(px3(18), 0, px3(18), H, dash="2,3", col=RED)
text(px3(24), (LN[0] + LN[1]) / 2, "Laufnut", 11)
text(px3(21), 11, "Bodennut", 10, col="#555")
text(px3(52), H - 2, "← Schattenfuge 3 × 4 liegt über", 11, col=GREEN)
text(px3(52), H - 12, "    dem halben Zapfen (8)", 11, col=GREEN)
text(px3(52), 11, "← Bodennut in der", 11, col=GREEN)
text(px3(52), 1, "    untersten Schwalbe", 11, col=GREEN)
ticks(px3(0) - 8, [0] + [v for t in front_tails for v in t] + [H], "left", GREEN)

# ---------- Regeln ----------
f = lambda v: f"{round(v, 2):g}"
rules = [
    f"Beispiel für DrawerHeight = {f(H)} mm · Steigung 1:{SLOPE} (± {d:g} mm über {L} mm Zinkenlänge) · Zapfen {PIN} mm an der schmalen Stelle",
    "Grüne Masse am Seitenende, wo die Schwalben am breitesten sind; rot gepunktet = Risslinie",
    f"Hinten: Verbindung 14 … H−7. Oberste Schwalbe = Laufnut + {MARGIN} mm Rand an der Risslinie ({f(top_tail[0])} … {f(top_tail[1])}).",
    f"           Halbe Zapfen oben und unten gleich ({f(half_back)}), dazwischen 2 gleiche Schwalben ({f(t_back)}).",
    f"Vorne: halber Zapfen oben {HALF_TOP_FRONT}, unten {f(half_bot_front)} (Bodennut mit 2 mm Rand in der Schwalbe), 3 gleiche Schwalben ({f(t_front)}).",
    "Oberste und unterste Schwalbe hängen an Ober- bzw. Unterkante; mit der Höhe ändern sich nur die mittleren.",
]
base = TOP + H * S + 40
for i, r in enumerate(rules):
    out.append(f'<text x="20" y="{base + i*20:.0f}" font-size="12" fill="#333" font-family="Helvetica">{r}</text>')

W, Hpx = 1420, base + len(rules) * 20 + 10
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hpx:.0f}" viewBox="0 0 {W} {Hpx:.0f}">'
       f'<rect width="100%" height="100%" fill="#fff"/>' + "".join(out) + "</svg>")
open(OUT, "w").write(svg)
print("hinten", [tuple(round(v, 2) for v in t) for t in back_tails], "halb", round(half_back, 2), "t", round(t_back, 2))
print("vorne ", [tuple(round(v, 2) for v in t) for t in front_tails], "halb unten", half_bot_front, "t", round(t_front, 2))
