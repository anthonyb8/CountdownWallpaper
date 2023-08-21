# Wallpaper Countdown Project

This project generates dynamic wallpapers showing a countdown to a specific date. It serves as a reminder of your goals and the time remaining to achieve them, directly on your desktop.

## Description

I created this tool to provide a continuous, visual reminder of an upcoming significant event. It's a constant motivator, ensuring that every glance at the desktop reminds me of the days, hours, and minutes left to my target date.

## Features

- **Dynamic Wallpaper Generation**: This feature allows for automatic generation of wallpapers with an updated countdown.
  
- **Automatic Updates**: With the integration of macOS's `launchd`, the wallpaper can be refreshed at defined intervals, ensuring the countdown is always accurate.

- **Logging**: The system keeps logs of every wallpaper update, ensuring that any issues can be quickly identified and addressed.

## How To Use

1. **Environment Setup**:
    - Navigate to the main project directory.
    - Create a `.env` file following the example in the [ENV-Template](ENV-template.txt) file.


2. **Run the Script**:
``` 
python src/main.py
```

3. **Automatic Wallpaper Update**:
    - Transfer the `com.<yourname>.wallpaper_countdown.plist` from the `launch_agents` directory to `~/Library/LaunchAgents/`.
    - Activate the plist with `launchd` using:
```
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.<yourname>.wallpaper_countdown.plist
```


4. **Software Requirements**:
    - Python 3.8.8
    - PIL (Python Imaging Library)
    - macOS (Tested on your macOS version; Ventura)

## Technologies

The project primarily utilizes:
- Python
- PIL (Python Imaging Library)
- macOS's launchd for periodic task scheduling

## License
MIT License
