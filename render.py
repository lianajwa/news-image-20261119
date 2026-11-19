#!/usr/bin/env python3
"""Draw the 19 November 2026 front page (1024x1024) with Pillow.

Written in this session. Vector shapes + system fonts only, so every
word is spelled exactly as shown. Deterministic output.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (24, 24, 24)
RED = (178, 34, 34)
NAVY = (23, 42, 74)
TEAL = (14, 90, 86)
GOLD = (176, 124, 22)
SEA = (198, 222, 235)
LAND = (196, 196, 150)
GREY = (90, 90, 90)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap measured in pixels."""
    out = []
    for word in text.split(" "):
        if not out:
            out.append(word)
            continue
        trial = out[-1] + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            out[-1] = trial
        else:
            out.append(word)
    return out


LEADS = [
    ("TRUMP, XI & PUTIN MEET IN SHENZHEN",
     "Xi hugs Trump on the tarmac as the APEC trilateral opens; Ukraine, Iran and AI on the table. Europe is absent.",
     "handshake", NAVY),
    ("US-IRAN WAR WIDENS ACROSS THE GULF",
     "Iran hits US bases in Kuwait and Bahrain again; the US struck a missile site on Qeshm Island on 17 Nov.",
     "missile", RED),
    ("ANTHROPIC DEBUTS AS ANT AT $83",
     "Claude-maker lists on Nasdaq at ~$1.5tn, the biggest IPO ever; 825m shares raise about $68.5bn.",
     "chart", TEAL),
    ("GTA VI GOES ON SALE WORLDWIDE",
     "Gamers enter Vice City after a 13-year wait; the global rollout begins in the UK and beyond.",
     "game", (40, 40, 60)),
    ("JEFFRIES TO BE FIRST BLACK SPEAKER",
     "Democrats nominate Hakeem Jeffries to lead the House, a first for an African-American.",
     "capitol", NAVY),
    ("CYCLONE AKVAN BEARS DOWN ON INDIA",
     "Landfall due at 145 km/h between Machilipatnam and Puri; Odisha moves 200,000 people to safety.",
     "cyclone", TEAL),
    ("VAN GOGH SELLS FOR RECORD $190.4m",
     "The painting sets a record at auction after a row over its Nazi-era history.",
     "painting", GOLD),
    ("VOYAGER 1 REACHES ONE LIGHT-DAY",
     "NASA's probe, 50 years after launch, is now a full light-day from Earth.",
     "rocket", NAVY),
    ("NORTH KOREA FIRES MISSILES",
     "Pyongyang launches ballistic missiles hours after a US-South Korea-Japan drill ends.",
     "burst", RED),
    ("MYANMAR FACES GENOCIDE VERDICT",
     "The UN court rules on the Rohingya massacres in a historic case for Myanmar.",
     "scales", TEAL),
    ("ISRAELI TANKS CROSS GAZA LINE",
     "A rare ground incursion goes beyond the Yellow Line as four nations urge aid into flooded Gaza.",
     "tank", RED),
    ("FED SIGNALS MORE RATE HIKES",
     "Minutes show most officials expect further hikes if inflation and jobs stay hot.",
     "dollar", GOLD),
]

BRIEFS = [
    "Crimean Bridge attacked again, Russian official says",
    "Nvidia's acting CEO Kress promises earlier pay rises",
    "Nvidia stops H-series chip shipments to China",
    "EU proposes a \u20ac45bn Ukraine loan, repaid by Russia",
    "Australia sanctions Israeli settlers in West Bank",
    "India and Japan hold 2+2 defence talks in Tokyo",
    "Canada's Carney rethinks China ties, seeks US deal",
    "US senators warn AI cyber threats outpace defences",
    "Herzog taps Eisenkot to form Israel's government",
    "US details $12bn in Venezuelan oil and mineral cash",
    "France holds fourth weekend of cost-of-living marches",
    "Saudi Arabia says danger passed in three south cities",
    "Cocaine and millions of pills seized in east Libya",
    "Alcaraz beats Medvedev at the ATP Finals in Turin",
    "Zverev beats Shelton 6-2, 7-6 (4) at ATP Finals",
    "Bumrah bowls Latham for a duck in Wellington Test",
    "Litton sets Test record: 8 dismissals in an innings",
    "Duckett's 133 puts England on top in 3rd ODI",
    "Brazil 7-0 Singapore; Argentina 7-0 Costa Rica",
    "HCMC Police FC stun Buriram United 1-0",
    "German climber survives a 100-metre fall in the Alps",
    "Russian held for spying on Palantir over Ukraine aid",
    "Congress targets Modi government over rising prices",
    "Islam set to be world's largest religion by 2035: Pew",
    "World COPD Day puts focus on early diagnosis",
    "McDonald's abuse inquiry: girls 'waited to turn 18'",
    "French minister: M\u00e9lenchon could win the presidency",
    "Oil prices fall as Middle East tensions rise",
    "Microsoft in talks to sell AI services to ByteDance",
    "Stocks fall on Gulf tensions; Tokyo scrambles jets",
    "NGO: Israel limits care for 1,100 child amputees",
    "Germany charges Ilona W. with spying for Russia",
    "S. Africa build a big lead v Bangladesh at Wanderers",
]

