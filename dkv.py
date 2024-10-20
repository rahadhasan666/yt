import os
import sys
import time
import platform
import subprocess

# Auto install required packages
def install_packages():
    try:
        import selenium
    except ImportError:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "chromedriver-autoinstaller"])

def display_banner():
    banner = '''
     ▄████████  ▄█  ███    █▄  ███▄▄▄▄   ███    █▄     ▄████████    ▄████████ 
    ███    ███ ███  ███    ███ ███▀▀▀██▄ ███    ███   ███    ███   ███    ███ 
    ███    ███ ███▌ ███    ███ ███   ███ ███    ███   ███    ███   ███    █▀  
    ███    ███ ███▌ ███    ███ ███   ███ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     
    ███    ███ ███▌ ███    ███ ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
    ███    ███ ███  ███    ███ ███   ███ ███    ███ ▀███████████   ███    █▄  
    ███    ███ ███  ███    ███ ███   ███ ███    ███   ███    ███   ███    ███ 
    ███    █▀  █▀   ████████▀   ▀█   █▀  ████████▀    ███    ███   ██████████ 
                                                     ███    ███ 

                      Created by: Rahad Hasan
    '''
    for line in banner.splitlines():
        print(line)
        time.sleep(0.05)  # Animation effect

def view_video(video_link):
    try:
        import chromedriver_autoinstaller
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        
        # Auto-download ChromeDriver if not installed
        chromedriver_autoinstaller.install()
        
        # Setup Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode (no GUI)
        options.add_argument("--mute-audio")  # Mute audio
        
        print("Launching browser...")
        driver = webdriver.Chrome(service=Service(), options=options)
        driver.get(video_link)

        # Check if the video page loaded
        time.sleep(5)  # Wait for the page to load
        print(f"Started viewing: {video_link}")

        # Keep the video open for a while to count as a view
        view_time = 30  # Time in seconds for each view
        print(f"Viewing video for {view_time} seconds to count as a view.")
        time.sleep(view_time)

        driver.quit()
        print("Video view complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    install_packages()

    # Display banner animation
    display_banner()

    # Ask for YouTube video link
    video_link = input("Enter the YouTube video link (e.g. https://youtu.be/F-0oiDmhHAg?si=UapBlDGrhNs1SLKh): ")

    # Start auto view process
    view_video(video_link)

if __name__ == "__main__":
    main()