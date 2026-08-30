<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Mr.Z&fontSize=52&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Software%20Engineering%20Student&descAlignY=56&descAlign=50" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3000&pause=825&color=58A6FF&center=true&vCenter=true&width=650&lines=I+build+things%2C+break+things%2C+fix+things.;Systems+%7C+Hardware+%7C+FPV+%7C+AI;Currently+learning+%E2%80%94+always+building.)](https://git.io/typing-svg)

<br/>

<img src="https://komarev.com/ghpvc/?username=ItsMrZxD&label=Profile%20views&color=58A6FF&style=flat" alt="profile views"/>

</div>

<br/>

<img align="right" src="https://github-readme-stats-eta-one-23.vercel.app/api/top-langs?username=ItsMrZxD&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" width="300"/>

### `> whoami`

```
Name     :  Mr.Z
Role     :  Software Engineering Student
Focus    :  Systems | Hardware | AI
Status   :  Building something. Always.
```

- **Hardware** — GPUs, mobile tech, consumer electronics
- **FPV Drones** — researching, occasionally flying
- **AI & Local Models** — running LLM experiments
- **Creative Writing** — long-form project on the side

<br clear="right"/>

---

### `> goals.txt`

```bash
[ ] Ship projects that actually solve real problems
[x] Get deep into systems programming and low-level dev
[x] Break into embedded systems / IoT / FPV
[ ] Contribute to open source
[ ] Build something people actually use
[ ] Get a job   # apparently GitHub profiles are not enough
```

---

### `> stack`

**Learning**

![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white)

**Tools**

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

---

### `> my best projects`

**[postflight](https://github.com/ItsMrZxD/postflight)** — reads the black-box flight recorder off an FPV drone and tells you what happened on that flight. Decodes Betaflight's compact binary log format from scratch — seven variable-length encodings, twelve delta predictors, and resynchronisation after the corruption that crashed logs routinely carry — then reports the flight and flags impacts, receiver dropouts, battery sag and logging overruns. Checked against the Betaflight firmware sources rather than guessed, and verified on real recordings from three flight controllers: 119,950 frames, zero decode errors.

```
flight 1 of 1 · AR8 · Betaflight 4.2.0 · HBRO KAKUTEF7
  duration       17.0 s
  battery        22.73 V → 21.47 V  (6S, min 2.93 V/cell)
  current        peak 119.8 A, 103 mAh used
  gyro           peak 37 / 197 / 43 deg/s
  gps            8 satellites, max 10 km/h, 25 m from home

warnings
  ⚠ voltage-sag: pack sagged to 2.93 V/cell, below the 3.30 V limit
```

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/postflight/ci.yml?branch=main&style=flat-square&label=CI)
![tests](https://img.shields.io/badge/tests-182%20passing-success?style=flat-square)
![dependencies](https://img.shields.io/badge/dependencies-0-success?style=flat-square)

**[hotseat-chess](https://github.com/ItsMrZxD/hotseat-chess)** — a complete chess game in a single self-contained HTML file: two-player hot-seat plus an AI opponent (Easy/Hard), full legal-move rules (castling, en passant, promotion, and all standard draws), and a live settings panel. Vanilla JS, no libraries.

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/hotseat-chess/ci.yml?branch=main&style=flat-square&label=CI)
![dependencies](https://img.shields.io/badge/dependencies-0-success?style=flat-square)

**[entity-resolver](https://github.com/ItsMrZxD/entity-resolver)** — fuzzy entity resolution in Python: matches records across two CSV datasets even when the names disagree — typos, abbreviations, legal suffixes, word order — and scores its own confidence so you know which matches to trust. Benchmarks three RapidFuzz similarity metrics and picks the default with data, not vibes.

```
"Apple Inc."          →  "Apple"                100.0
"Nvidia Corporaton"   →  "NVIDIA Corporation"    90.0
"Tesla Motors"        →  "Tesla Inc"             90.0
```

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/entity-resolver/ci.yml?branch=main&style=flat-square&label=CI)
![tests](https://img.shields.io/badge/tests-12%20passing-success?style=flat-square)

**[sysglance](https://github.com/ItsMrZxD/sysglance)** — a tiny zero-dependency CLI that prints a clean snapshot of your system (CPU, memory, disk, network, battery, temperature, OS, uptime). Pure Python standard library — no `pip install` required.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/sysglance/ci.yml?branch=main&style=flat-square&label=CI)
![dependencies](https://img.shields.io/badge/dependencies-0-success?style=flat-square)
![platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-informational?style=flat-square)

> _More on the way — just getting started._

---

### `> stats`

<div align="center">

<img src="https://github-readme-stats-eta-one-23.vercel.app/api?username=ItsMrZxD&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github&include_all_commits=true" height="165"/>
<img src="https://github-readme-streak-stats-eight.vercel.app/?user=ItsMrZxD&theme=tokyo-night&hide_border=true" height="165"/>

</div>

---

### `> snake`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ItsMrZxD/itsmrzxd/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/ItsMrZxD/itsmrzxd/output/github-contribution-grid-snake.svg"/>
  <img alt="github-contribution-grid-snake" src="https://raw.githubusercontent.com/ItsMrZxD/itsmrzxd/output/github-contribution-grid-snake.svg"/>
</picture>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>
