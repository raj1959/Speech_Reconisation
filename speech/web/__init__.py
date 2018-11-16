import webbrowser

chrome_path = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --kiosk %s'

google = input('Google search:')
#webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

f_text = 'https://www.google.pl/search?q=' + google
webbrowser.get(chrome_path).open(f_text)