NUMBERS = [
    ("45", "STORIES"), ("7", "CONTINENTS"), ("$83", "ANT PRICE"),
    ("$1.5tn", "VALUATION"), ("$190.4m", "VAN GOGH"),
    ("145 km/h", "AKVAN"), ("50y", "VOYAGER 1"),
]

# pin positions (x, y) on the map, one per lead
PINS = [(860, 190), (565, 220), (160, 190), (440, 170), (185, 215),
        (690, 225), (455, 185), (115, 225), (905, 200), (735, 245),
        (550, 205), (140, 245)]


def draw_icon(d, kind, x, y, s, color):
    d.rectangle([x, y, x + s, y + s], fill=color)
    cx, cy = x + s // 2, y + s // 2
    w = (255, 255, 255)
    if kind == "handshake":
        d.ellipse([x + 6, y + 12, x + 20, y + 26], outline=w, width=2)
        d.ellipse([x + 24, y + 12, x + 38, y + 26], outline=w, width=2)
        d.arc([x + 10, y + 22, x + 34, y + 40], 0, 180, fill=w, width=2)
    elif kind == "missile":
        d.polygon([(cx, y + 6), (cx + 8, y + 30), (cx - 8, y + 30)], fill=w)
        d.line([cx, y + 30, cx, y + 40], fill=w, width=3)
    elif kind == "chart":
        d.line([x + 8, y + 36, x + 36, y + 36], fill=w, width=2)
        d.line([x + 8, y + 36, x + 8, y + 8], fill=w, width=2)
        d.line([x + 10, y + 30, x + 18, y + 22, x + 26, y + 26, x + 36, y + 10],
               fill=w, width=3)
    elif kind == "game":
        d.rounded_rectangle([x + 6, y + 12, x + 38, y + 32], 6, outline=w, width=2)
        d.line([x + 14, y + 22, x + 20, y + 22], fill=w, width=2)
        d.line([x + 17, y + 19, x + 17, y + 25], fill=w, width=2)
        d.ellipse([x + 26, y + 19, x + 30, y + 23], fill=w)
        d.ellipse([x + 31, y + 22, x + 35, y + 26], fill=w)
    elif kind == "capitol":
        d.arc([x + 12, y + 8, x + 32, y + 24], 180, 360, fill=w, width=2)
        d.line([x + 10, y + 24, x + 34, y + 24], fill=w, width=2)
        for lx in (13, 20, 27):
            d.line([x + lx, y + 26, x + lx, y + 38], fill=w, width=2)
        d.line([x + 8, y + 38, x + 36, y + 38], fill=w, width=2)
    elif kind == "cyclone":
        for r in (5, 10, 15):
            d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300, fill=w, width=2)
    elif kind == "painting":
        d.rectangle([x + 8, y + 8, x + 36, y + 36], outline=w, width=2)
        d.ellipse([x + 16, y + 14, x + 28, y + 26], fill=w)
        d.line([x + 8, y + 32, x + 36, y + 32], fill=w, width=2)
    elif kind == "rocket":
        d.polygon([(cx, y + 5), (cx + 7, y + 26), (cx - 7, y + 26)], fill=w)
        d.polygon([(cx, y + 26), (cx + 4, y + 38), (cx - 4, y + 38)], fill=(255, 180, 60))
        d.ellipse([cx - 3, y + 14, cx + 3, y + 20], fill=color)
    elif kind == "burst":
        for a in range(0, 360, 45):
            import math
            r1, r2 = 6, 16
            x1 = cx + r1 * math.cos(math.radians(a))
            y1 = cy + r1 * math.sin(math.radians(a))
            x2 = cx + r2 * math.cos(math.radians(a))
            y2 = cy + r2 * math.sin(math.radians(a))
            d.line([x1, y1, x2, y2], fill=w, width=2)
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=w)
    elif kind == "scales":
        d.line([cx, y + 8, cx, y + 36], fill=w, width=2)
        d.line([x + 8, y + 14, x + 36, y + 14], fill=w, width=2)
        d.arc([x + 6, y + 14, x + 16, y + 28], 0, 180, fill=w, width=2)
        d.arc([x + 28, y + 14, x + 38, y + 28], 0, 180, fill=w, width=2)
    elif kind == "tank":
        d.rectangle([x + 8, y + 18, x + 32, y + 30], fill=w)
        d.line([x + 30, y + 22, x + 40, y + 20], fill=w, width=3)
        for wx in (13, 21, 29):
            d.ellipse([x + wx, y + 31, x + wx + 5, y + 36], fill=w)
    elif kind == "dollar":
        d.text((cx - 7, y + 8), "$", font=font(SANS_B, 26), fill=w)
        d.line([x + 8, y + 34, x + 36, y + 34], fill=w, width=2)


