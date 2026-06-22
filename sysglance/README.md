# sysglance

A tiny, zero-dependency CLI that prints a clean snapshot of your system — CPU,
memory, disk, OS, and uptime. Pure Python standard library, so it runs anywhere
Python 3.8+ does, with no `pip install` required.

## Usage

```bash
python3 sysglance.py
```

Disable colored output (useful when piping to a file):

```bash
python3 sysglance.py --no-color
```

## Example output

```
sysglance
---------
User      mrz@laptop
OS        Linux 6.18.5
Arch      x86_64
Python    3.11.15
CPU       Intel(R) Xeon(R) Processor @ 2.80GHz
Cores     4
Memory    5.2 GB / 15.7 GB (33%)
Disk (~)  7.0 GB / 252.0 GB (3%)
Uptime    2d 4h 31m
```

## How it works

No third-party libraries — just the standard library poking at how the system
exposes its own state:

- **CPU / memory / uptime** are read from `/proc` on Linux, with `sysctl`
  fallbacks on macOS.
- **Disk** uses `shutil.disk_usage`.
- **OS / arch / Python** come from the `platform` module.

When information can't be determined on a given platform, the field falls back
to `n/a` instead of crashing.

## Why

A small learning project: practicing clean, dependency-free Python and getting
hands-on with how operating systems report their own state. Easy to extend —
good next steps would be temperature sensors, network interfaces, or a
`--json` output mode.

## License

MIT — see [LICENSE](LICENSE).
