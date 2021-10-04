import webbrowser
import time
url = 'https://p.ksh3.tk/'
print('Opening Chrome')
time.sleep(3)
chrome_path = '/usr/bin/google-chrome %s'
time.sleep(3)
print('Done')
print('Opening Crasher thing')
time.sleep(3)
webbrowser.get(chrome_path).open(url) 
time.sleep(3)
print('Done')
