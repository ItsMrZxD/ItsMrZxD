#!/usr/bin/env python3
"""sysglance - a tiny, zero-dependency snapshot of your system.

Prints CPU, memory, disk, OS, and uptime using only the Python standard
library. Works on Linux and macOS, with graceful fallbacks elsewhere.
"""
from __future__ import annotations

import argparse
import os
import platform
import shutil
import socket
import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
GREEN = "\033[32m"


def supports_color() -> bool:
    """True if stdout is an interactive terminal that likely supports ANSI."""
    return sys.stdout.isatty() and os.name != "nt"


def paint(text: str, color: str, enable: bool) -> str:
    return f"{color}{text}{RESET}" if enable else text


def human_bytes(n: float) -> str:
    """Format a byte count as a short human-readable string."""
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if n < 1024.0:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} EB"


def cpu_model() -> str:
    """Best-effort CPU model name across platforms."""
    try:
        with open("/proc/cpuinfo") as fh:
            for line in fh:
                if line.lower().startswith("model name"):
                    return line.split(":", 1)[1].strip()
    except OSError:
        pass
    if platform.system() == "Darwin":
        try:
            import subprocess

            out = subprocess.check_output(
                ["sysctl", "-n", "machdep.cpu.brand_string"], text=True
            )
            return out.strip()
        except Exception:
            pass
    return platform.processor() or "Unknown CPU"


def mem_info() -> tuple[int | None, int | None]:
    """Return (total_bytes, available_bytes), or (None, None) if unknown."""
    try:
        fields = {}
        with open("/proc/meminfo") as fh:
            for line in fh:
                key, _, val = line.partition(":")
                fields[key.strip()] = val.strip()
        total = int(fields["MemTotal"].split()[0]) * 1024
        avail = int(fields.get("MemAvailable", fields["MemFree"]).split()[0]) * 1024
        return total, avail
    except (OSError, KeyError, ValueError, IndexError):
        return None, None


def uptime_seconds() -> float | None:
    """Seconds since boot, or None if it can't be determined."""
    try:
        with open("/proc/uptime") as fh:
            return float(fh.read().split()[0])
    except (OSError, ValueError, IndexError):
        pass
    if platform.system() == "Darwin":
        try:
            import subprocess

            out = subprocess.check_output(["sysctl", "-n", "kern.boottime"], text=True)
            boot = int(out.split("sec =")[1].split(",")[0])
            return max(0.0, time.time() - boot)
        except Exception:
            pass
    return None


def fmt_uptime(secs: float | None) -> str:
    if secs is None:
        return "n/a"
    secs = int(secs)
    days, rem = divmod(secs, 86400)
    hours, rem = divmod(rem, 3600)
    mins, _ = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    parts.append(f"{mins}m")
    return " ".join(parts)


def gather() -> list[tuple[str, str]]:
    """Collect the rows of system information to display."""
    user = os.environ.get("USER") or os.environ.get("USERNAME") or "unknown"
    rows = [
        ("User", f"{user}@{socket.gethostname()}"),
        ("OS", f"{platform.system()} {platform.release()}"),
        ("Arch", platform.machine()),
        ("Python", platform.python_version()),
        ("CPU", cpu_model()),
        ("Cores", str(os.cpu_count() or "?")),
    ]

    total, avail = mem_info()
    if total and avail is not None:
        used = total - avail
        rows.append(
            ("Memory", f"{human_bytes(used)} / {human_bytes(total)} ({used / total * 100:.0f}%)")
        )
    else:
        rows.append(("Memory", "n/a"))

    disk = shutil.disk_usage(os.path.expanduser("~"))
    rows.append(
        ("Disk (~)", f"{human_bytes(disk.used)} / {human_bytes(disk.total)} ({disk.used / disk.total * 100:.0f}%)")
    )
    rows.append(("Uptime", fmt_uptime(uptime_seconds())))
    return rows


def render(rows: list[tuple[str, str]], color: bool) -> None:
    title = "sysglance"
    rule = "-" * len(title)
    if color:
        print(f"{BOLD}{CYAN}{title}{RESET}")
        print(f"{DIM}{rule}{RESET}")
    else:
        print(title)
        print(rule)
    width = max(len(key) for key, _ in rows)
    for key, value in rows:
        print(f"{paint(f'{key:<{width}}', GREEN, color)}  {value}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="A tiny snapshot of your system.")
    parser.add_argument("--no-color", action="store_true", help="disable colored output")
    args = parser.parse_args(argv)
    render(gather(), supports_color() and not args.no_color)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
