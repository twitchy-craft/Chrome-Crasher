import webbrowser
import time
#uses the dev crash test thingy
url = 'http://a/%%30%30'
#runs chrome
print('Opening Chrome')
time.sleep(3)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
time.sleep(3)
print('Done')
#opens the dev url
print('Opening Crasher thing')
time.sleep(3)
webbrowser.get(chrome_path).open(url) #crashes coom
time.sleep(3)
print('Done')
