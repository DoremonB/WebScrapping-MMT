from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

delay=10

#variables:

no_adults=3
no_children=2
no_infants=1
FromLocation='Mumbai'
ToLocation='Kolkata'
date='10/10/2020'
flight_list=[]

#

options = webdriver.ChromeOptions()
options.add_argument(" --disable-notifications")



driver =webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()


driver.find_element_by_id('fromCity').send_keys(FromLocation)
driver.find_element_by_id('toCity').send_keys(ToLocation)

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/label/span').click()



driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div/ul[1]/li[{no_adults}]').click()

driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div/div/div[1]/ul/li[{no_children+1}]').click()

driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div/div/div[2]/ul/li[{no_infants+1}]').click()

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/button').click()

#submit
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/p/a').click()





#https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-07/02/2020&tripType=O&paxType=A-3_C-2_I-1&intl=false&cabinClass=E
current_url=driver.current_url
l=current_url.split('-')
l2=l[2].split('&')
current_url=f'{l[0]}-{l[1]}-{date}&{l2[1]}&{l2[2]}-{l[3]}-{l[4]}-{l[5]}'
driver.get(current_url)


WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div[2]/p/span')))

for i in range(1,100):
    driver.execute_script("window.scrollTo(0,   document.body.scrollHeight);")

        

try:
    for i in range(1,1000):
        company_name=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[1]/div[2]/p/span').text
        depart_time=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div/div/label/div[1]/div').text
        arrive_time=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div/div/label/div[3]/div/p[1]').text 
        price = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[3]/p/span').text
        duration=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div/div/label/div[2]/p[1]').text
        
        hrs_to_mins=int(duration[0:2])*60
        mins=int(duration[7:9])
        duration_min=str(hrs_to_mins+mins)


        price=price.replace(",", "")
        price=price.replace(" ", "")
        price=price.replace("₹", "")

        
        flight=dict()
        flight["website"]="https://www.makemytrip.com/"
        flight["company_name"]=company_name
        flight["depart_time"]=depart_time
        flight["arrive_time"]=arrive_time
        flight["duration"]=duration
        flight["duration_mins"]=duration_min
        flight["price"]=price
        flight_list.append(flight)

       
            
except Exception as e:
    print("#################  EXCEPTION OCCURED ############")
    print(str(e))

print(flight_list)


















# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException

# delay=10


# options = webdriver.ChromeOptions()
# options.add_argument(" --disable-notifications")


# driver =webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)

# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()


# driver.find_element_by_id('fromCity').send_keys('Mumbai')
# driver.find_element_by_id('toCity').send_keys('Kolkata')

# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/label/span').click()
# time.sleep(1)

# no_adults=3
# driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div/ul[1]/li[{no_adults}]').click()

# no_children=2
# driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div/div/div[1]/ul/li[{no_children+1}]').click()

# no_infants=1
# driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/div/div/div[2]/ul/li[{no_infants+1}]').click()

# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[5]/div[1]/button').click()

# #submit
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/p/a').click()


# time.sleep(5)

# current_url=driver.current_url
# #https://www.makemytrip.com/flight/search?itinerary=DEL-BLR-07/02/2020&tripType=O&paxType=A-3_C-2_I-1&intl=false&cabinClass=E

# l=current_url.split('-')
# # print(l)

# l2=l[2].split('&')
# # print(l2)

# # current_date=l2[0]
# date='10/10/2020'


# current_url=f'{l[0]}-{l[1]}-{date}&{l2[1]}&{l2[2]}-{l[3]}-{l[4]}-{l[5]}'
# driver.get(current_url)



# for i in range(1,100):
#     driver.execute_script("window.scrollTo(0,   document.body.scrollHeight);")

        
# flight=[]
# try:
#     for i in range(1,1000):
#         company_name=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[1]/div[2]/p/span').text
#         try:
#             arrive_time=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div/div/label/div[1]/div').text
#             depart_time=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div/div/label/div[3]/div/p[1]').text
#             price = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[3]/p/span').text
            

#             price=price.replace(",", "")
#             price=price.replace(" ", "")
#             price=price.replace("₹", "")

            
            

#             k=dict()
#             k["company_name"]=company_name
#             k["arrive_time"]=arrive_time
#             k["depart_time"]=depart_time
#             k["price"]=price
#             flight.append(k)

#         except Exception as e:
#             print(str(e))
#             pass
#             # arrive_time1=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/label/div[1]/div').text
#             # arrive_time2=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div/label/div[1]/div').text
            
#             # depart_time1=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/div/label/div[3]/div/p[1]').text
#             # depart_time2=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div/label/div[3]/div/p[1]').text

#             # price=driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[{i}]/div[1]/div[1]/div/div/div/div[3]/span/p[1]/span[2]').text
#             # price=price.replace(",", "")
#             # price=price.replace(" ", "")
#             # price=price.replace("₹", "")

#             # k=dict()
#             # k["company_name"]=company_name
#             # k["arrive_time"]=arrive_time1
#             # k["depart_time"]=depart_time1
#             # k["price"]=price
#             # flight.append(k)

#             # k=dict()
#             # k["company_name"]=company_name
#             # k["arrive_time"]=arrive_time2
#             # k["depart_time"]=depart_time2
#             # k["price"]=price
#             # flight.append(k)
            
# except Exception as e:
#     print("#################  EXCEPTION OCCURED ############")
#     print(str(e))

# print(flight)
