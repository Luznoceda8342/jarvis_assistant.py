import os
import webbrowser
from datetime import datetime

print ('JARVIS SYSTEM ONLINE...')

while True:
    command = input ("\nHow can I help you, sir? (type 'exit' to quit') \n ").lower().strip()
    if command == 'exit':
        print('Shutting down protocols. Goodbye, sir.')
        break

    match command:
      case 'open google':
        print('Opening browser...')
        webbrowser.open('https://www.google.com')

      case 'open youtube':
        print('Opening browser...')
        webbrowser.open('https://www.youtube.com')

      case     'open facebook':
        print('Opening browser...')
        webbrowser.open('https://www.facebook.com')

      case    'open instagram':
        print('Opening browser...')
        webbrowser.open('https://www.instagram.com')

      case    'open linkedin':
        print('Opening browser...')
        webbrowser.open('https://www.linkedin.com')

      case 'open spotify':
        print('Opening browser...')
        webbrowser.open('https://open.spotify.com')

      case 'time':
        now = datetime.now().strftime('%H:%M:%S')
        print (f'It exactly {now}, sir.')

      case 'search':
        query = input ('What should I search for, sir? ').lower().strip()
        webbrowser.open(f'https://www.google.com/search?q={query}')

      case _:
          print('I sorry, sir. That command is not in my database.')