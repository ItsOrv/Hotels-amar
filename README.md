# Automatic Random Statistics Registration

A Selenium-based automation script that logs into Iran's Hotel Management System
(`myst.mcth.ir`) and submits the daily hotel statistics report for a list of
dates, filling each form with random but realistic values.

> ⚠️ **Old practice project.** This was written as a learning exercise. It is
> not production-ready — some pieces are still unfinished (see [TODO.md](TODO.md))
> and the form is driven by brittle absolute XPaths. Use it for testing and
> educational purposes only.

## Overview

The daily statistics form on the portal has to be filled in by hand, one day at
a time. This script automates that: it reads a queue of dates, and for each one
it opens the registration form, generates random values for every field, types
them in, and submits.

The numbers it enters (`eghamat` / occupancy, `vorod` / check-ins,
`khoroj` / check-outs, `otagh` / rooms) are random within fixed ranges, so the
result looks like plausible day-to-day activity rather than constant values.

## How it works

1. **Login** — Chrome opens the login page; you are prompted in the terminal for
   email, phone number, captcha, and the verification code.
2. **Date queue** — dates to register are read from `date.txt`, one per line, in
   the format `1402/03/03`.
3. **Registration** — for each date the script opens the form, fills in random
   values, sets the date, and submits.
4. **Retry on failure** — `date.txt` acts as the work queue. It is cleared at the
   start of a run, and any rows that fail are written back so the next run
   retries only those.

## Project structure

| File              | Responsibility                                              |
| ----------------- | ----------------------------------------------------------- |
| `main.py`         | Entry point — wires up the browser and the steps below      |
| `config.py`       | Paths (ChromeDriver, Chromium, `date.txt`, log file)        |
| `login.py`        | Logs into the portal and opens the statistics page          |
| `registration.py` | Fills and submits the daily form for each date              |
| `algorithms.py`   | Random number generation                                   |
| `scraper.py`      | Asks whether to use `date.txt` or scrape dates *(WIP)*      |
| `data_handler.py` | Reads/writes the `date.txt` queue                           |
| `exceptions.py`   | `LoginError`, `RegistrationError`                           |

## Requirements

- Python 3.10+
- Google Chrome / Chromium and a matching ChromeDriver
- Python libraries:
  - `selenium==4.11.2`
  - `webdriver-manager==3.8.6`
  - `python-dateutil==2.8.2`

## Installation and Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ItsOrv/Hotels-amar.git
   cd Hotels-amar
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure paths** — edit `config.py` so `CHROMEDRIVER_PATH` and
   `CHROMIUM_PATH` point at your local Chrome/ChromeDriver install.

5. **Add dates** — create a `date.txt` file in the project root with one date
   per line (e.g. `1402/03/03`).

6. **Run the script:**

   ```bash
   python main.py
   ```

   Follow the terminal prompts to enter the email, number, captcha, and
   verification code. The script then registers the statistics for each date.

## Future Updates

- **Telegram bot integration** — start/stop the process and receive progress
  updates and logs via Telegram commands.
- **Docker setup** — a `docker-compose` configuration for easier deployment.
- **Real logging** — `config.LOG_FILE` is defined but not yet used; replace the
  `print` calls with proper logging.
- **Date scraper** — let the script scrape pending dates instead of relying on a
  hand-written `date.txt`.

See [TODO.md](TODO.md) for the full list of unfinished pieces.

## Disclaimer

**This project is intended for testing and educational purposes only.** It
submits randomly generated data into a real web portal; do not point it at any
system you are not explicitly authorized to use. Use of this script is at your
own risk — the author takes no responsibility for any issues or damages arising
from its use. By using it you agree to act responsibly and in accordance with
the terms and conditions of any service involved.

## Contributing

Contributions are welcome! Please open an issue to discuss improvements or
report bugs, or submit a pull request.
