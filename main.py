#only for windows
import webbrowser
#uses the dev crash test thingy
url = 'chrome://inducebrowsercrashforrealz'
#runs chrome
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#opens the dev url
webbrowser.get(chrome_path).open(url) #crashes coom
