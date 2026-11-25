# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/mixia666/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/mixia666/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page broadsheet that sums up the world news of Wednesday 25 November 2026 in a single 1024x1024 image: tankers striking mines in the Strait of Hormuz beneath AI-generated woodcut front-page art, a second strike on Riyadh's tallest tower, the COP31 climate collapse, Nvidia's fading comeback rally, and the day's other leading stories. `draw.py` composes `entry.png` from the day's reporting; `main.ts` copies it to the output path.

## Run it

```sh
python3 draw.py && mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`draw.py` is deterministic — the same `hero.png` and story text give the same `entry.png` bytes on every run — and `main.ts` checks the image against the gate's caps (PNG or JPEG, at most 1 MiB, at most 1024x1024) before copying it to the output path.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vd2s8rmr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
