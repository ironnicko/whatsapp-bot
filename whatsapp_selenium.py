import os
os.system('pip install selenium')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = f"{os.getcwd()}\\chromedriver.exe" # remove .exe and install the chrome driver if you're using other operating systems
driver = webdriver.Chrome(PATH)

driver.get('https://web.whatsapp.com/')

print('Please note that you\'ll have to scan QR code')

while True:
    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))

    input('Scan QR code and then press Enter to execute')
    
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.RETURN)

    if input('Press \'0\' to stop and anything else to continue.')== '0':break
