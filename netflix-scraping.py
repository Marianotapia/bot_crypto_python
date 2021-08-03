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
mensaje1=(input("""decime un titulo de neflix: """))

browser = webdriver.Chrome(options=options, executable_path = path)
browser.get("https://www.google.com/")

input_buscador_xpath="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
input_buscador = browser.find_element_by_xpath(input_buscador_xpath)
input_buscador.send_keys(f"{mensaje1} netflix site:www.netflix.com")
input_buscador.send_keys(Keys.RETURN)
time.sleep(3)

busqueda = browser.find_element_by_id("rso")
primer_div = busqueda.find_element_by_tag_name("div")
primer_div.find_element_by_tag_name("a").click()
lista_sections = browser.find_elements_by_class_name("nmtitle-section")[-4]
if "Episodios" in lista_sections.text:
    serie = browser.find_element_by_class_name("title-info")
    nombre_serie = serie.find_element_by_class_name("title-title")
    sinopsis = serie.find_element_by_class_name("title-info-synopsis")
    def BuscarEpisodios():
        for capitulo in lista_episode:
            titulito = capitulo.find_element_by_class_name("episode-title").text
        
            if titulito.strip() == "":
                continue
            synopsis= capitulo.find_element_by_class_name("epsiode-synopsis").text
            f.write(f""" 
            {titulito}

            {synopsis}
            ------------------------------------------------------------\n""")
    time.sleep(2)
    
    try:
        lista_episode = browser.find_elements_by_class_name("episode")
        container_temporadas = browser.find_element_by_id("undefined-select")
        lista_temporadas = container_temporadas.find_elements_by_tag_name("option")      
        f = open(f"series.txt","a") 
        f.write(f"""
        Titulo:  {nombre_serie.text}

        Sinopsis:   {sinopsis.text}

        ------------------------------------------------------------\n""")
        for temporada_index in range(len(lista_temporadas)):            
            select = Select(container_temporadas)        
            select.select_by_index(temporada_index)            
            f.write(f"""
            {lista_temporadas[temporada_index].text}
            
            ---------------------------------------------------------------------\n""")
            BuscarEpisodios()            
        f.close
        browser.quit()
    except:   
        lista_episode = browser.find_elements_by_class_name("episode")
        f = open("series.txt","a") 
        f.write(f"""
        Titulo:  {nombre_serie.text}

        Sinopsis:   {sinopsis.text}

        ------------------------------------------------------------\n""")        
        BuscarEpisodios()
        f.close
        browser.quit()
else: 
    f = open("peliculas.txt","a") 
    pelicula = browser.find_element_by_class_name("title-info")
    nombre_pelicula = pelicula.find_element_by_class_name("title-title")
    f.write(f"Titulo: {nombre_pelicula.text}\n")    
    sinopsis = pelicula.find_element_by_class_name("title-info-synopsis")
    f.write(f"Sinopsis: {sinopsis.text}\n")
    prot_y_dir = pelicula.find_element_by_class_name("title-info-talent")
    f.write(f"""{prot_y_dir.text}
    ---------------------------------------------------------------\n""")
    browser.quit()
