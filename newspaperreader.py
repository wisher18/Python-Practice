import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for Today!... Let's begin.")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=85055d78644e4a2ba2f096d9f1e06dfb"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict['articles'])
    arts= news_dict["articles"]
    print("Top 3 News are:")
    speak("Top 3 News are:")
    i = 0
    for article in arts:
        i += 1
        print(article["title"])
        speak(article['title'])
        print(f"For more info you can visit: {article['url']}")
        if i == 3:
            break
        speak("Moving on to the next News....")

    speak("Thanks for listening")




