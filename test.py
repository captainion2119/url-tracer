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
import json

# Selenium chrome driver -> For new webdrivers, workaround
driver = webdriver.Chrome(ChromeDriverManager().install())

# I will default the app to open a wikipedia page and start tracking
driver.get("https://en.wikipedia.org")

# List for visited urls...
visited_urls = []
continue_tracking = True

# Trace dict, has count var, url array
tracking_info = {
    "total_count": 0,  
    "urls_opened": []  
}

def track_urls():
    global visited_urls, tracking_info
    while continue_tracking:
        current_url = driver.current_url

        if current_url not in visited_urls:
            visited_urls.append(current_url)

            tracking_info["total_count"] += 1
            tracking_info["urls_opened"].append(current_url)

        # print("Current URL:", current_url)
        driver.implicitly_wait(10)

def dump_urls():
    # Save to file mechanic
    global continue_tracking, tracking_info
    continue_tracking = False

    # Json dumping here...
    with open("visited_urls.json", "w") as file:
        json.dump(tracking_info, file, indent=4)
    print("Visited URLs and tracking information saved to 'visited_urls.json'")

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
