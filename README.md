# Selenium Pytest Automation Framework


### Packages required
    pytest
    selenium
    allure-pytest
    pytest-xdist
    pytest-rerunfailures
    requests
    pyyaml
    dotenv


````markdown
# Selenium Python PyTest Automation Framework

A scalable and maintainable test automation framework built using Selenium WebDriver, Python, and PyTest. The framework follows the Page Object Model (POM) design pattern to improve code reusability, readability, and maintainability.

## Features

- Selenium WebDriver with Python
- PyTest test runner
- Page Object Model (POM)
- Reusable utilities and fixtures
- Environment-based configuration
- Parallel test execution
- HTML and Allure reporting
- Screenshot capture on test failures

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <project-folder>
````

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run tests in parallel:

```bash
pytest -n auto
```

Run tests with verbose output:

```bash
pytest -v
```

## Generate Reports

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

View Allure report:

```bash
allure serve allure-results
```

```

This is the style most recruiters and GitHub visitors prefer—short, focused, and easy to follow.
```
