from selenium import webdriver
from selenium.webdriver.common.by import By


# Start the session
driver = webdriver.Chrome()

# Take action on browser
driver.get("https://tp-crawlers.istic.univ-rennes1.fr/pokemons/pages")

# Question 1: 
# Extract the name of your favorite Pokémon 
# using its number and print it to the console.
favorite_pokemon = driver.find_element(By.ID, "025")
his_name = favorite_pokemon.find_element(By.CLASS_NAME, "pokemon-name")
print("My favorite pokemon is : ",his_name.text)

# Question 2:
# Extract the weight of all the Pokémons present on the page, 
# compute the total sum, and print it to the console
total_weight = 0

for pokemon_weight in driver.find_elements(By.CLASS_NAME, "pokemon-weight"):
    total_weight += float(pokemon_weight.text.split(' ')[1].replace(',', '.'))

try:
    print("Next pages")
    while(driver.find_element(By.ID, "next")):
        driver.find_element(By.ID, "next").click()
        for pokemon_weight in driver.find_elements(By.CLASS_NAME, "pokemon-weight"):
            total_weight += float(pokemon_weight.text.split(' ')[1].replace(',', '.'))
except Exception as e:
    if type(e).__name__ == 'NoSuchElementException': pass
    else: print(e)

print("The total weight of all pokemons is : ",total_weight)

# Question 3: Extract the height of all the Pokémons from all the pages
#  by interacting with the "Next" button at the bottom of the page.
# Compute the mean, maximum, minimum of the height for all Pokémons 
# and print it to the console.

# Voir la résolution de la question précédente

# Close the session
driver.quit()
