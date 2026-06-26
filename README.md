# Lightnovel Crawler

[![download win](https://img.shields.io/badge/download-lncrawl.exe-red?logo=windows&style=for-the-badge)](https://go.bitanon.dev/lncrawl-windows)
[![download linux](<https://img.shields.io/badge/download-lncrawl_(linux)-brown?logo=linux&style=for-the-badge>)](https://go.bitanon.dev/lncrawl-linux)
[![download mac](<https://img.shields.io/badge/download-lncrawl_(mac)-blue?logo=apple&style=for-the-badge>)](https://go.bitanon.dev/lncrawl-mac)
<br>
[![PyPI version](https://img.shields.io/pypi/v/lightnovel-crawler.svg?logo=python)](https://pypi.org/project/lightnovel-crawler)
[![Python version](https://img.shields.io/pypi/pyversions/lightnovel-crawler.svg)](https://pypi.org/project/lightnovel-crawler)
[![Downloads](https://pepy.tech/badge/lightnovel-crawler)](https://pepy.tech/project/lightnovel-crawler)
[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/lncrawl/lightnovel-crawler/blob/master/LICENSE)
<br>
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/lncrawl/lightnovel-crawler)
[![Lint](https://github.com/lncrawl/lightnovel-crawler/actions/workflows/lint.yml/badge.svg)](https://github.com/lncrawl/lightnovel-crawler/actions/workflows/lint.yml)
[![Build and Publish](https://github.com/lncrawl/lightnovel-crawler/actions/workflows/release.yml/badge.svg)](https://github.com/lncrawl/lightnovel-crawler/actions/workflows/release.yml)

**Lightnovel Crawler** downloads web novels and similar fiction from hundreds of online reading sites and saves them as e-books — so you can read offline on your phone, tablet, or e-reader.

- Download a story you follow as a single EPUB instead of bookmarking hundreds of web pages.
- Run a private home server to collect and read all your novels in one place.

> **Personal use only.** Sites publish fiction under their own terms and copyright. Only use this tool for personal backups of content you have legitimate access to. Do not redistribute or sell someone else's work.

## Quick Start

| I want to…        | How                                     |
| ----------------- | --------------------------------------- |
| Just try it       | [Download the executable](#-standalone) |
| Use the CLI       | [pip install](#-pip)                    |
| Run a home server | [Docker](#-docker)                      |

Once it's running: open **http://localhost:8181**, sign in with `admin` / `admin`, and paste a novel URL to download it.

---

## Installation

<a href="https://github.com/lncrawl/lightnovel-crawler"><img src="res/lncrawl-icon.png" width="128px" align="right"/></a>

Pick **one** of the three methods below.

### ⏬ Standalone

Download and run — no Python required.

| Platform | Download                                                 |
| -------- | -------------------------------------------------------- |
| Windows  | [📦 lncrawl.exe](https://go.bitanon.dev/lncrawl-windows) |
| Linux    | [📦 lncrawl](https://go.bitanon.dev/lncrawl-linux)       |
| macOS    | [📦 lncrawl](https://go.bitanon.dev/lncrawl-mac)         |

_Check [Releases](https://github.com/lncrawl/lightnovel-crawler/releases) for older versions._

**Windows:** Double-click the downloaded `.exe`. SmartScreen may warn about an unknown app — click "More info → Run anyway". Setup is required before first run.

**macOS / Linux:** No setup needed. Make the file executable and run it:

```bash
chmod +x lncrawl
./lncrawl
```

[![Tutorial](res/screenshots/tutorial.png)](res/screenshots/tutorial.png)

### 📦 pip

Requires Python 3.11+.

```bash
pip install -U lightnovel-crawler
```

_If it fails, try `python -m pip install -U lightnovel-crawler`._

To install directly from GitHub:

```bash
# Latest stable
pip install -U git+https://github.com/lncrawl/lightnovel-crawler.git#egg=lightnovel-crawler

# Development branch (latest fixes but unstable)
pip install -U https://github.com/lncrawl/lightnovel-crawler/tarball/refs/heads/dev#egg=lightnovel-crawler
```

Verify the install:

```bash
lncrawl -h
```

_If `lncrawl` is not found, use `python -m lncrawl -h` instead._

<!-- auto generated command line output -->
```text
$ lncrawl -h
Usage: lncrawl [OPTIONS] COMMAND [ARGS]...                                     
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --verbose             -l            Log levels: -l = warn, -ll = info, -lll  │
│                                     = debug                                  │
│ --config              -c      PATH  Config file                              │
│ --install-completion                Install completion for the current       │
│                                     shell.                                   │
│ --show-completion                   Show completion for the current shell,   │
│                                     to copy it or customize the              │
│                                     installation.                            │
│ --help                -h            Show this message and exit.              │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ app      Launches the web application.                                       │
│ version  Show current version.                                               │
│ config   View and modify configuration settings.                             │
│ sources  Manage sources.                                                     │
│ crawl    Crawl from novel page URL.                                          │
│ search   Search for novels by query string.                                  │
│ server   Run web server.                                                     │
╰──────────────────────────────────────────────────────────────────────────────╯
```
<!-- auto generated command line output -->

### 🐳 Docker

Requires [Docker](https://www.docker.com/get-started/).

```bash
mkdir -p lncrawl-data
docker pull ghcr.io/lncrawl/lightnovel-crawler
docker run -v ./lncrawl-data:/data -it -p 8181:8181 --name lncrawl-server ghcr.io/lncrawl/lightnovel-crawler -ll server
```

Then open **http://localhost:8181** and sign in with `admin` / `admin`.

[![Login](res/screenshots/login.png)](res/screenshots/login.png)

---

## Using the App

### Web interface

The web UI lets you browse, download, and read novels without touching the command line.

**Start the server:**

- **Standalone / pip:** run `lncrawl server`.
- **Docker:** the server starts with the `docker run` command above.

**Open in browser:** Visit **http://localhost:8181**.

**First-time login:** `admin` / `admin`. Change your password in **Settings → Account**.

**Downloading a novel:**

1. Go to **Crawlers** to browse supported sites, or paste a novel URL directly into the search bar.
2. Select the chapters you want (a range or all of them).
3. Choose an output format (see [Output Formats](#output-formats) below).
4. Click **Download** — track progress on the **Requests** page.
5. Open the result in the built-in **Reader**, or download the file to your device.

**Library:** Save novels to your Library to re-download new chapters with one click whenever the story updates.

[![Crawlers](res/screenshots/crawlers.png)](res/screenshots/crawlers.png)
[![Requests](res/screenshots/requests.png)](res/screenshots/requests.png)
[![Novels](res/screenshots/novels.png)](res/screenshots/novels.png)
[![Reader](res/screenshots/reader.png)](res/screenshots/reader.png)
[![Libraries](res/screenshots/libraries.png)](res/screenshots/libraries.png)
[![Settings](res/screenshots/settings.png)](res/screenshots/settings.png)

**Common examples:**

```bash
# Open as application (no login)
lncrawl app

# Run as a server (has login)
lncrawl server

# Download the first 10 chapters as EPUB
lncrawl crawl "https://example.com/novel/page" -f epub --first 10

# Download all chapters
lncrawl crawl "https://example.com/novel/page" -f epub --all

# Search by title
lncrawl search "The Beginning After The End"
```

_Use a URL from any [supported source](#supported-sources)._

---

## Output Formats

| Format      | Needs Calibre | Best for                        |
| ----------- | :-----------: | ------------------------------- |
| 📚 **EPUB** |               | Most e-readers and reading apps |
| 📃 **TXT**  |               | Simple reading, any text editor |
| 🗂️ **JSON** |               | Scripts and developers          |
| 📄 **PDF**  |       ✓       | Print-ready, universal          |
| 🔳 **AZW3** |       ✓       | Kindle (current)                |
| 🔲 **MOBI** |       ✓       | Kindle (older devices)          |
| 📝 **DOCX** |       ✓       | Word, LibreOffice               |
| 📑 **RTF**  |       ✓       | WordPad and others              |
| 📔 **FB2**  |       ✓       | FB2 readers                     |
| 📕 **LIT**  |       ✓       | MS Reader (obsolete)            |
| 📗 **LRF**  |       ✓       | Sony readers                    |
| 🗄️ **PDB**  |       ✓       | PalmOS (legacy)                 |
| 📘 **RB**   |       ✓       | RocketBook/REB1100              |
| 📙 **TCR**  |       ✓       | Psion readers                   |

### Calibre (optional)

Install [Calibre](https://calibre-ebook.com/download) to unlock the formats marked above.

- **macOS / Linux:** No extra configuration — `ebook-convert` is detected automatically after installing Calibre.
- **Windows:** After installing, add the Calibre folder to your `Path` (default: `C:\Program Files\Calibre2`).

---

## Contributing

Contributions are welcome — bug fixes, new sources, documentation, and more.

![Repobeats](https://repobeats.axiom.co/api/embed/ecf3e93f676c27ba6404315e22523033d50aab45.svg "Repobeats analytics image")

See [**CONTRIBUTING.md**](.github/CONTRIBUTING.md) for setup instructions, code style, and how to add a source crawler.

- [CI on forks](.github/FORKING.md)
- [AI-assisted project overview (DeepWiki)](https://deepwiki.com/lncrawl/lightnovel-crawler)

### Local dev setup

Install [uv](https://docs.astral.sh/uv/) first (or let `make setup` install it for you).

```bash
git clone https://github.com/lncrawl/lightnovel-crawler.git
cd lightnovel-crawler
make install   # install uv + syncs dependencies
make start     # runs the dev server
```

Or with uv directly:

```bash
uv sync --all-extras --all-groups
uv run python -m lncrawl -ll server
```

<details>
<summary>Full Makefile reference</summary>

```bash
# Setup
make setup            # install uv
make install          # setup + uv sync (default: `make`)
make sync             # uv sync only
make upgrade          # setup + uv sync --upgrade

# Dev
make start            # Run dev server
make watch            # Run with auto-reload
make lint             # ruff format and check

# Version (writes lncrawl/VERSION)
make patch            # bump patch version
make minor            # bump minor version
make major            # bump major version

# Build
make build            # Full build: wheel + exe
make build-wheel      # Python wheel only
make build-exe        # PyInstaller exe only

# Dependencies
make add-dep <pkg>    # Add runtime dependency
make add-dev <pkg>    # Add dev dependency
make rm-dep <pkg>     # Remove runtime dependency
make rm-dev <pkg>     # Remove dev dependency

# Docker
make docker-build     # Build base + app images
make docker-up        # docker compose up -d
make docker-down      # docker compose down
make docker-logs      # docker compose logs -f

# Misc
make clean            # Remove .venv, build artifacts, caches
make version          # Print current version
```

</details>

### Adding a new source

Copy one of the example file from [sources/\_examples/](sources/_examples) into `sources/{lang}/` and implement the required methods.

Full guide: [.github/docs/CREATING_CRAWLERS.md](.github/docs/CREATING_CRAWLERS.md)

---

## Supported Sources

To request a new source, please [create an issue](https://github.com/lncrawl/lightnovel-crawler/issues/new/choose).

<details>
<summary>Click to expand</summary>

<!-- auto generated supported sources list -->

We are supporting 340 sources and 394 crawlers.

### `~` Unknown

<table>
<tbody>
<tr><th></th>
<th>Source URL</th>
<th>Version</th>
<th>Contributors</th>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://es.mtlnovels.com/" target="_blank">http://es.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://fr.mtlnovels.com/" target="_blank">http://fr.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://id.mtlnovels.com/" target="_blank">http://id.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://www.mtlnovels.com/" target="_blank">http://www.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://18.foxaholic.com/" target="_blank">https://18.foxaholic.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/foxaholic.py" title="02 April 2026 04:44:44 PM (UTC+0)">84</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/watzeedzad"><img src="https://avatars.githubusercontent.com/u/16551821?v=4&s=24" alt="watzeedzad" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://es.mtlnovels.com/" target="_blank">https://es.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://foxaholic.com/" target="_blank">https://foxaholic.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/foxaholic.py" title="02 April 2026 04:44:44 PM (UTC+0)">84</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/watzeedzad"><img src="https://avatars.githubusercontent.com/u/16551821?v=4&s=24" alt="watzeedzad" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://fr.mtlnovels.com/" target="_blank">https://fr.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://global.foxaholic.com/" target="_blank">https://global.foxaholic.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/foxaholic.py" title="02 April 2026 04:44:44 PM (UTC+0)">84</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/watzeedzad"><img src="https://avatars.githubusercontent.com/u/16551821?v=4&s=24" alt="watzeedzad" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://id.mtlnovels.com/" target="_blank">https://id.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://my.w.tt/" target="_blank">https://my.w.tt/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/wattpad.py" title="16 May 2026 04:51:10 PM (UTC+0)">75</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://wtr-lab.com/" target="_blank">https://wtr-lab.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/wtrlab.py" title="22 May 2026 12:46:36 PM (UTC+0)">21</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://www.foxaholic.com/" target="_blank">https://www.foxaholic.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/foxaholic.py" title="02 April 2026 04:44:44 PM (UTC+0)">84</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/watzeedzad"><img src="https://avatars.githubusercontent.com/u/16551821?v=4&s=24" alt="watzeedzad" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://www.mtlnovels.com/" target="_blank">https://www.mtlnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/mtlnovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">31</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://www.novelupdates.com/" target="_blank">https://www.novelupdates.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/novelupdates.py" title="02 June 2026 07:30:14 PM (UTC+0)">14</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://www.quotev.com/" target="_blank">https://www.quotev.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/quotev.py" title="01 April 2026 05:15:05 PM (UTC+0)">8</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://www.wattpad.com/" target="_blank">https://www.wattpad.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/wattpad.py" title="16 May 2026 04:51:10 PM (UTC+0)">75</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://www.webfic.com/" target="_blank">https://www.webfic.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/multi/webfic.py" title="06 May 2026 05:05:04 PM (UTC+0)">8</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
</tbody>
</table>


### `ar` Arabic

<table>
<tbody>
<tr><th></th>
<th>Source URL</th>
<th>Version</th>
<th>Contributors</th>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://arnovel.me/" target="_blank">https://arnovel.me/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/ar/arnovel.py" title="06 April 2026 06:15:39 AM (UTC+0)">27</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://kolnovel.com/" target="_blank">https://kolnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/ar/kolnovel.py" title="23 February 2023 12:26:02 AM (UTC+0)">1</a></td>
<td></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://rewayat.club/" target="_blank">https://rewayat.club/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/ar/rewayatclub.py" title="12 June 2026 08:44:54 PM (UTC+0)">15</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
</tbody>
</table>


### `en` English

<table>
<tbody>
<tr><th></th>
<th>Source URL</th>
<th>Version</th>
<th>Contributors</th>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://lightnovels.live/" target="_blank">http://lightnovels.live/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelme.py" title="09 May 2026 06:08:01 PM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://novelfull.com/" target="_blank">http://novelfull.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelfull.py" title="26 March 2024 06:17:03 AM (UTC+0)">50</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://readlightnovel.online/" target="_blank">http://readlightnovel.online/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelreader.py" title="02 April 2026 04:44:44 PM (UTC+0)">21</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://readonlinenovels.com/" target="_blank">http://readonlinenovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/r/readonlinenovels.py" title="01 April 2026 05:15:05 PM (UTC+0)">70</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/amritoo"><img src="https://avatars.githubusercontent.com/u/45586379?v=4&s=24" alt="amritoo" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="http://zenithnovels.com/" target="_blank">http://zenithnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/z/zenithnovels.py" title="06 April 2026 06:15:39 AM (UTC+0)">21</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://88tangeatdrinkread.wordpress.com/" target="_blank">https://88tangeatdrinkread.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/8/88tang.py" title="01 April 2026 05:15:05 PM (UTC+0)">75</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://allnovel.org/" target="_blank">https://allnovel.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/allnovel.py" title="22 March 2026 09:34:05 AM (UTC+0)">49</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://allnovelfull.com/" target="_blank">https://allnovelfull.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/allnovelfull.py" title="02 September 2025 06:36:20 PM (UTC+0)">9</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://allnovelfull.net/" target="_blank">https://allnovelfull.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/allnovelfull.py" title="02 September 2025 06:36:20 PM (UTC+0)">9</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://americanfaux.com/" target="_blank">https://americanfaux.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/americanfaux.py" title="01 April 2026 05:15:05 PM (UTC+0)">5</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://ancientheartloss.wordpress.com/" target="_blank">https://ancientheartloss.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/ancientheartloss.py" title="01 April 2026 05:15:05 PM (UTC+0)">77</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://api.babelnovel.com/" target="_blank">https://api.babelnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/babelnovel.py" title="13 May 2026 11:40:54 AM (UTC+0)">35</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://aquareader.net/" target="_blank">https://aquareader.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/aquamanga.py" title="13 June 2026 10:10:06 PM (UTC+0)">82</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://aquareader.org/" target="_blank">https://aquareader.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/aquamanga.py" title="13 June 2026 10:10:06 PM (UTC+0)">82</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://arcanetranslations.com/" target="_blank">https://arcanetranslations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/arcanetranslations.py" title="22 March 2026 09:34:05 AM (UTC+0)">4</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://automtl.wordpress.com/" target="_blank">https://automtl.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/a/automtl.py" title="06 April 2026 06:15:39 AM (UTC+0)">72</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://babelnovel.com/" target="_blank">https://babelnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/babelnovel.py" title="13 May 2026 11:40:54 AM (UTC+0)">35</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://bakapervert.wordpress.com/" target="_blank">https://bakapervert.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bakapervert.py" title="01 April 2026 05:15:05 PM (UTC+0)">76</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://batotoo.com/" target="_blank">https://batotoo.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://batotwo.com/" target="_blank">https://batotwo.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://battwo.com/" target="_blank">https://battwo.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://bednovel.com/" target="_blank">https://bednovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bednovel.py" title="02 April 2026 04:44:15 PM (UTC+0)">1</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://bestlightnovel.com/" target="_blank">https://bestlightnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bestlightnovel.py" title="06 April 2026 06:15:39 AM (UTC+0)">29</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://bonnovel.com/" target="_blank">https://bonnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bonnovel.py" title="06 April 2026 06:15:39 AM (UTC+0)">86</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://booknet.com/" target="_blank">https://booknet.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/booknet.py" title="02 April 2026 04:44:44 PM (UTC+0)">10</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://chapmanganato.com/" target="_blank">https://chapmanganato.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/r/readmanganato.py" title="01 April 2026 05:15:05 PM (UTC+0)">64</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://chrysanthemumgarden.com/" target="_blank">https://chrysanthemumgarden.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/c/chrysanthemumgarden.py" title="01 April 2026 05:15:05 PM (UTC+0)">21</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://ckandawrites.online/" target="_blank">https://ckandawrites.online/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/c/ckandawrites.online.py" title="23 July 2024 06:43:35 PM (UTC+0)">2</a></td>
<td></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://coffeemanga.io/" target="_blank">https://coffeemanga.io/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/c/coffeemanga.py" title="06 April 2026 06:15:39 AM (UTC+0)">22</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://comiko.net/" target="_blank">https://comiko.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://comrademao.com/" target="_blank">https://comrademao.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/c/fu_kemao.py" title="13 May 2026 11:40:54 AM (UTC+0)">20</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://creativenovels.com/" target="_blank">https://creativenovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/c/creativenovels.py" title="06 April 2026 06:15:39 AM (UTC+0)">37</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://crescentmoon.blog/" target="_blank">https://crescentmoon.blog/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/c/crescentmoon.py" title="01 April 2026 05:15:05 PM (UTC+0)">62</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://daotranslate.com/" target="_blank">https://daotranslate.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/daotranslate.py" title="01 April 2026 05:15:05 PM (UTC+0)">23</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://daotranslate.us/" target="_blank">https://daotranslate.us/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/daotranslate.py" title="01 April 2026 05:15:05 PM (UTC+0)">23</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://demontranslations.com/" target="_blank">https://demontranslations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/demontrans.py" title="06 April 2026 06:15:39 AM (UTC+0)">71</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://dmtranslationscn.com/" target="_blank">https://dmtranslationscn.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/dmtrans.py" title="01 April 2026 05:15:05 PM (UTC+0)">65</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://dobelyuwai.wordpress.com/" target="_blank">https://dobelyuwai.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/dobelyuwai.py" title="06 April 2026 06:15:39 AM (UTC+0)">81</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://dobytranslations.com/" target="_blank">https://dobytranslations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/dobytranslations.py" title="08 August 2025 03:52:11 PM (UTC+0)">2</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://dragontea.ink/" target="_blank">https://dragontea.ink/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/dragon_tea.py" title="01 April 2026 05:15:05 PM (UTC+0)">20</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://dto.to/" target="_blank">https://dto.to/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://dummynovels.com/" target="_blank">https://dummynovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/d/dummynovels.py" title="02 April 2026 04:44:44 PM (UTC+0)">8</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://ebotnovel.com/" target="_blank">https://ebotnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/e/ebotnovel.py" title="23 July 2024 06:12:46 PM (UTC+0)">2</a></td>
<td></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://engnovel.com/" target="_blank">https://engnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/e/engnovel.py" title="06 April 2026 06:15:39 AM (UTC+0)">5</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://exiledrebelsscanlations.com/" target="_blank">https://exiledrebelsscanlations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/e/exiledrebels.py" title="01 April 2026 05:15:05 PM (UTC+0)">71</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://f-w-o.com/" target="_blank">https://f-w-o.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/f/fantasyworldonline.py" title="06 April 2026 06:15:39 AM (UTC+0)">73</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://faqwiki.us/" target="_blank">https://faqwiki.us/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/f/faqwiki.py" title="06 April 2026 06:15:39 AM (UTC+0)">15</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://fenrirealm.com/" target="_blank">https://fenrirealm.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/f/fenrirealm.py" title="26 April 2026 08:18:39 PM (UTC+0)">7</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://freemanga.me/" target="_blank">https://freemanga.me/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/f/freemanga.py" title="06 April 2026 06:15:39 AM (UTC+0)">80</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://freewebnovel.com/" target="_blank">https://freewebnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/f/freewebnovel.py" title="08 May 2026 11:45:33 PM (UTC+0)">37</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://genesistls.com/" target="_blank">https://genesistls.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/g/genesistls.py" title="06 April 2026 06:15:39 AM (UTC+0)">6</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://home.novel-gate.com/" target="_blank">https://home.novel-gate.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelgate.py" title="03 April 2026 06:55:06 PM (UTC+0)">27</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://hostednovel.com/" target="_blank">https://hostednovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/h/hostednovel.py" title="01 April 2026 05:15:05 PM (UTC+0)">11</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://hto.to/" target="_blank">https://hto.to/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://hui3r.wordpress.com/" target="_blank">https://hui3r.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/h/hui3r.py" title="06 April 2026 06:15:39 AM (UTC+0)">67</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://inadequatetranslations.wordpress.com/" target="_blank">https://inadequatetranslations.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/i/inadequatetrans.py" title="01 April 2026 05:15:05 PM (UTC+0)">74</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://infinitenoveltranslations.net/" target="_blank">https://infinitenoveltranslations.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/i/infinitetrans.py" title="01 April 2026 05:15:05 PM (UTC+0)">70</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://innread.com/" target="_blank">https://innread.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/i/innread.py" title="02 April 2026 04:44:15 PM (UTC+0)">1</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://isotls.com/" target="_blank">https://isotls.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/i/isotls.py" title="01 April 2026 05:15:05 PM (UTC+0)">66</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://jpmtl.com/" target="_blank">https://jpmtl.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/j/jpmtl.py" title="06 April 2026 06:15:39 AM (UTC+0)">69</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://justatranslatortranslations.com/" target="_blank">https://justatranslatortranslations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/j/justatrans.py" title="06 April 2026 06:15:39 AM (UTC+0)">70</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://katreadingcafe.com/" target="_blank">https://katreadingcafe.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/k/katreadingcafe.py" title="12 June 2026 04:53:32 PM (UTC+0)">8</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://king-manga.com/" target="_blank">https://king-manga.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/k/kingmanga.py" title="06 April 2026 06:15:39 AM (UTC+0)">79</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://kissmanga.in/" target="_blank">https://kissmanga.in/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/k/kissmanga.py" title="06 April 2026 06:15:39 AM (UTC+0)">81</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://latestnovel.net/" target="_blank">https://latestnovel.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/latestnovel.py" title="02 April 2026 04:44:44 PM (UTC+0)">80</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/watzeedzad"><img src="https://avatars.githubusercontent.com/u/16551821?v=4&s=24" alt="watzeedzad" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lazybirdtranslations.wordpress.com/" target="_blank">https://lazybirdtranslations.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/ladybirdtrans.py" title="06 April 2026 06:15:39 AM (UTC+0)">70</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lazygirltranslations.com/" target="_blank">https://lazygirltranslations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lazygirltranslations.py" title="02 April 2026 04:44:44 PM (UTC+0)">16</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://leafstudio.site/" target="_blank">https://leafstudio.site/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/leafstudio.py" title="02 April 2026 04:44:44 PM (UTC+0)">4</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lemontreetranslations.wordpress.com/" target="_blank">https://lemontreetranslations.wordpress.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lemontree.py" title="01 April 2026 05:15:05 PM (UTC+0)">73</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://librarynovel.com/" target="_blank">https://librarynovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/librarynovel.py" title="02 April 2026 04:44:44 PM (UTC+0)">11</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://libread.com/" target="_blank">https://libread.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/libread_com.py" title="02 April 2026 04:44:15 PM (UTC+0)">1</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://libread.org/" target="_blank">https://libread.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/libread_org.py" title="02 April 2026 04:44:15 PM (UTC+0)">1</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovel.world/" target="_blank">https://lightnovel.world/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelworld.py" title="01 April 2026 05:15:05 PM (UTC+0)">65</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovelheaven.com/" target="_blank">https://lightnovelheaven.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelheaven.py" title="06 April 2026 06:15:39 AM (UTC+0)">72</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovelpub.org/" target="_blank">https://lightnovelpub.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelpuborg.py" title="13 June 2026 09:37:36 PM (UTC+0)">5</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovelreader.me/" target="_blank">https://lightnovelreader.me/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelreader.py" title="02 April 2026 04:44:44 PM (UTC+0)">21</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovels.live/" target="_blank">https://lightnovels.live/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelme.py" title="09 May 2026 06:08:01 PM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovelsonl.com/" target="_blank">https://lightnovelsonl.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelsonl.py" title="06 April 2026 06:15:39 AM (UTC+0)">24</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lightnovelstranslations.com/" target="_blank">https://lightnovelstranslations.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovetrans.py" title="02 June 2026 07:30:14 PM (UTC+0)">20</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/zerty"><img src="https://avatars.githubusercontent.com/u/4232921?v=4&s=24" alt="zerty" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lnmtl.com/" target="_blank">https://lnmtl.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lnmtl.py" title="12 June 2026 08:44:54 PM (UTC+0)">106</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://lnreader.org/" target="_blank">https://lnreader.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/l/lightnovelreader.py" title="02 April 2026 04:44:44 PM (UTC+0)">21</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a> <a href="https://github.com/mesmerlord"><img src="https://avatars.githubusercontent.com/u/76161333?v=4&s=24" alt="mesmerlord" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://m.readlightnovel.cc/" target="_blank">https://m.readlightnovel.cc/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/r/readlightnovelcc.py" title="02 April 2026 04:44:44 PM (UTC+0)">17</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://m.webnovel.com/" target="_blank">https://m.webnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/w/webnovel.py" title="02 June 2026 07:30:14 PM (UTC+0)">102</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangabuddy.com/" target="_blank">https://mangabuddy.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangabuddy.py" title="02 April 2026 04:44:44 PM (UTC+0)">11</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangachill.love/" target="_blank">https://mangachill.love/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangachilllove.py" title="06 April 2026 06:15:39 AM (UTC+0)">17</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangarosie.love/" target="_blank">https://mangarosie.love/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangarosie.py" title="06 April 2026 06:15:39 AM (UTC+0)">82</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangarosie.me/" target="_blank">https://mangarosie.me/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangarosie.py" title="06 April 2026 06:15:39 AM (UTC+0)">82</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://mangatoon.mobi/" target="_blank">https://mangatoon.mobi/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangatoon.py" title="02 April 2026 04:44:44 PM (UTC+0)">12</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangatoto.net/" target="_blank">https://mangatoto.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangatoto.org/" target="_blank">https://mangatoto.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangatx.com/" target="_blank">https://mangatx.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangatx.py" title="02 April 2026 04:44:44 PM (UTC+0)">80</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mangaweebs.in/" target="_blank">https://mangaweebs.in/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mangaweebs.py" title="06 April 2026 06:15:39 AM (UTC+0)">80</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://manhuaplus.online/" target="_blank">https://manhuaplus.online/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/manhuaplus.py" title="06 April 2026 06:15:39 AM (UTC+0)">22</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://miraslation.net/" target="_blank">https://miraslation.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/miraslation.py" title="01 April 2026 05:15:05 PM (UTC+0)">66</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://mltnovels.com/" target="_blank">https://mltnovels.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mltnovels.py" title="10 October 2022 03:39:48 PM (UTC+0)">4</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://mostnovel.com/" target="_blank">https://mostnovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mostnovel.py" title="02 April 2026 04:44:44 PM (UTC+0)">12</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://mtlreader.com/" target="_blank">https://mtlreader.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mtlreader.py" title="02 April 2026 04:44:44 PM (UTC+0)">8</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa">🖼️</span></td>
<td><a href="https://mto.to/" target="_blank">https://mto.to/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/b/bato.py" title="13 May 2026 11:40:54 AM (UTC+0)">13</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/CryZFix"><img src="https://avatars.githubusercontent.com/u/13964422?v=4&s=24" alt="CryZFix" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://mydramanovel.com/" target="_blank">https://mydramanovel.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mydramanovel.py" title="06 April 2026 06:15:39 AM (UTC+0)">10</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://mysticalmerries.com/" target="_blank">https://mysticalmerries.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/m/mysticalmerries.py" title="01 April 2026 05:15:05 PM (UTC+0)">71</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://newnovel.org/" target="_blank">https://newnovel.org/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/newnovelorg.py" title="19 October 2022 08:32:28 PM (UTC+0)">67</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://noblemtl.com/" target="_blank">https://noblemtl.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/noblemtl.py" title="10 October 2022 04:30:09 PM (UTC+0)">10</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novel-bin.com/" target="_blank">https://novel-bin.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novel-bin.py" title="07 May 2026 01:59:09 AM (UTC+0)">4</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novel-bin.net/" target="_blank">https://novel-bin.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novel-bin.net.py" title="12 May 2026 07:22:11 AM (UTC+0)">2</a></td>
<td><a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novel27.com/" target="_blank">https://novel27.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novel27.py" title="06 April 2026 06:15:39 AM (UTC+0)">72</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelbin.com/" target="_blank">https://novelbin.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelbin.py" title="12 May 2026 07:22:11 AM (UTC+0)">77</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/zerty"><img src="https://avatars.githubusercontent.com/u/4232921?v=4&s=24" alt="zerty" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelbin.me/" target="_blank">https://novelbin.me/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novel-bin.py" title="07 May 2026 01:59:09 AM (UTC+0)">4</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelbin.net/" target="_blank">https://novelbin.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelbin.net.py" title="29 November 2022 03:01:01 PM (UTC+0)">1</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations">🤖</span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelbuddy.io/" target="_blank">https://novelbuddy.io/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelbuddy.py" title="02 June 2026 07:30:14 PM (UTC+0)">8</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelfire.net/" target="_blank">https://novelfire.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelfire.py" title="02 June 2026 11:44:45 AM (UTC+0)">17</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelfull.com/" target="_blank">https://novelfull.com/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelfull.py" title="26 March 2024 06:17:03 AM (UTC+0)">50</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching"></span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelfull.me/" target="_blank">https://novelfull.me/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelfullme.py" title="02 April 2026 04:44:44 PM (UTC+0)">7</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/jere344"><img src="https://avatars.githubusercontent.com/u/86294972?v=4&s=24" alt="jere344" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelfull.net/" target="_blank">https://novelfull.net/</a></td>
<td><a href="https://github.com/lncrawl/lightnovel-crawler/blob/7647d8991d95511eb6738c9012ead6a0e2e8ca5b/sources/en/n/novelfull.py" title="26 March 2024 06:17:03 AM (UTC+0)">50</a></td>
<td><a href="https://github.com/dipu-bd"><img src="https://avatars.githubusercontent.com/u/5158124?v=4&s=24" alt="dipu-bd" height="24"/></a> <a href="https://github.com/yudilee"><img src="https://avatars.githubusercontent.com/u/7065691?v=4&s=24" alt="yudilee" height="24"/></a> <a href="https://github.com/idMysteries"><img src="https://avatars.githubusercontent.com/u/11484976?v=4&s=24" alt="idMysteries" height="24"/></a> <a href="https://github.com/SirGryphin"><img src="https://avatars.githubusercontent.com/u/36343615?v=4&s=24" alt="SirGryphin" height="24"/></a> <a href="https://github.com/kuwoyuki"><img src="https://avatars.githubusercontent.com/u/51709703?v=4&s=24" alt="kuwoyuki" height="24"/></a> <a href="https://github.com/Galunid"><img src="https://avatars.githubusercontent.com/u/10298730?v=4&s=24" alt="Galunid" height="24"/></a></td>
</tr>
<tr><td><span title="Contains machine translations"></span><span title="Supports searching">🔍</span><span title="Supports login"></span><span title="Contains manga/manhua/manhwa"></span></td>
<td><a href="https://novelgate.net/" target="_blank">https://novelgate.net/</a></td>
