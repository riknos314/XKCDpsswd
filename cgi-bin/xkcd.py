#!/usr/bin/env python
import os
import random

headers = ["Content-type: text/html"]
qs = os.environ['QUERY_STRING']


def getWords():
	dictionary = [i.strip() for i in open('/usr/share/dict/american-english').readlines()]
	wordone = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordtwo = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordthree = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordfour = dictionary[ random.randrange(0,len(dictionary)-1,1)]
	wordlist = [wordone, wordtwo, wordthree, wordfour]
	return wordlist

def sendHeaders():
    for h in headers:
        print h
    print "\n"

def sendForm():
    print '''
    <html>
				<head>
					<title></title>
				</head>
					<h1>XKCD rules pasword generator</h1>
					<body>
						<form method="get" action="cgi-bin/xkcd.py">
							<label>select password peramaters</label><br>
							<input type="text" name="minl" value="enter a minimum length"><br>
							<input type="text" name="maxl" value="enter a maximum length"><br>
							<input type="checkbox" name="three">3 == e<br>
							<input type="checkbox" name="zero">0 == o<br>
							<input type="checkbox" name="one">1 == l<br>
							<input type="checkbox" name="five">5 == s<br>
							<input type="checkbox" name="four">4 == a<br>
							<input type="checkbox" name="cFirst">Capitalize first word<br>
							<input type="checkbox" name="cSecond">Capitalize second word<br>
							<input type="checkbox" name="cThird">Capitalize third word<br>
							<input type="checkbox" name="cFourth">Capitalize fourth word<br>
							<input type="checkbox" name="cFifth">Capitalize fifth word<br>

							<input type="submit" value="generate" ></input>

						</form>
					</body>
				</html>
    '''

def sendPage(name):
    print '''
    <html>
      <body>
        <h1>Hello {0}</h1>
      </body>
    </html>
    '''.format(name)

if not qs:
    sendHeaders()
    sendForm()
else:
    if 'firstname' in qs:
        name = qs.split('=')[1]
    else:
        name = 'No Name Provided'
    sendHeaders()
    sendPage(name)
