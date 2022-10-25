
from sqlalchemy import true
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import json
import time
import os

def run_speedtest():
  capabilities =     {
        "xcodeOrgId": "XXX",
        "xcodeSigningId": "iPhone Developer",
        'platformName': 'iOS',
        'platformVersion': '15.6.1',
        'automationName': 'XCUITest',
        'browserName': 'Safari',
        'deviceName': 'iPad',
        'udid': "XXX",
        'showXcodeLog': "true"
      }
        # 'updatedWDABundleId': 'com.francesco.prappium',

  driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)


  SHORT_TIME=2
  LONG_TIME=120
  XPATH_BANNER='//*[@id="onetrust-accept-btn-handler"]'
  XPATH_GO='//span[@class="start-text"]'

  XPATH_PING =     '//span[@class="result-data-value ping-speed"]'
  XPATH_DOWNLOAD = '//span[@class="result-data-large number result-data-value download-speed"]'
  XPATH_UPLOAD =   '//span[@class="result-data-large number result-data-value upload-speed"]'

  XPATH_ORG =     '//div[@class="result-label js-data-isp"]' 
  XPATH_IP =      '//div[@class="result-data js-data-ip"]' 
  XPATH_SPONSOR = '//a[@class="js-data-sponsor"]' 
  XPATH_CITY =    '//div[@class="result-data js-sponsor-name"]' 

  # OLDER PATHS
  #XPATH_GO='//*[@id="container"]/div[2]/div/div/div/div[3]/div[1]/div[1]/a/span[4]'
  #XPATH_PING     = '/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div[1]/div/div[2]/span'
  #XPATH_DOWNLOAD = '/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/span'
  #XPATH_UPLOAD   = '/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[3]/div/div[1]/div[2]/div[3]/div/div[2]/span'
  #XPATH_ORG='//*[@id="container"]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[4]/div/div[2]/div/div[1]/div[2]'
  #XPATH_IP='//*[@id="container"]/div[2]/div/div/div/div[3]/div[1]/div[3]/div/div[4]/div/div[2]/div/div[1]/div[3]'

  driver.get("https://www.speedtest.net/")

  # Click Banner
  elem = driver.find_elements("xpath", XPATH_BANNER)
  print("Element ", elem)
  if len(elem)>0:
      elem[0].click()
  time.sleep(SHORT_TIME)

  # Click Go
  elem = driver.find_elements("xpath", XPATH_GO)
  elem[0].click()
  time.sleep(SHORT_TIME)

  # Wait Results
  def num_there(s):
      return any(i.isdigit() for i in s)
  element = WebDriverWait(driver, LONG_TIME).until(lambda driver : num_there(driver.find_elements("xpath", XPATH_UPLOAD)[0].text))
  time.sleep(SHORT_TIME)

  # Get Results
  ping     = driver.find_elements("xpath", XPATH_PING)[0].text
  download = driver.find_elements("xpath", XPATH_DOWNLOAD)[0].text
  upload   = driver.find_elements("xpath", XPATH_UPLOAD)[0].text
  org      = driver.find_elements("xpath", XPATH_ORG)[0].text
  sip      = driver.find_elements("xpath", XPATH_IP)[0].text
  sponsor  = driver.find_elements("xpath", XPATH_SPONSOR)[0].text
  city     = driver.find_elements("xpath", XPATH_CITY)[0].text

  # Close
  driver.close()

  return {"ping_ms": ping,
          "download_mbps": download,
          "upload_mbps": upload,
          "organization": org,
          "server_ip": sip,
          "sponsor": sponsor,
          "city": city}
    

TEST_NB = 50
BASE_DIR='test_' + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
SLEEP=30

if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
    
for i in range(TEST_NB):
  print("Iteration:", i+1)
  
  directory=BASE_DIR + '/{}_{}'.format("safari_mobile",i)
  
  if not os.path.exists(directory):
      os.makedirs(directory)

  try:
      result = run_speedtest()
      result['browser'] = "safari_mobile"
      result['iteration'] = i
      result['time'] = time.time()
      result['platform'] = "ios"
      print("Iteration result: {}".format(result))
      json.dump(result, open("{}/result.json".format(directory),"w"))
  except Exception as e:
      print ("Error:", e)
      
  time.sleep(SLEEP)