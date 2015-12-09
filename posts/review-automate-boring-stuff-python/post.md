I am new to Python, and I wanted to read an easy book, that would give me a hight level overview of the language and what I can do with it.

[Automate the Boring Stuff with Python by Al Sweigart](http://amzn.to/1Nj4FTL) was exactly what I was looking for.

 The book starts out a little slow, since Part I covered the Python Programming Basics, with the emphasis on the *Basics*. I quickly read through it though, because I wanted to familiarize myself with Python syntax, and I am glad that I did. I've picked up some nice tips (copy and paste into clipboard, joining strings etc.) in Part I, that I would have missed otherwise.

 Part II goes into practical application of the core concepts and it is summarized in the next section. Overall, the book was clearly written by somebody who spent many years working with Python. It read like a collection of useful tips, with most examples being less than 20 lines of code.

## Examples of Automation
The author takes us through the following areas that can be automated with Python. I am also highlighting some of the examples that stood out for me.

1. **Pattern Matching with Regular Expressions**
  - Finding and replacing phone numbers, emails and urls in a range of text files
1. **Reading and Writing Files**
  - Opening, reading from, and saving data to files
1. **Organizing Files**
  - Copying, renaming and deleting files
  - Listing files in folder and all folders inside that folder
  - Compressing and uncompressing files (i.e. creating ZIP files)
1. **Debugging**
1. **Web Scraping**
  - Scrape and parse HTML to extract all images from various web pages
  - Use a Selenium module to automate opening browsers and navigating and interacting with web pages (i.e. sign in, fill out a form)
1. **Working with Excel Spreadsheets**
  - Opening, reading data from and writing data to Excel files
1. **Working with PDF and Word Documents**
  - Extracting text from PDFs
  - Combining multiple PDF files into one
  - Creating and styling a word document
1. **Working** with CSV Files and JSON Data
  - Simple example of reading, parsing and saving the data
1. **Keeping Time, Scheduling Tasks, and Launching Programs**
  - Time tracking Modules
  - Example of a Multithreaded program to fetch data from various pages on a website
1. **Sending Email and Text Messages**
  - Connecting to email server to send and receive Messages
  - Using Twilio Module/API to send text messages to yourself to notify when a long running process is done
1. **Manipulating Images**
  - Adding a logo to each image in a folder
1. **Controlling the Keyboard and Mouse with GUI Automation**
  - Writing code to click around your desktop and send keyboard key presses, allowing to automate virtually any software that your computer can run.

## Covered Modules
Bellow is the list of modules that author discussed in his book. Knowing what module to use is already half the battle :) You might want to save this list, for the next time you'll find yourself asking "What module do I use to do *X* in Python?"

- [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Parse HTML
- [copy](https://docs.python.org/2/library/copy.html) - Copy and deep copy of objects
- [csv](https://python.readthedocs.org/en/v2.7.2/library/csv.html) - Work with CSV files
- [datetime](https://docs.python.org/2/library/datetime.html) - Basic date and time types
- [python-docx](https://python-docx.readthedocs.org/en/latest/) - Work with Microsoft Docx files
- [imapclient](https://imapclient.readthedocs.org/en/stable/) - IMAP client library
- [json](https://docs.python.org/2/library/json.html) - Work with JSON files/data
- [logging](https://docs.python.org/2/library/logging.html) - Control Logging output based on config (i.e. debug vs production mode)
- [openpyxl](https://pypi.python.org/pypi/openpyxl/2.3.2) - Work with Excel files
- [os](https://docs.python.org/2/library/os.html) - Operating System interface, change directory etc.
- [pprint](https://docs.python.org/2/library/pprint.html) - Pretty Print your data, instead of regular print.
- [pyautogui](https://pyautogui.readthedocs.org/en/latest/) - Cross platform GUI automation, control your mouse and keyboard to automate any program
- [PyPDF2](https://pythonhosted.org/PyPDF2/) - Work with PDF files
- [pyperclip](https://github.com/asweigart/pyperclip) - Copy/Paste to/from your clipboard
- [pyzmail](http://www.magiksys.net/pyzmail/) - Email library for reading, composing, and sending emails
- [re](https://docs.python.org/2/library/re.html) - Regular Expressions
- [requests](http://docs.python-requests.org/en/latest/) - Make HTTP requests
- [pillow](https://python-pillow.github.io/) - Work with images
- [selenium](http://selenium-python.readthedocs.org/) - Browser automation using Selenium - open web pages, sign in, fill out forms etc.
- [send2trash](https://pypi.python.org/pypi/Send2Trash) - Delete files
- [shelve](https://docs.python.org/2/library/shelve.html) - Persist your in memory objects into a file, to load at a later time
- [shutil](https://docs.python.org/2/library/shutil.html) - Shell utilities: copy, move etc.
- [smtplib](https://docs.python.org/2/library/smtplib.html) - SMTP client
- [subprocess](https://docs.python.org/2/library/subprocess.html) - Spawn new processes
- [threading](https://docs.python.org/2/library/threading.html) - Start new threads
- [time](https://docs.python.org/2/library/time.html) - Time related functions epoch etc.
- [traceback](https://docs.python.org/2/library/traceback.html) - Print stack traces
- [twilio](https://github.com/twilio/twilio-python) - Twilio integration for phone calls and SMS
- [webbrowser](https://docs.python.org/2/library/webbrowser.html) - Open web browser and tabs
- [zipfile](https://docs.python.org/2/library/zipfile.html) - Work with Zip Archives

## Summary
I though that [Automate the Boring Stuff with Python by Al Sweigart](http://amzn.to/1Nj4FTL) was a great read. Not only did the book provide an easy introduction to the Python programming language, but also opened my eyes (as mostly a web developer) to different kinds of tasks that I can easily automated with Python.
