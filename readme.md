# Fast Map CLI

The Fast Map CLI is a command-line tool for fetching travel distances between two locations using the Google Maps API.

## Features

- Fetch travel distance between two locations.
- Utilizes the Google Maps API for accurate distance calculations.

## Prerequisites

Before using the Fast Map CLI, make sure you have the following:

- Python 3.6 or higher installed.
- A Google Maps API key. You can obtain one by following the [Google Maps API documentation](https://developers.google.com/maps/gmp-get-started).

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/thribhu/fast-map.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fast-map
   ```

3. Install the required dependencies:

   ```bash
   pipenv install
   ```

## Usage

To fetch the travel distance between two locations, use the following command:

```bash
pipenv run python cli.py "Origin Location" "Destination Location"
```

Replace `"Origin Location"` and `"Destination Location"` with the actual locations you want to calculate the distance for.

For example:

```bash
pipenv run python cli.py "New York" "Los Angeles"
```

This will display the travel distance between New York and Los Angeles.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Fast Map CLI uses the Google Maps API for distance calculations.
- Created by Thribhuvan Kumar DSVB
