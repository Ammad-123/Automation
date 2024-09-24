from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

# wait for website to be loaded successfuly
driver.implicitly_wait(5)   #irs work same like  time.sleep(5)
#

my_element  = driver.find_element(By.ID,"downloadButton")
my_element.click()


progress_element =  driver.find_element(By.CLASS_NAME,"progress-label")
print(f'{progress_element.text}')

# print(f"{progress_element.text == 'Complete!'}") ## Explicity wait means on condition
WebDriverWait(driver,30).until(
    EC.text_to_be_present_in_element(
    (By.CLASS_NAME,"progress-label"),  # Element filtration
    "Complete!"                         # The Expected text
    )
)
print(f'{progress_element.text}')


#
# print("its working ...")