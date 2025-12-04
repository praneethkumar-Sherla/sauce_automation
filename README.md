# Sauce Automation

Automated testing framework for Sauce Demo e-commerce website using Playwright, pytest, and Allure reporting.

## Overview

This project provides end-to-end test automation for the Sauce Demo website (https://www.saucedemo.com/). It implements the Page Object Model (POM) design pattern for maintainable and scalable test automation.

## Features

- **Playwright-based** browser automation
- **Page Object Model** architecture for maintainability
- **Allure reporting** with screenshots and step-by-step documentation
- **Multi-browser support** (Chromium, Firefox, WebKit)
- **Pytest framework** for test execution and fixtures
- **Comprehensive test coverage** for checkout flow

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Allure command-line tool


## Project Structure

```
sauce_automation/
├── pages/                  # Page Object Model classes
│   ├── login_page.py      # Login page interactions
│   ├── inventory_page.py  # Product inventory page
│   ├── cart_page.py       # Shopping cart page
│   └── checkout_page.py   # Checkout process page
├── tests/                 # Test cases
│   └── test_checkout_flow.py  # End-to-end checkout test
├── utils/                 # Utility classes
│   └── reporter.py        # Allure reporting utilities
├── conftest.py            # Pytest fixtures and configuration
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## Running Tests

### Run all tests

```bash
pytest
```

### Run tests with specific browser

```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Run with verbose output

```bash
pytest -v
```

### Run specific test file

```bash
pytest tests/test_checkout_flow.py
```

## Test Flow

The main test (`test_checkout_flow.py`) performs the following steps:

1. **Login** - Authenticates with default credentials
2. **Select Random Items** - Adds 3 random items to the shopping cart
3. **Cart Verification** - Verifies items are present in the cart
4. **Checkout** - Fills in checkout information
5. **Complete Order** - Finishes checkout and verifies success message

## Allure Reporting

After test execution, Allure reports are automatically generated and opened in your browser.

### Manual report generation

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```