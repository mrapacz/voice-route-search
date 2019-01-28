# Voice route searching

This is a proof of concept of an app that joins VoiceLab's Polish speech recognition API with jakdojade (a trip planning app).

## Requirements
1. Make sure Selenium binary is installed and accessible.

2. Run
```bash
pip install -r requirements.txt
```

## Configuration

In order to run the app, you'll need to:
0. (optional) In case you want to use your location with jakdojade:
    - create a new Firefox profile
    - go to `jakdojade.pl` and, when asked, always allow location data
1. Create an empty `config.py` file
2. Therein declare the following constants:

```python
BEARER = "" # your VoiceLab authorization token
BINARY = "" # Absolute path to VoiceLab's binary
ADDR = "" # VoiceLab's grpc address
PORT = "" # VoiceLab's grpc port
FIREFOX_PROFILE_PATH = "" # Absolute path to your Firefox profile

VOICE = True
DEFAULT_TIMEOUT = 10

```

## Running

1. Run
```bash
python main.py
```
2. When `Listening...` prompt appears, speak and declare the route's source and destination as follows:
 ```
Miasteczko studenckie *w kierunku* czerwone maki`
```
 