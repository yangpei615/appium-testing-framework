import pytest
import os


pytest.main()


os.system('allure generate -c -o report allure-results')
