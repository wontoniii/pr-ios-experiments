
from sqlalchemy import true
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import datetime
import json
import time
import os

def run_webpage(page):
  capabilities =     {
        "xcodeOrgId": "4X87KUK52T",
        "xcodeSigningId": "iPhone Developer",
        'platformName': 'iOS',
        'platformVersion': '15.6.1',
        'automationName': 'XCUITest',
        'browserName': 'Safari',
        'deviceName': 'iPad',
        'udid': "00008103-001579403C88801E",
        'showXcodeLog': "true"
      }
        # 'updatedWDABundleId': 'com.francesco.prappium',

  driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
  print("get {}".format(page))

  driver.get("https://"+page)
  
  ''' Use Navigation Timing  API to calculate the timings that matter the most '''   
 
  # navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
  # responseStart = driver.execute_script("return window.performance.timing.responseStart")
  # domComplete = driver.execute_script("return window.performance.timing.domComplete")
  all = driver.execute_script("return window.performance.timing")
  
  driver.close()

  return all
    

TEST_NB = 5
BASE_DIR='test_' + datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
FILE_PATH='fr.txt'
SLEEP=10

if not os.path.exists(BASE_DIR):
  os.makedirs(BASE_DIR)
    
f = open(FILE_PATH, 'r')
lines = f.readlines()
# Strips the newline character
for line in lines:
  line = line.rstrip("\n")
  for i in range(TEST_NB):
    print("Iteration:", i+1)
    
    directory=BASE_DIR + '/{}_{}'.format("safari_mobile",i)
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        result = run_webpage(line)
        result['page'] = line
        result['browser'] = "safari_mobile"
        result['iteration'] = i
        result['time'] = time.time()
        result['platform'] = "ios"
        print("Iteration result: {}".format(result))
        json.dump(result, open("{}/result.json".format(directory),"w"))
    except Exception as e:
        print ("Error:", e)
        
    time.sleep(SLEEP)