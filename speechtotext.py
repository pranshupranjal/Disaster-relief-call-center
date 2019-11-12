import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# URL of what you want to scrape
url = "https://speechnotes.co/"

options = Options()
# Wherever your chrome is installed
options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

# path of web driver
path = r'C:\\Users\\pranjal\\Desktop\\git-waala\\Disaster-relief-call-center\\data sources\\chrome driver\\chromedriver_win32_v78\\Chromedriver'
driver = webdriver.Chrome(chrome_options=options, executable_path=path)

# provide the url
driver.get(url)

# start listening
driver.find_element_by_id('start_button').click()
driver.implicitly_wait(10)

# freeze program for 10 seconds
time.sleep(10)

# stop listening
driver.find_element_by_id('start_button').click()
driver.implicitly_wait(10)

# find text
# converted_text = driver.find_element_by_id('results_box')

# freeze program for 5 seconds
time.sleep(5)

# get converted text
ctext = driver.find_element_by_id('results_box').get_attribute('value')

# for debugging save the instance the textarea was scraped
driver.save_screenshot('processed_data/Scrapedatthisinstance.png')

print("\nYou said: \n")
print(ctext)

driver.close()

f = open("processed_data/isaid.txt", "w")
f.write(ctext)
f.close()
