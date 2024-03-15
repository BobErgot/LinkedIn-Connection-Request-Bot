# LinkedIn-Connection-Request_Bot

## Description

This Python script automates the process of sending connection requests on LinkedIn. It navigates through a list of LinkedIn profile URLs, extracted from a CSV file, and attempts to send connection requests to each profile. Utilizing the `selenium` package, the script automates browser interactions to log into LinkedIn, navigate to each profile, and send a connection request if possible.

## Features

- Automated login to LinkedIn.
- Navigation through a list of profile URLs from a CSV file.
- Automated sending of connection requests.
- Handling of various scenarios where the connection request button may be located differently.

## Prerequisites

Before you can run this script, you will need:

- Python 3.x installed on your system.
- `pandas` and `selenium` Python packages installed.
- Firefox Web Browser.
- GeckoDriver (Firefox WebDriver) installed and correctly placed in your PATH or specified in the script.

## Installation

1. **Clone this repository** or download the script file to your local machine.

2. **Install the required Python packages** using the `requirements.txt` file included in the repository. Run the following command in your terminal:

   ```sh
   pip install -r requirements.txt
   ```
3. **Download GeckoDriver**: Ensure you have GeckoDriver, which is required for Firefox browser automation. Download it from [Mozilla's GitHub](https://github.com/mozilla/geckodriver/releases) page. Select the version compatible with your operating system and Firefox version. After downloading, extract the executable to a known location on your machine.

4. **Configure the Script**: Before running the script, make sure to adjust the path to GeckoDriver and your LinkedIn credentials within the script. Find the following lines and update them accordingly:

   ```python
   service = Service('path/to/your/geckodriver.exe')  # Replace with your GeckoDriver path
   ...
   username.send_keys("your_email_here")  # Replace with your LinkedIn login email
   password.send_keys("your_password_here")  # Replace with your LinkedIn password```

5. **Prepare the LinkedIn database CSV file**: Ensure you have a linkedin_database.csv file with 
profile URLs in the expected format. The script reads URLs from the third column (index 2) of each row.

## Usage 

To run the script, refer commands.txt file.

> Note: This script automates actions on your LinkedIn account. Use it responsibly to avoid potential breaches of LinkedIn's terms of service.

## Disclaimer 

This tool is for educational purposes only. Automated actions on LinkedIn, especially for sending connection requests, can violate LinkedIn's terms of service. Use this script at your own risk. The author(s) of this script are not responsible for any potential consequences of using it.
