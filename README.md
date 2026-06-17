# Selenium PyTest Automation Framework

A scalable, maintainable, and extensible test automation framework built using Python, Selenium WebDriver, PyTest, and Requests.

The framework supports both **UI Automation** and **API Automation**, follows the **Page Object Model (POM)** design pattern, and includes centralized configuration management, screenshot capture, Allure reporting, environment-based execution, and reusable utilities.

---

## Tech Stack

| Component          | Technology                   |
| ------------------ | ---------------------------- |
| Language           | Python 3                     |
| UI Automation      | Selenium WebDriver           |
| API Automation     | Requests                     |
| Test Framework     | PyTest                       |
| Reporting          | Allure Reports               |
| Parallel Execution | pytest-xdist                 |
| Retry Mechanism    | pytest-rerunfailures         |
| Configuration      | YAML + Environment Variables |
| Test Data          | JSON                         |
| Design Pattern     | Page Object Model (POM)      |
| CI/CD              | Jenkins / GitHub Actions     |

---

## Framework Architecture

```text
project-root
│
├── api/
│   ├── events.py
│   └── ticket_booking.py
│
├── config/
│   ├── config_manager.py
│   └── qa.yaml
│
├── core/
│   ├── api_client.py
│   ├── auth_manager.py
│   ├── driver_manager.py
│   └── retry_handler.py
│
├── exceptions/
│   └── custom_exceptions.py
│
├── pages/
│   ├── base_page/
│   └── form_page/
│
├── test_data/
│   ├── event_data.json
│   └── bookings_data.json
│
├── tests/
│   ├── api_test/
│   └── ui_test/
│
├── utils/
│   ├── screenshot_utils.py
│   ├── logger.py
│   ├── json_reader.py
│   └── date_utils.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Key Design Decisions

| Design Decision          | Implementation                        | Benefit                                 |
| ------------------------ | ------------------------------------- | --------------------------------------- |
| Page Object Model        | Base Page + Feature Pages             | Easier maintenance and reusable actions |
| Configuration Management | YAML-based environment configuration  | Easy environment switching              |
| Screenshot Capture       | Automatic screenshot on test failures | Faster debugging                        |
| API Layer Separation     | Dedicated API modules                 | Cleaner test implementation             |
| Reusable Driver Factory  | DriverManager                         | Centralized browser management          |
| JSON Test Data           | Externalized test data files          | Better test maintainability             |
| Allure Reporting         | Integrated with PyTest hooks          | Rich execution reports                  |
| Retry Support            | pytest-rerunfailures                  | Handles flaky tests                     |

---

## Features

### UI Automation

* Selenium WebDriver
* Page Object Model (POM)
* Reusable page actions
* Cross-browser execution
* Headless execution support
* Automatic screenshot capture on failures

### API Automation

* REST API testing using Requests
* Reusable API client layer
* Authentication management
* Request and response validation

### Framework Utilities

* Environment-based configuration
* Centralized logging
* JSON test data management
* Custom exception handling
* Retry mechanism
* Parallel execution

---

## Supported Browsers

* Chrome
* Firefox

Browser configuration is managed through environment-specific YAML files.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Selenium-Pytest-Automation-Framework
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Packages

```text
pytest
selenium
allure-pytest
pytest-xdist
pytest-rerunfailures
requests
pyyaml
python-dotenv
```

---

## Running Tests

### Execute Complete Test Suite

```bash
pytest
```

### Run UI Tests

```bash
pytest tests/ui_test -v
```

### Run API Tests

```bash
pytest tests/api_test -v
```

### Execute Tests Against Environment

```bash
pytest --env=qa
```

### Parallel Execution

```bash
pytest -n auto
```

### Re-run Failed Tests

```bash
pytest --reruns 2
```

### Verbose Execution

```bash
pytest -v
```

---

## Allure Reporting

Generate Allure Results

```bash
pytest --alluredir=reports/allure-results
```

Generate Report

```bash
allure generate reports/allure-results --clean
```

Open Report

```bash
allure serve reports/allure-results
```

---

## Test Coverage

### UI Test Coverage

* Form validation
* Input field validation
* User interaction workflows
* End-to-end UI scenarios

### API Test Coverage

#### Events API

* Create Event
* Retrieve Event
* Update Event
* Delete Event

#### Ticket Booking API

* Create Booking
* Retrieve Booking
* Update Booking
* Cancel Booking

---

## Configuration Management

Environment-specific configurations are maintained in YAML files.

Example:

```yaml
browser: chrome
headless: false
base_url: https://example.com
```

Run using:

```bash
pytest --env=qa
```

---

## Reporting & Debugging

The framework provides:

* Allure Reports
* Failure Screenshots
* Execution Logs
* Request/Response Validation
* Detailed Assertion Messages

---

## CI/CD Ready

The framework can be integrated with:

* Jenkins
* GitHub Actions
* GitLab CI/CD
* Azure DevOps

Pipeline capabilities include:

* Automated execution
* Scheduled runs
* Allure report generation
* Artifact publishing
* Failure notifications

---

## Best Practices Implemented

* Page Object Model (POM)
* Reusable Components
* Environment-Based Configuration
* Externalized Test Data
* Separation of Concerns
* API/UI Layer Isolation
* Screenshot Capture on Failure
* Rich Reporting
* CI/CD Friendly Design

---

## Author

Santhosh S

Senior QA Engineer | Test Automation | API Testing | Selenium | PyTest
