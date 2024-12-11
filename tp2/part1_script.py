from selenium import webdriver
import trio
import time

# Question 1:
# compute and print in your console all the Network requests 
# and responses of the url page

url = "https://tp-crawlers.istic.univ-rennes1.fr/pokemons/scroll"

async def request(listener):
    async for event in listener:
        print(f"Request: {event.request.method} {event.request.url}\n")

async def response(listener):
    async for event in listener:
        print(f"Response: {event.response.status} {event.response.url}\n")

async def main():
    driver = webdriver.Chrome()

    async with driver.bidi_connection() as connection:
        session, devtools = connection.session, connection.devtools

        await session.execute(devtools.network.enable())
        request_listener = session.listen(devtools.network.RequestWillBeSent)
        response_listener = session.listen(devtools.network.ResponseReceived)

        async with trio.open_nursery() as nursery:
            nursery.start_soon(request, request_listener)
            nursery.start_soon(response, response_listener)

            driver.get(url)
            
            time.sleep(5)
            # Attendre un peu plus pour capturer les requêtes/réponses supplémentaires
            await trio.sleep(5)

trio.run(main)



