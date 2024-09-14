# Automatic Random Statistics Registration

## Overview

This project is designed to automate the process of registering random statistics on the (Hotel Management System) website of iran. The script uses Selenium to interact with the website and input data for various statistical parameters. The data is generated randomly within specified ranges and distributed across days within each month, ensuring accurate and realistic entries.

## Features

- **Automated Data Entry:** The script logs into the website and navigates to the appropriate page to input statistical data.
- **Random Data Generation:** Generates random values for different parameters (e.g., `eghamat`, `vorod`, `khoroj`, `otagh`) based on user-defined ranges and distributions.
- **Date Handling:** Supports generating and handling dates in the format `1402/03/03` and ensures that data for all days within the specified range is processed.

## Requirements

To run this project, you need the following Python libraries:

- `selenium==4.11.2`
- `webdriver-manager==3.8.6`
- `python-dateutil==2.8.2`

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Installation and Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ItsOrv/Hotels-amar.git
   cd Hotels-amar
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script:**

   ```bash
   python main.py
   ```

   Follow the prompts to enter the Email, number, captcha, and code for login. The script will then proceed to input the generated statistics into the website.

## Future Updates

### Telegram Bot Integration

In future updates, I plan to integrate a Telegram bot to manage and monitor the registration process. The bot will allow you to:

- **Start/Stop the Data Entry Process:** Control the execution of the script via Telegram commands.
- **Receive Updates and Logs:** Get real-time updates and logs about the data entry process.

### Docker Setup

We will also be adding Docker support to simplify the deployment and management of the project. The Docker setup will include:

- **Docker Compose Configuration:** For setting up the environment and dependencies.
- **Automated Deployment:** A streamlined process to deploy the project in a Docker container, making it easier to run and manage.

## Contributing

Contributions to the project are welcome! Please submit a pull request or open an issue to discuss improvements or report bugs.
