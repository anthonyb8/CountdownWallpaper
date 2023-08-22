import subprocess
import generate_wallpaper
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

if __name__ == '__main__':
    # Check if plist exists; if not, generate it
    if not os.path.exists(os.path.expanduser(f"{os.getenv('PLIST_PATH')}.plist")):
        subprocess.run(["python3", "src/generate_plist.py"])
        print("-- New plist generated. --")

    # Run the countdown wallpaper script
    generate_wallpaper.main()
