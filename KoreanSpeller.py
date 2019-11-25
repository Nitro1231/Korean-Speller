# Nitro
# nitro0@naver.com
# 11/25/2019
# Korean Speller based on 'Korean Splling Checker' by Pusan National University Artificial Intelligence Lab and Narainfotech Co., Ltd.

import requests 

def speller(text):
    URL = "https://speller.cs.pusan.ac.kr/results"
    data = {'text1':text} # Put the text that you want to check
    r = requests.post(url = URL, data = data) # Post the requests to checker

    webResult = r.text.replace("\n", "")
    result = webResult[webResult.find("data = ") + 7:webResult.find("pageIdx")].strip()[0:-1] # Find the data of checker from the javascript data of the checker.
    print("JSON: %s"%result)

speller("아녕")