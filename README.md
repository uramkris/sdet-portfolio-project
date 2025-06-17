
# SDET Portfolio Project

![CI](https://github.com/uramkris/sdet-portfolio-project/actions/workflows/ci.yml/badge.svg)

# "SauceMaster" - A Hybrid Test Automation Framework

This project is a demonstration of a modern test automation framework built for a portfolio. It uses Python, Selenium, and Pytest to test the UI of the e-commerce site [Swag Labs](https://www.saucedemo.com/). It also includes API tests and is configured to run in a Docker container and a CI/CD pipeline using GitHub Actions.

## Key Features & Skills Demonstrated

*   **Programming Language:** Python
*   **UI Automation:** Selenium WebDriver
*   **Test Framework:** Pytest (with fixtures for setup/teardown)
*   **Design Pattern:** Page Object Model (POM) for maintainable and scalable test code.
*   **API Testing:** Using the `requests` library to test RESTful endpoints.
*   **Reporting:** `pytest-html` for generating shareable test reports.
*   **Containerization:** `Docker` to create a consistent and portable testing environment.
*   **CI/CD:** `GitHub Actions` to automate test execution on every code push.

## How to Run

### 1. Running Locally

**Prerequisites:** Python 3.9+, Git

1.  Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/sdet-portfolio-project.git
    cd sdet-portfolio-project
    ```
2.  Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  Run all tests:
    ```bash
    pytest
    ```
4.  To generate an HTML report:
    ```bash
    pytest --html=reports/report.html
    ```

### 2. Running with Docker

**Prerequisites:** Docker Desktop

1.  Build the Docker image:
    ```bash
    docker build -t sdet-tests .
    ```
2.  Run the tests inside the container:
    ```bash
    docker run sdet-tests
    ```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration. The pipeline is configured in `.github/workflows/ci.yml` and is triggered on every push to the `main` branch. It performs the following steps:
1.  Checks out the code.
2.  Sets up the Python environment.
3.  Installs dependencies and Google Chrome.
4.  Executes the entire `pytest` suite.
5.  Uploads the test execution report as a downloadable artifact.