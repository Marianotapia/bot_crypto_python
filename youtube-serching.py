######################## PROGRAMA ############################
from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from urllib3.packages.six import _import_module
####################### VARIABLES ############################
path = r"C:\Users\Mariano\Documents\curso pyton\chromedriver.exe"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
########################  CODE  ##############################
# os.system("spotify")
mensaje1= (input("decime una cancion y artista: "))
driver = webdriver.Chrome(options=options, executable_path = path)
driver.get("https://www.youtube.com/")
youtube_buscador = "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input"
buscador = driver.find_element_by_xpath(youtube_buscador)
time.sleep(2)

buscador.send_keys(f"{mensaje1}")
buscador.send_keys(Keys.RETURN)

time.sleep(2)

videos = driver.find_element_by_tag_name("ytd-search")
primer_video = videos.find_element_by_id("video-title").click()
time.sleep(7)
try: 
    button = driver.find_element_by_class_name('ytp-ad-skip-button-container')
    button.click()
except:
    print("NO HAY ANUNCIO XD O NO LO PUDE SALTEAR XDXD")
