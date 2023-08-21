from PIL import Image, ImageDraw, ImageFont, ImageOps
from datetime import datetime, date
import time
import subprocess
import os
import glob
import logging
import os

# Load .env values
def load_env():
    env_vars = {}
    with open('.env', 'r') as file:
        for line in file.readlines():
            key, value = line.strip().split('=')
            env_vars[key] = value
    return env_vars

ENV_VARS = load_env()


def generate_countdown_image(end_date, header, background_image_path=None):
    # Define image dimensions
    width, height = 1920, 1080
    
    if background_image_path:
        # Load the provided background image and resize it to the required dimensions
        image = Image.open(background_image_path)
        image = ImageOps.fit(image, (width, height))
    else:
        # Create an empty image with a light grey background
        image = Image.new('RGB', (width, height), 'darkgrey')
    
    draw = ImageDraw.Draw(image)
    draw = ImageDraw.Draw(image)

    # Create and position header text
    header_text = header
    header_font_size = 40
    header_font = ImageFont.truetype('/System/Library/Fonts/Supplemental/BigCaslon.ttf', header_font_size)
    header_dimensions = draw.textbbox((0, 0), header_text, font=header_font)
    header_position = ((width - (header_dimensions[2] - header_dimensions[0])) / 2, (height - (header_dimensions[3] - header_dimensions[1])) * 0.4)
    draw.text(header_position, header_text, fill="black", font=header_font)

    # Calculate remaining time until goal date and create countdown text
    goal_time = time.mktime(time.strptime(end_date, '%d-%m-%Y'))
    remaining_time = goal_time - time.time()
    countdown_text = f"{int(remaining_time // (60 * 60 * 24))} days " \
                 f"{int((remaining_time % (60 * 60 * 24)) // (60 * 60))} hours " \
                 f"{int((remaining_time % (60 * 60)) // 60)} minutes"


    # Create and position countdown text
    font_size = 30
    font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Futura.ttc', font_size)
    text_dimensions = draw.textbbox((0, 0), countdown_text, font=font)
    position = ((width - (text_dimensions[2] - text_dimensions[0])) / 2, (height - (text_dimensions[3] - text_dimensions[1])) * 0.45)
    draw.text(position, countdown_text, fill="black", font=font)

    # Save the image and log the update
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    image_path = os.path.join(ENV_VARS["WALLPAPER_DIR"], f'countdown_wallpaper_{timestamp}.jpg')
    image.save(image_path)
    update_log(timestamp)
    
    return image_path

def set_wallpaper(image_path):
    # Set the generated image as the desktop wallpaper
    absolute_image_path = os.path.abspath(image_path)
    command = f"osascript -e 'tell application \"System Events\" to tell every desktop to set picture to \"{absolute_image_path}\"'"
    subprocess.run(command, shell=True)

def update_log(timestamp):
    # Log the time of the wallpaper update
    logging.basicConfig(filename=ENV_VARS["LOG_PATH"], level=logging.DEBUG)
    logging.info(f'Wallpaper Timer last updated: {timestamp}')


def clean_old_wallpapers(directory, current_file):
    # Remove all previous countdown wallpapers, leaving only the current one
    wallpapers = glob.glob(os.path.join(directory, 'countdown_wallpaper_*.jpg'))
    wallpapers.remove(current_file)
    for wallpaper in wallpapers:
        os.remove(wallpaper)

def clear_logs(directory):
    # Clear log and error files once daily
    last_clear_file = os.path.join(directory, 'last_clear_date.log')
    try:
        with open(last_clear_file, 'r') as f:
            if f.readline().strip() == date.today().strftime("%Y-%m-%d"):
                return
    except FileNotFoundError:
        pass

    # Clear log and error files
    for file in glob.glob(os.path.join(directory, '*.log')) + glob.glob(os.path.join(directory, '*.error')):
        with open(file, 'w') as f:
            pass

    # Update the date of the last clear operation
    with open(last_clear_file, 'w') as f:
        f.write(date.today().strftime("%Y-%m-%d"))

def main():
    image_path = generate_countdown_image(ENV_VARS["END_DATE"], ENV_VARS['HEADER'], ENV_VARS['BACKGROUND_IMAGE']) # Remove background image if not using one
    set_wallpaper(image_path)
    clean_old_wallpapers(ENV_VARS["WALLPAPER_DIR"], image_path)
    clear_logs(ENV_VARS["LOG_DIR"]) # Clear log and error files if not already cleared today

if __name__ == '__main__':
    main()

