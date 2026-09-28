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
[x] Ship projects that actually solve real problems
[x] Get deep into systems programming and low-level dev
[x] Break into embedded systems / IoT / FPV
[x] Publish an app on the Microsoft Store        # Flylet, live
[ ] Build something people actually use          # in progress: real users are starting to send bug reports
[ ] Get Flylet into winget
[ ] Contribute to open source
[ ] Get a job   # apparently GitHub profiles are not enough
```

---

### `> stack`

**Learning**

![C#](https://img.shields.io/badge/C%23-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![.NET](https://img.shields.io/badge/.NET_10-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![XAML](https://img.shields.io/badge/WPF%20%2F%20XAML-0C54C2?style=for-the-badge&logo=windows&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
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

**[Flylet](https://github.com/ItsMrZxD/Flylet)** — modern, Fluent-style replacements for the Windows volume, brightness, media and lock-key pop-ups, live on the [Microsoft Store](https://apps.microsoft.com/detail/9NPSS6NW7T23). A maintained continuation of the archived ModernFlyouts (MIT). It hides Windows' own pop-up by hooking window events on `explorer.exe`, then draws its own above it with the undocumented `CreateWindowInBand`. Fixed a media timeline that froze between reports, made it work on Windows 11, and ships 31 fully translated languages, custom colors and a live-following accent color. Every release goes through the Store's certification, with unit tests on every push.

![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![.NET](https://img.shields.io/badge/.NET_10-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![release](https://img.shields.io/github/v/release/ItsMrZxD/Flylet?style=flat-square)
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/Flylet/tests.yml?branch=main&style=flat-square&label=tests)
![Microsoft Store](https://img.shields.io/badge/Microsoft%20Store-live-success?style=flat-square&logo=microsoftstore&logoColor=white)

**[betaflight-blackbox-parser](https://github.com/ItsMrZxD/betaflight-blackbox-parser)** — reads the black-box flight recorder off an FPV drone and tells you what happened on that flight. Decodes Betaflight's compact binary log format from scratch — seven variable-length encodings, twelve delta predictors, and resynchronisation after the corruption that crashed logs routinely carry — then reports the flight and flags impacts, receiver dropouts, battery sag and logging overruns. Checked against the Betaflight firmware sources rather than guessed, and verified on real recordings from three flight controllers: 119,950 frames, zero decode errors.

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
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/betaflight-blackbox-parser/ci.yml?branch=main&style=flat-square&label=CI)
![tests](https://img.shields.io/badge/tests-182%20passing-success?style=flat-square)
![dependencies](https://img.shields.io/badge/dependencies-0-success?style=flat-square)

**[fuzzy-entity-matching](https://github.com/ItsMrZxD/fuzzy-entity-matching)** — fuzzy entity resolution in Python: matches records across two CSV datasets even when the names disagree — typos, abbreviations, legal suffixes, word order — and scores its own confidence so you know which matches to trust. Benchmarks three RapidFuzz similarity metrics and picks the default with data, not vibes.

```
"Apple Inc."          →  "Apple"                100.0
"Nvidia Corporaton"   →  "NVIDIA Corporation"    90.0
"Tesla Motors"        →  "Tesla Inc"             90.0
```

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/ItsMrZxD/fuzzy-entity-matching/ci.yml?branch=main&style=flat-square&label=CI)
![tests](https://img.shields.io/badge/tests-12%20passing-success?style=flat-square)

**Smaller projects:** [browser-chess-ai](https://github.com/ItsMrZxD/browser-chess-ai) (chess with a minimax AI in one HTML file) · [python-sysinfo-cli](https://github.com/ItsMrZxD/python-sysinfo-cli) (zero-dependency system snapshot) · [password-generator](https://github.com/ItsMrZxD/password-generator) (secure CLI generator) · [cpp-todo-cli](https://github.com/ItsMrZxD/cpp-todo-cli) (C++ task manager)

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
