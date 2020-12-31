# TODO

Known incomplete bits and things to come back to. None of these break the
current flow (simple random + existing date.txt), they are just unfinished.

## Random number generation

- `algorithms.choose_rand` option 2 (random distribution over a fixed monthly
  total) calls `auto_detect_numbers`, which is an empty stub. Implement the
  distribution logic or drop the option.
- `algorithms.distribute_random_numbers` and `algorithms.auto_detect_numbers`
  are still empty placeholders.
- `choose_rand` returns the ranges as strings from `input()`. Once it is wired
  back into `register_amar`, convert them to int and actually use them instead
  of the hardcoded ranges.

## Date scraping

- `scraper.choose_date_file` only asks the y/n question and returns the choice.
  The "n" path is supposed to scrape the dates instead of reading date.txt, but
  there is no scraper yet. Build it and have `main` act on the returned choice.

## Logging

- `config.LOG_FILE` is defined but nothing writes to it. Set up real logging and
  replace the `print` calls in registration/algorithms.

## Cleanup

- `utils.generate_random_numbers` is unused. Either use it or remove utils.py.

## From the README

- Telegram bot to start/stop and report progress.
- Docker / docker-compose setup.
