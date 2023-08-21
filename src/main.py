import subprocess
import generate_wallpaper

if __name__ == '__main__':
    # Generate plist
    subprocess.run(["python3", "src/generate_plist.py"])

    # Run the countdown wallpaper script
    generate_wallpaper.main()
