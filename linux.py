import webbrowser
import time
#crashes chrome
url = 'https://p.ksh3.tk/'
#opens chrome
print('Opening Chrome')
time.sleep(3)
chrome_path = '/usr/bin/google-chrome %s'
time.sleep(3)
print('Done')
#opens the crasher url
print('Opening Crasher thing')
time.sleep(3)
#open it pp moment
webbrowser.get(chrome_path).open(url) 
time.sleep(3)
print('Done')
