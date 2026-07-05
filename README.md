# python_packaging_example_2

A simple example of creating a Python package for weather forecast data using the OpenWeatherMap API.

[![Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Package Manager](https://img.shields.io/pypi/v/sunnyday-IP.svg)](https://pypi.org/project/sunnyday-IP/)

## Introduction

This project demonstrates how to create a Python package for fetching weather forecast data from the OpenWeatherMap API. It provides a simple and easy-to-use interface for developers to integrate weather data into their applications.

The primary workflow involves installing the package, configuring it with your OpenWeatherMap API key, and using the provided functions to fetch weather forecasts.

## Features

- **Fetch Weather Data**: Retrieve current weather conditions, forecasted temperatures, humidity, and more.
- **Easy Installation**: Install via pip for quick setup.
- **Comprehensive Documentation**: Detailed README and examples included.

## How It Works

The package uses the `requests` library to make HTTP requests to the OpenWeatherMap API. The main functionality is encapsulated in the `sunnyday.py` module, which provides functions to fetch weather data based on city names or geographic coordinates.

### Architecture Diagram

```
+-------------------+
|  sunnyday.py      |
|                   |
| - get_current_weather(city) |
| - get_forecast(city)    |
+-------------------+
          |
          v
+-------------------+
|  requests         |
|                   |
| - make_request(url, params) |
+-------------------+
```

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python     | The programming language used for the package. |
| Requests   | A library for making HTTP requests to the OpenWeatherMap API. |

## Requirements

- Python 3.5 or later
- An active OpenWeatherMap account with an API key

## Installation

To install the package, run:

```bash
pip install sunnyday-IP==2.0.0
```

## Configuration

You need to set your OpenWeatherMap API key as an environment variable:

```bash
export OPENWEATHERMAP_API_KEY='your_api_key_here'
```

## Quick Start

Here's a quick example of how to use the package:

```python
from sunnyday import get_current_weather, get_forecast

# Fetch current weather for New York City
current_weather = get_current_weather('New York')
print(current_weather)

# Fetch 5-day forecast for London
forecast = get_forecast('London')
print(forecast)
```

## Usage

You can find more usage examples and detailed documentation in the [README.md](README.md) file.

## Project Structure

```plaintext
.
├── .gitignore
├── README.md
├── dist/
│   ├── sunnyday-2.0.0.tar.gz
│   ├── sunnyday-IP-1.0.0.tar.gz
│   ├── sunnyday-IP-1.0.1.tar.gz
│   └── sunnyday-IP-2.0.0.tar.gz
├── setup.py
├── sunnyday.egg-info/
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
└── sunnyday/
    ├── __init__.py
    └── sunnyday.py
```

## Development

To develop the package, clone the repository and install the development dependencies:

```bash
git clone https://github.com/PartORG/python_packaging_example_2.git
cd python_packaging_example_2
pip install -e .
```

## Testing

This project does not include tests at this time.

## Limitations

- The package only supports fetching weather data for cities and geographic coordinates.
- No error handling is included in the example usage.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.