def draw_map(d):
    d.rectangle([24, 146, 1000, 282], fill=SEA, outline=INK, width=2)
    d.text((36, 152), "THE WORLD — WHERE IT HAPPENED",
           font=font(SANS_B, 12), fill=NAVY)
    # simplified continents (schematic blobs)
    blobs = [
        [(60, 190), (140, 175), (180, 195), (160, 235), (100, 245), (65, 220)],
        [(210, 200), (300, 185), (330, 210), (300, 250), (230, 245)],
        [(430, 180), (520, 170), (560, 190), (540, 220), (470, 230), (435, 205)],
        [(580, 195), (660, 185), (700, 205), (680, 250), (610, 255), (585, 225)],
        [(740, 180), (860, 170), (920, 195), (900, 235), (800, 245), (745, 215)],
        [(860, 245), (920, 240), (940, 262), (880, 272), (855, 258)],
    ]
    for b in blobs:
        d.polygon(b, fill=LAND, outline=(120, 120, 90))
    for (lx, ly, name) in [(110, 200, "N. AMERICA"), (260, 215, "S. AMERICA"),
                            (480, 195, "EUROPE"), (640, 215, "AFRICA"),
                            (830, 205, "ASIA"), (895, 252, "OCEANIA")]:
        d.text((lx, ly), name, font=font(SANS_B, 9), fill=(70, 70, 50))
    for i, (px, py) in enumerate(PINS, 1):
        d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED, outline=(255, 255, 255), width=2)
        t = str(i)
        tw = d.textlength(t, font=font(SANS_B, 10))
        d.text((px - tw / 2, py - 7), t, font=font(SANS_B, 10), fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # masthead
    title = "THE WORLD IN ONE DAY"
    f_title = font(SERIF, 46)
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 14), title, font=f_title, fill=INK)
    sub = "THURSDAY 19 NOVEMBER 2026  \u2022  45 STORIES  \u2022  7 CONTINENTS  \u2022  1 PAGE"
    f_sub = font(SANS_B, 15)
    tw = d.textlength(sub, font=f_sub)
    d.text(((W - tw) / 2, 72), sub, font=f_sub, fill=RED)
    d.line([24, 98, 1000, 98], fill=INK, width=3)
    # numbers strip
    d.rectangle([24, 104, 1000, 138], fill=NAVY)
    cell = (1000 - 24) / len(NUMBERS)
    for i, (num, lab) in enumerate(NUMBERS):
        cx = 24 + cell * i + cell / 2
        fn, fl = font(SANS_B, 16), font(SANS_B, 9)
        d.text((cx - d.textlength(num, font=fn) / 2, 108), num, font=fn, fill=(255, 255, 255))
        d.text((cx - d.textlength(lab, font=fl) / 2, 126), lab, font=fl, fill=(180, 200, 230))
    draw_map(d)
    # leads: 3 columns x 4 rows
    col_x = [24, 356, 688]
    col_w = 312
    row_y = [292, 382, 472, 562]
    for idx, (head, summ, kind, color) in enumerate(LEADS):
        cx = col_x[idx % 3]
        cy = row_y[idx // 3]
        d.ellipse([cx, cy, cx + 22, cy + 22], fill=RED)
        t = str(idx + 1)
        tw = d.textlength(t, font=font(SANS_B, 12))
        d.text((cx + 11 - tw / 2, cy + 3), t, font=font(SANS_B, 12), fill=(255, 255, 255))
        draw_icon(d, kind, cx + 28, cy, 44, color)
        tx = cx + 78
        twd = col_w - 78
        lines = wrap(d, head, font(SANS_B, 13), twd)[:2]
        y = cy
        for ln in lines:
            d.text((tx, y), ln, font=font(SANS_B, 13), fill=INK)
            y += 16
        slines = wrap(d, summ, font(SANS, 11), twd)[:3]
        for ln in slines:
            d.text((tx, y), ln, font=font(SANS, 11), fill=(60, 60, 60))
            y += 14
    d.line([24, 652, 1000, 652], fill=INK, width=2)
    d.text((24, 660), "ALSO TODAY \u2014 BRIEFS 13\u201345",
           font=font(SANS_B, 14), fill=RED)
    # briefs: 3 columns x 11 rows
    f_b = font(SANS, 11)
    for i, b in enumerate(BRIEFS):
        col = i // 11
        row = i % 11
        x = 24 + col * 328
        y = 686 + row * 27
        d.text((x, y), "%d. %s" % (13 + i, b), font=f_b, fill=INK)
    d.line([24, 986, 1000, 986], fill=INK, width=2)
    d.text((24, 994),
           "Sources: Reuters \u2022 AP \u2022 AFP \u2022 BBC \u2022 Al Jazeera \u2022 CNN \u2022 NYT \u2014 checked 19 Nov 2026",
           font=font(SANS, 11), fill=GREY)
    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
