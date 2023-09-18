# PhishGuard Email Analyzer

![PhishGuard Logo](phishguard_logo.jpg)

## Overview

PhishGuard Email Analyzer is a command-line tool that allows you to analyze email content and links for potential phishing and spoofing attempts. It helps you identify suspicious emails by searching for specific keywords commonly used in phishing emails.

## Why This Tool?

Phishing attacks have become increasingly sophisticated, making it crucial to have tools that help identify potentially harmful emails. PhishGuard Email Analyzer serves as a reliable tool to quickly analyze email content and links, helping users identify suspicious elements that could be indicative of phishing attempts. By providing a simple yet effective way to analyze emails, this tool contributes to improved email security and user awareness.
## Features


- Email content analysis for phishing keywords detection.
- Link analysis to identify potential phishing links.
- Helps users identify suspicious emails.
- Command-line tool for easy and quick analysis.
- Designed to improve email security and user awareness.

## Getting Started

### Prerequisites

- Before using PhishGuard Email Analyzer, ensure you have the following prerequisites installed on your system:

- Python 3.x: This tool is written in Python, so you'll need Python 3.x installed.

- You can download Python from the official website: [Python Official Website](https://www.python.org/downloads/)

- Required Python packages: You'll need to install the following Python packages using 'pip':

  ```
  pip install prettytable pyfiglet colorama
  ```

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/00112244/phishguard-email-analyzer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd phishguard-email-analyzer
   ```

3. Install the required Python packages:

   ```bash
   pip install pyfiglet colorama
   ```

### Usage

To analyze an email, run the script with the path to a text file containing the email content and links:

```bash
python phishguard.py /path/to/email.txt
```

Example usage:

```bash
python phishguard.py sample_email.txt
```

## Author

This tool was developed by Hariharan T.

Thank you for using PhishGuard Email Analyzer! We appreciate your interest and welcome any feedback or contributions to make this tool even better. Stay safe and secure!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





