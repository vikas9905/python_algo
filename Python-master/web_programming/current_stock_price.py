import requests
from bs4 import BeautifulSoup
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

def speak(audio):
    #time.sleep(10)
    engine.say(audio)
    engine.runAndWait()

def stock_price(symbol: str = "AAPL") -> str:
    url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
    return soup.find("div", class_=class_).find("span").text


if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
        speak(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
