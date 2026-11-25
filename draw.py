#!/usr/bin/env python3
"""Draw "The World in One Day" for Wednesday 25 November 2026.

A one-page broadsheet, 1024x1024 PNG, summing up the day's world news
for the make.fun news-image-20261125 entry. The front-page art
(hero.png, kept beside this file) is an AI-generated woodcut-style
illustration of the lead story; every headline and paragraph below was
reported on 25 November 2026 (SCMP, The Japan Times, ProPublica,
Qatar Tribune, One Turn, Horizon, DD India). Deterministic: the same
inputs give the same bytes every run.

Run:  python3 draw.py            (writes entry.png beside this file)
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 245, 238)
INK = (21, 20, 18)
GREY = (92, 86, 76)
RED = (163, 28, 28)
RULE = (35, 33, 30)
FAINT = (168, 160, 146)

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 36                 # side margin
X1 = W - MX             # right edge of the text block
CW = X1 - MX            # column width


def hline(y, x0=MX, x1=X1, w=2, fill=RULE):
    d.line([(x0, y), (x1, y)], fill=fill, width=w)


def centered(text, y, fnt, fill=INK):
    tw = d.textlength(text, font=fnt)
    d.text(((W - tw) / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


def wrap(text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def block(text, x, y, fnt, max_w, leading, fill=INK):
    for ln in wrap(text, fnt, max_w):
        d.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def story(x, y, col_w, kicker, head, body):
    d.text((x, y), kicker, font=F(SANS_B, 13), fill=RED)
    y += 18
    y = block(head, x, y, F(SERIF_B, 22), col_w, 25)
    y += 2
    y = block(body, x, y, F(SERIF, 16), col_w, 20, fill=(45, 42, 38))
    return y


# ---- masthead -------------------------------------------------------------
y = 22
y = centered("WEDNESDAY · 25 NOVEMBER 2026 · ONE PAGE, THE WHOLE DAY",
             y, F(SANS_B, 15), fill=GREY)
y += 6
y = centered("THE WORLD IN ONE DAY", y, F(SERIF_B, 54))
y += 8
hline(y, w=3)
y += 4
hline(y, w=1)
y += 13

# ---- lead -----------------------------------------------------------------
d.text((MX, y), "STRAIT OF HORMUZ · THE IRAN WAR", font=F(SANS_B, 14), fill=RED)
y += 22
y = block("Tankers Hit Mines in Hormuz", MX, y, F(SERIF_B, 52), CW, 58)
y += 2
y = block("Iran's Revolutionary Guards said two tankers struck mines in the "
          "chokepoint that carries a fifth of the world's oil — and with a "
          "second strike on Riyadh, a collapsed climate summit and a rout "
          "in AI shares, it was a day felt everywhere at once.",
          MX, y, F(SERIF, 19), CW, 24, fill=(45, 42, 38))
y += 10

# ---- front-page art ---------------------------------------------------------
art = Image.open("hero.png").convert("RGB")
img.paste(art, (MX, y))
d.rectangle([MX, y, MX + art.width - 1, y + art.height - 1], outline=RULE, width=2)
y += art.height + 6
y = block("A tanker crosses the strait as an explosion lights the far shore "
          "and a naval mine rides the swell.",
          MX, y, F(SANS, 13), CW, 16, fill=GREY)
y += 8
hline(y, w=2)
y += 12

# ---- two columns ------------------------------------------------------------
GUT = 28
COLW = (CW - GUT) // 2
LX, RX = MX, MX + COLW + GUT
top = y

ly = top
ly = story(LX, ly, COLW, "SAUDI ARABIA",
           "Riyadh's Tallest Tower Struck Again",
           "Saudi Arabia said 11 people were hurt when the capital's "
           "tallest skyscraper was hit for the second time in a week, "
           "blaming Yemen's Houthi rebels.")
ly += 11
ly = story(LX, ly, COLW, "CLIMATE · ANTALYA",
           "Climate Talks Collapse at COP31",
           "The summit ended in failure after Saudi Arabia and other "
           "oil states blocked any mention of phasing out fossil fuels, "
           "pressing carbon capture instead.")
ly += 11
ly = story(LX, ly, COLW, "UNITED STATES · COURTS",
           "Huawei Convicted in U.S. Trial",
           "A federal jury convicted the Chinese telecoms giant in a "
           "sprawling criminal case over its Iran business and "
           "technology taken from American rivals.")

ry = top
ry = story(RX, ry, COLW, "TECH · NVIDIA",
           "Huang's Comeback Rally Fades",
           "Nvidia slid about 7% as lawmakers questioned President "
           "Trump's hand in restoring Jensen Huang as chief executive; "
           "Huang told staff he is in daily therapy.")
ry += 11
ry = story(RX, ry, COLW, "MARKETS",
           "AI Doubts Sink Asian Shares",
           "The Nikkei fell 2.76% and the S&P 500 0.5% as investors "
           "again doubted the AI boom will pay off. Brent crude dropped "
           "to $87.49 a barrel.")
ry += 11
ry = story(RX, ry, COLW, "SPACE · SHENZHOU-24",
           "First Pakistani Astronaut Aboard China's Station",
           "Shenzhou-24 docked at China's space station carrying the "
           "first Pakistani national into orbit, a first for the two "
           "countries' space partnership.")

y = max(ly, ry) + 10
d.line([(MX + COLW + GUT // 2, top), (MX + COLW + GUT // 2, y - 16)],
       fill=FAINT, width=1)

# ---- also today -------------------------------------------------------------
hline(y, w=2)
y += 9
d.text((MX, y), "ALSO TODAY", font=F(SANS_B, 14), fill=RED)
y += 20
y = block("Cartagena supermarket hostages freed unharmed · Sports court "
          "returns the Africa Cup title to Senegal · Beijing investigates "
          "Shanghai's party chief in a widening shake-up · Australia signs "
          "a Solomon Islands security pact barring foreign bases · "
          "Washington readies new global tariffs after its capacity probe "
          "· Landmine casualties hit a five-year high of 7,000 · World "
          "court rules Myanmar's army committed genocide against the "
          "Rohingya",
          MX, y, F(SERIF, 16), CW, 21, fill=(45, 42, 38))
y += 9
hline(y, w=1)
y += 7
centered("Reporting: SCMP · The Japan Times · ProPublica · Qatar Tribune · "
         "One Turn · Horizon · DD India", y, F(SANS, 13), fill=GREY)

assert y + 30 <= H, f"page overflow: content ends at {y}"
img.quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(
    "entry.png", optimize=True)
print("wrote entry.png, content ends at y =", y)
