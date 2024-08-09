# Selenium Test Automation Framework with Pytest

## Overview
This repository contains a Selenium-based test automation framework using Pytest. It is designed to facilitate robust and scalable test automation for web applications, following best practices for maintainability and ease of use.

## Features
- **Cross-Browser Testing**: Supports multiple browsers (Chrome, Firefox).
- **Page Object Model (POM)**: Enhances test code maintainability.
- **Data-Driven Testing**: Easily integrate data from external sources (e.g., CSV, JSON).
- **Detailed Reporting**: Generates detailed test reports using HTML.

## Prerequisites
- Python 3.12 or higher
- Pip (Python package installer)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/WkjuniorDiaz/Pytest-Web-Automation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo
   ```
3. Install the required packages:
   ```bash
   pip install pytest
   ```
   ```bash
   pip install selenium
   ```

## Project Structure
- `tests`: Contains the test cases.
- `pageObjects`: Contains the Page Object Model (POM) classes.
- `utilities`: Stores general methods to use and log configuration.
- `reports`: Directory where test reports are saved.
- `testData`: Contains the data required for the test cases.

## Running Tests
### Run All Tests
To execute all test cases:
```bash
pytest
```

### Run Specific Test File
To run a specific test file:
```bash
pytest tests/test_your_test_file.py
```

### Run Tests with Custom Settings
To specify custom settings, such as the browser:
```bash
pytest --browser_name chrome
```

### Generate Reports
To generate a test report:
```bash
pytest --html=reports/report.html
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
