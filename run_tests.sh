#!/bin/bash
pytest tests/ --alluredir=reports/allure
allure serve reports/allure