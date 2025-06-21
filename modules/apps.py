import os
import subprocess
from tts import speak

# Add aliases for common apps
app_aliases = {
    "vs code": "code",
    "visual studio code": "code",
    "chrome": "chrome",
    "firefox": "firefox",
    "notepad": "notepad",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "outlook": "outlook",
    "cmd": "cmd",
    "terminal": "cmd"
}

def open_application(query: str):
    app_name = query.lower().replace("open", "").strip()
    app_exe = app_aliases.get(app_name, app_name)

    speak(f"Attempting to open {app_name}, Sir.")

    # Try start command (PATH apps)
    try:
        subprocess.Popen(['start', '', app_exe], shell=True)
        return
    except:
        pass

    # Try 'where' command
    try:
        result = subprocess.run(['where', app_exe], stdout=subprocess.PIPE, text=True, shell=True)
        found_path = result.stdout.strip().split('\n')[0]
        if os.path.exists(found_path):
            subprocess.Popen(found_path)
            speak(f"{app_name} launched from system path.")
            return
    except:
        pass

    # Try Start Menu shortcuts
    start_menu_dirs = [
        os.path.join(os.environ['APPDATA'], r'Microsoft\Windows\Start Menu\Programs'),
        os.path.join(os.environ['PROGRAMDATA'], r'Microsoft\Windows\Start Menu\Programs')
    ]

    for base_dir in start_menu_dirs:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if app_name in file.lower() and file.endswith('.lnk'):
                    try:
                        os.startfile(os.path.join(root, file))
                        speak(f"Shortcut for {app_name} launched.")
                        return
                    except:
                        pass

    # Deep scan in Program Files
    program_dirs = [os.environ.get('ProgramFiles'), os.environ.get('ProgramFiles(x86)')]
    for prog_dir in program_dirs:
        if not prog_dir:
            continue
        for root, dirs, files in os.walk(prog_dir):
            for file in files:
                if file.lower().startswith(app_name) and file.endswith('.exe'):
                    try:
                        subprocess.Popen(os.path.join(root, file))
                        speak(f"{app_name} launched from Program Files.")
                        return
                    except:
                        pass

    speak(f"Sorry, I couldn’t locate {app_name} anywhere on your system.")
    speak("Please check the application name and try again.")