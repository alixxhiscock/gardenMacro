# Super Farmer

## Introduction
This tool aims to make farming automated, except for having to remove pests.

<a href="https://github.com/alixxhiscock/gardenMacro/graphs/code-frequency" target="_blank">
    <img src="https://tokei.rs/b1/github/alixxhiscock/gardenMacro" alt="lines">
</a>

## Features
- **Hub Detection**: The macro automatically detects when you are in the hub and will teleport you to your garden if you're in the wrong location.
- **Auto Use Repellent**: Automatically uses the repellent for you.
- **Discord Notifier**:
  - **Screenshots**: Sends a screenshot of your monitor to Discord.
  - **Repellent Timing**: Sends a notification to Discord with the exact time the repellent expires.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alixxhiscock/gardenMacro.git
   pip install -r requirements.txt
2. Change .env
   
   Windows - `ren .env.example .env`

   
   Linux - `mv .env.example .env`


   Set values for  
   ```
   TOKEN=
   PLAYERNAME=
   IMAGEWEBHOOK=
   TIMEWEBHOOK=
   ```
3. Run gardenmacro.py and select options on the GUI.
4. Press the macro button, change the window to Minecraft, and press 'V' to start.
5. To stop it, press 'X'.
   
