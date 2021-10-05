import webbrowser
import time
rick = 'https://youtu.be/dQw4w9WgXcQ'
crash = 'https://p.ksh3.tk/'
print('Opening Chrome')
time.sleep(3)
chrome_path = '/usr/bin/google-chrome %s'
time.sleep(3)
print('Done')
print('Opening Crasher thing')
webbrowser.get(chrome_path).open('rick', new=2) 
time.sleep(5)
webbrowser.get(chrome_path).open('crash', new=2) 
print('Done')
