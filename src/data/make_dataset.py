
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

start = time.time()
driver = webdriver.Chrome()

driver.get('https://www.icao.int/publications/DOC8643/Pages/Search.aspx')
xpath_extender = '//*[@id="atd-table_length"]/label/select' 
xpath_num_pages = '//*[@id="atd-table_paginate"]/ul/li[8]/a'
xpath_next = '//*[@id="atd-table_next"]/a'
xpath_table = '//*[@id="atd-table-body"]'
xpath_row = '//*[@id="atd-table-body"]/tr[{}]'
xpath_cell = '//*[@id="atd-table-body"]/tr[{}]/td[{}]'

wait = WebDriverWait(driver, 60)

wait.until(
    EC.presence_of_element_located(
        (By.XPATH, xpath_cell.format(2, 2))
        )
    )

extender = driver.find_element(By.XPATH, xpath_extender)
extender.send_keys(100)
num_pages = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, xpath_num_pages)
        )
    )

pages = int(num_pages.text)

print(f'No of Pages: {num_pages.text}')

data = []

for i in range(pages):
    
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, xpath_cell.format(2, 2))
            )
        )
    
    table = driver.find_element(By.XPATH, xpath_table)

    lines = table.text.count('\n') + 1
    
    for j in range(lines):
    
        line = table.find_element(By.XPATH, xpath_row.format(j+1))
    
        values = [
                line.find_element(
                    By.XPATH, xpath_cell.format(j+1, k+1)
                    ).text for k in range(7)]
        
        if (j+1)%10 == 0: print(f'Lines Completed: {(j+1) + 100*(i):3d}')
        
        data.append(values)
    
    print('---------------------')    
    print(f'Pages Done: {i+1:3d}')
    
    if i == (pages - 1):
        break
        
    next_ = driver.find_element(By.XPATH, xpath_next)
    next_.click()
    
# %%
    
df = pd.DataFrame(data = data,
                  columns = ['NOME_FABRICANTE', 'MODELO',
                             'TIPO_ICAO', 'ATERRISAGEM',
                             'TIPO_MOTORES', 'NUM_MOTORES',
                             'WTC']
                  )

total_time = time.time() - start
mins = int(total_time//60)
secs = total_time%60
print(f'Running Time: {mins:2d} minutes and {secs:5.2f} seconds.')
    
print(f'\nTotal Instances: {df.shape[0]}')
print(f'Total Fields: {df.shape[1]}')
    
df.to_csv('../../data/raw/icao_categories.csv', index = False)
