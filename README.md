# 🟢 Ping Monitor

A minimalist script for macOS menu bar app that shows a green circle when a target address is reachable, and a red circle when it's not.

## Preview

```
🟢  ←  host is reachable
🔴  ←  host is unreachable
```

## Requirements

- macOS
- Python 3.7+
- pip

## Installation

```bash
# Clone the repository
git clone https://github.com/username/ping-monitor.git
cd ping-monitor

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

The icon will appear in the menu bar. To quit, click the icon and select **Quit**.

## Configuration

Edit the following variables in `app.py`:

```python
TARGET = "8.8.8.8"  # address or domain to ping
INTERVAL = 5        # check interval in seconds
```

## Building a standalone .app

To run the app without a terminal:

```bash
pip install py2app
python setup.py py2app
```

The built application will appear in the `dist/` folder and can be moved to `/Applications`.

## Dependencies

| Package | Purpose |
|---------|---------|
| [rumps](https://github.com/jaredks/rumps) | macOS menu bar apps in Python |
| [py2app](https://py2app.readthedocs.io/) | Build standalone .app bundles (optional) |
