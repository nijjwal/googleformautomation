import csv 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeW-4j-MXIgSvVIaLOFNk3Qf4ilC5PU7BwR3KLJg1kIRacTWA/viewform')

        time.sleep(1)

        name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        name.send_keys(line[0])

        age = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        age.send_keys(line[1])

        genderMale = driver.find_element(By.XPATH, '//*[@id="i13"]/div[3]/div')
        genderFemale = driver.find_element(By.XPATH, '//*[@id="i16"]/div[3]/div')
        genderNoAnswer = driver.find_element(By.XPATH, '//*[@id="i19"]/div[3]/div')

        
        if(line[2] == 'Male'):
            print('Male')
            genderMale.click()
        elif(line[2] == 'Female'):
            print('feMale')
            genderFemale.click()
        else:
            print('uk')
            genderNoAnswer.click()

        submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit.click()
        time.sleep(2)


       