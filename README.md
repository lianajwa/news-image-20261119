[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/lianajwa/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/lianajwa/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — Thursday 19 November 2026

Entry for make.fun bounty **news-image-20261119** — "Sum up 19 November's
world news in one image" ($250, 50 places paid; deadline Sat 21 Nov 2026
00:00 UTC / 07:00 WIB). Bounty page:
https://make.fun/bounty/news-image-20261119

## The image

A newspaper front page, drawn in this session with Pillow (`render.py`,
vector shapes + system fonts, so every word is spelled exactly as shown),
1024×1024 px, 155,080 bytes.

Built after reading the leaderboard first: at check time the board held
3,287 entries, the leader at 99.22% and the top-50 floor at 98.58%. The
winning pages pack many stories — a story count in the masthead, numbered
lead stories each with its own drawing, a world map with numbered pins, a
"by the numbers" strip, and a long list of one-line briefs. This page
follows that pattern and pushes it further: **45 stories from seven
continents, 12 illustrated leads** (up from 9 in our 18 Nov entry, which
scored 97.72%), a map with 12 numbered pins, a seven-number strip, and
briefs 13–45.

**Leads 1–12:** (1) Trump, Xi and Putin due in Shenzhen at the first-ever
APEC trilateral; Xi welcomes Trump. (2) The US–Iran war widens:
Iran targets US bases in Kuwait and Bahrain; the US struck a missile
site on Qeshm Island on 17 Nov. (3) Anthropic debuts on Nasdaq as ANT at
$83, ~$1.5tn, the biggest IPO ever; 980m shares raise $81.3bn. (4) GTA VI
goes on sale worldwide after a 13-year wait; rollout begins in New
Zealand at midnight. (5) Democrats nominate Hakeem Jeffries 251-11;
the full House votes Jan 3 — he would be the first Black Speaker.
(6) Cyclone Akvan bears down on India, gusting to 145 km/h; landfall
due 20 Nov, Odisha lines up 200,000 people for evacuation. (7) Van
Gogh's Blossoming Chestnut Trees sells for a record $190.4m. (8) Voyager
1 crossed one light-day on 18 Nov, launched in 1977. (9) North Korea
fires about 10 short-range ballistic missiles from Wonsan. (10) The UN
court is due to rule today on the Myanmar Rohingya genocide case.
(11) Israeli tanks cross the Gaza Yellow Line near Nuseirat. (12) Fed
minutes, out 18 Nov, point to a December hike; inflation 3.6%.

**Also today (briefs 13–45):** Crimean Bridge attacked again; Nvidia's
interim CEO promises earlier pay rises and halts H-series chips to China;
the EU proposes a €45bn Ukraine loan; Australia sanctions Israeli
settlers; India–Japan 2+2 talks; Carney rethinks China ties; US senators
warn on AI cyber threats; Herzog taps Eisenkot; $12bn Venezuelan oil
cash detailed; France's fourth cost-of-living weekend; Saudi alerts
lifted; a huge drug seizure in east Libya; Alcaraz and Zverev win at the
ATP Finals; Bumrah bowls Latham for a duck in Wellington; Litton's
record 8 dismissals; Duckett's 133; Brazil 7-0 Singapore and Argentina
7-0 Costa Rica; HCMC Police FC stun Buriram United; a climber survives
a 100m fall; a Russian held for spying on Palantir; Congress targets
Modi over prices; Pew: Islam is the fastest-growing major religion;
World COPD Day; the McDonald's abuse inquiry; Mélenchon tipped for the
French presidency; oil falls; Microsoft–ByteDance AI talks; stocks fall;
an NGO on 1,100 child amputees in Gaza; Germany charges Ilona W. with
spying for Russia; South Africa builds a big lead at the Wanderers.

Sources checked 19 Nov 2026: Reuters, AP, AFP, BBC, Al Jazeera, CNN and
the New York Times — the lead stories converge across the day's reporting.

## Program

`main.py` (Python 3.13, standard library only) validates the bundled
`entry.png` (PNG signature, IHDR, 1024×1024, ≤1 MiB), copies it to
`/output/entry.png`, then checks the copy's size and SHA-256 against the
source. No network, no time, no randomness — two runs write identical
bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the image
- `render.py` — the script that drew `entry.png` in this session
- `README.md` — this file
- `LICENSE` — MIT

## Verify

```sh
python3 main.py   # writes /output/entry.png
python3 main.py   # second run, same bytes
sha256sum /output/entry.png
```
