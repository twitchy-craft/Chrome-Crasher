import webbrowser
import time
nerd = 'https://youtu.be/dQw4w9WgXcQ'
bozo = 'https://p.ksh3.tk/'
print('Opening Chrome')
time.sleep(3)
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'time.sleep(3)
print('Done')
print('Opening Crasher thing')
webbrowser.get(chrome_path).open(nerd) 
time.sleep(5)
webbrowser.get(chrome_path).open(bozo) 
time.sleep(3)
print('Done')
