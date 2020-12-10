# Automatic Random Statistics Registration

## Overview

This project is designed to automate the process of registering random statistics on the (Hotel Management System) website of iran. The script uses Selenium to interact with the website and input data for various statistical parameters. The data is generated randomly within specified ranges and distributed across days within each month, ensuring accurate and realistic entries.

## Features

- **Automated Data Entry:** The script logs into the website and navigates to the appropriate page to input statistical data.
- **Random Data Generation:** Generates random values for different parameters (e.g., `eghamat`, `vorod`, `khoroj`, `otagh`) based on user-defined ranges and distributions.
- **Date Handling:** Supports generating and handling dates in the format `1402/03/03` and ensures that data for all days within the specified range is processed.

## Requirements

To run this project, you need the following Python libraries:

- `selenium`
- `webdriver-manager`
- `python-dateutil`

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```
