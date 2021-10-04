import webbrowser
import time
nerd = 'https://youtu.be/dQw4w9WgXcQ'
url = 'https://p.ksh3.tk/'
print('Opening Chrome')
time.sleep(3)
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
time.sleep(3)
print('Done')
print('Opening Crasher thing')
webbrowser.get(chrome_path).open(nerd) 
time.sleep(5)
webbrowser.get(chrome_path).open(url) 
time.sleep(3)
print('Done')
