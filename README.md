# Auto Generated System Monitor

This repository contains a Python script that monitors system CPU and memory usage. It periodically prints the current CPU and memory usage to the console. The tool is useful for observing system resource utilization over time.

## Features

- Reports CPU usage percentage.
- Reports memory usage percentage.
- Configurable reading interval.
- Configurable number of iterations for limited runs.

## Installation

1. Clone this repository or download the `main.py` file.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

```
python main.py [-h] [-i INTERVAL] [-n ITERATIONS]
```

- `-i`, `--interval` — Interval between readings in seconds (default: 1.0).
- `-n`, `--iterations` — Number of readings to display (default: 5). Use 0 for infinite loop.

For example, to monitor your system with a half-second interval for 10 readings:

```
python main.py -i 0.5 -n 10
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
