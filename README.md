Below is the directory and file structure of the Appium + Pytest Mobile Automation Testing Framework:
appium-testing-framework/
├── .idea/                     # IDE configuration files (e.g., PyCharm)
├── __pycache__/               # Python bytecode cache (auto-generated, can be ignored)
├── allure-results/            # Raw Allure test results (generated during test execution)
├── commons/                   # Shared utilities and helper modules (e.g., base page, logger, wait methods)
├── logs/                      # Execution logs for debugging and traceability
├── report/                    # Generated Allure HTML reports (output from `allure serve`)
├── scripts/                   # Utility scripts (e.g., environment setup, device checks)
├── testcases/                 # Test case scripts using Pytest and Page Object Model (POM)
├── config.ini                 # Configuration file for device, app package, and environment settings
├── conftest.py                # Global Pytest fixtures (e.g., driver setup/teardown)
├── pytest.ini                 # Pytest configuration (plugins, markers, test paths)
└── run.py                     # Entry point to execute tests (e.g., `python run.py`)


How to Run:
# Install dependencies
pip install -r requirements.txt

# Run tests
python run.py

# Generate Allure report
allure serve report/

