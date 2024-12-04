from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import matplotlib.pyplot as plt
import numpy as np

# Start the session
driver = webdriver.Chrome()

# Take action on browser
url = "https://tp-crawlers.istic.univ-rennes1.fr/pokemons/scroll"
driver.get(url)
time.sleep(1) # A wait of 1 seconds

# Question 1:
# Extract the type of all Pokémons by scrolling down the page
# until nothing is loaded.

try:
    pokemons_types = [] # Pour stocker les types par pokemon
    types_control = [] # Pour énumerer les differents types
    plot_y_values = [] # Pour stocker les valeurs
    type_counter = 0 # Pour conter les types

    prev_height = driver.execute_script("return document.body.scrollHeight")
    max_scrolls = 100
    scroll_count = 0

    # scroll the page until nothing is loaded
    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1
    
    pokemons = driver.find_elements(By.CLASS_NAME, "pokemon-info")

    for id in range(1, len(pokemons), 4):
        pokemons_types.append(pokemons[id].text.replace(',', '').split(' ')[1:])

    print('Pokemons number :', len(pokemons_types))

    for types in pokemons_types:
        for t in types:
            if t in types_control:
                continue
            else:
                types_control.append(t)
                for type in pokemons_types:
                    for t in type:
                        if t == types_control[-1]:
                            type_counter += 1
                print(types_control[-1], ":", type_counter)
                plot_y_values.append(type_counter)
                type_counter = 0

    print('Liste des types :', types_control)

    # Graphique matplotlib: histogramme
    x = np.arange(len(types_control))
    plt.bar(x, plot_y_values, align='center')
    plt.xticks(x, types_control, rotation=90)
    plt.xlabel('Types')
    plt.ylabel('Nombre de Pokémons')
    plt.title('Histogramme des Pokémons par types')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(type(e).__name__, ":\n", e)
    

# Close the session
driver.quit()