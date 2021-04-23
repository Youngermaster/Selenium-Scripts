# Selenium-Scripts

This repo contains some Selenium scripts I'm using to learn Selenium

## Setup

### Python package

Make sure to install the following packages:

```
pip install selenium
pip install python-dotenv
```

**Note:** If you are using MacOs or Linux, maybe you should use `pip3` instead of `pip`.

### Web Drivers

- Download the [web driver](https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/)
of the browser you will use.

- Add the driver/s to the path, [learn more](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).

If everything goes right you will be able to run almost every tutorial.

## Examples

### EAFIT_daily_health_report.py

To be able to run the `EAFIT_daily_health_report.py` script you have create a `.env` file that looks
like this:

```
EMAIL=email@email.com
PASSWORD=1234567890
```