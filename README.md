# Webcam IP

## How it works

To set up and use the Webcam IP program, follow these steps:

### Create a Python Virtual Environment

```bash
$> python -m venv .venv
```

### Activate the Virtual Environment

```bash
$> source .venv/bin/activate   # On Windows, use .venv\Scripts\activate
```

If the virtual environment is activated successfully, you will see (venv) on the left side of your terminal.

### Install Dependencies

```bash
$> pip install -r requirements.txt
```

### Run the Python Code

```bash
$> python __init__.py
```

If everything is set up correctly, you will see localhost IP addresses in the console. Open your browser and enter the following address:

```js
http://127.0.0.1:1234
```

Now you can view your webcam using a local IP address.

## Observation

This script is designed for testing purposes and allows the video to be displayed for only one request per device. For example, if you try to access the video from both a mobile device and a PC, the PC's request will take drop, and the camera feed will only be visible on the mobile device.