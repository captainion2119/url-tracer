# ------------------ URL TRACKER ------------------
# To do:
#   Track url from wikipedia...
#   Keep track of visited sites...
#   Save the url to a text file...
# -------------------------------------------------

import tkinter as tk
import threading
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Selenium chrome driver -> For new webdrivers, workaround
driver = webdriver.Chrome(ChromeDriverManager().install())

# I will default the app to open a wikipedia page and start tracking
driver.get("https://en.wikipedia.org")

# List for visited urls...
visited_urls = []
continue_tracking = True

def track_urls():
    global visited_urls
    while continue_tracking:
        current_url = driver.current_url

        if current_url not in visited_urls:
            visited_urls.append(current_url)

        driver.implicitly_wait(10)

def dump_urls():
    # Save to file mechanic
    with open("visited_urls.txt", "w") as file:
        for url in visited_urls:
            file.write(url + "\n")
    print("Visited URLs saved to 'visited_urls.txt'")

def stop_tracking():
    global continue_tracking
    continue_tracking = False

# Thread management section
url_tracking_thread = threading.Thread(target=track_urls)
url_tracking_thread.start()

# Tkinter stuff... ignore :]
root = tk.Tk()
root.title("URL Tracker")
dump_button = tk.Button(root, text="Dump", command=dump_urls)
dump_button.pack()
stop_button = tk.Button(root, text="Stop Tracking", command=stop_tracking)
stop_button.pack()
root.mainloop()
url_tracking_thread.join()

# Quit.
driver.quit()
