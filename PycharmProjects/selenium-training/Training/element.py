import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver=webdriver.Chrome(opts)

'''driver.get('https://www.iforex.in/tools/live-rates')

driver.find_element('xpath','//div[@id="ai-chat-close"])').click()
time.sleep(5)


gold_sellprice=driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[2]')
gold_buyprice=driver.find_element('xpath','(//div[text()="Gold"]/../..//span)[3]')

print(gold_sellprice.text)
print(gold_buyprice.text)
'''
driver.get('https://www.makemytrip.com/')
time.sleep(5)

driver.find_element('xpath','//span[@class="commonModal__close"]').click()
time.sleep(5)

driver.find_element('xpath','//span[text()="Departure"]').click()
time.sleep(5)

def select_date(month,date):
    while True:
      try:
         driver.find_element('xpath','//div[text()="{month}"]/../..//p[text()="{date}"]').click()
         break
      except:
         driver.find_element('xpath','//span[@class="DayPicker-NavButton DayPicker-NavButton--next"]').click()
         time.sleep(5)
select_date('September 2026','15')










