#!/usr/bin/env python3
import requests
import sys
import time

class Security_Headers():
	def __init__(self):
		self.headers = {
		    'Accept-Encoding': 'gzip, deflate, sdch',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		    'Referer': 'http://www.wikipedia.org/',
		    'Connection': 'keep-alive',
			}
	
	def main(self):
		try:
			target = input('\nEnter Your Target Domain with http(s) : ')
			summary = input('\nDo You Want The Summary Of The Missing Headers y/n : ')
			print('\n   [+] Checking Missing Headers For \"' + target + '\" : \n')
			response = requests.get(target, headers=self.headers).headers
			
			if 'Strict-Transport-Security' not in response:
				print('\n >>  Strict-Transport-Security ...\n')
				if summary == 'y':
					print('''\n\nSummary: \nHTTP Strict Transport Security is an excellent feature to support on your \nsite and strengthens your implementation of TLS by getting the \nUser Agent to enforce the use of HTTPS. \nRecommended value "Strict-Transport-Security: max-age=31536000; includeSubDomains". ''')
					print('--------------------------------------------------------------------------------------')
				else:
					pass
				time.sleep(1)

			if 'Content-Security-Policy' not in response:
				print(' >>  Content-Security-Policy ...\n')
				if summary == 'y':
					print('''\n\nSummary: \nContent Security Policy is an effective measure to protect your site from XSS attacks. \nBy whitelisting sources of approved content, you can \nprevent the browser from loading malicious assets. ''')
					print('--------------------------------------------------------------------------------------')
				else:
					pass
				time.sleep(1)

			if 'X-Frame-Options' not in response:
				print(' >>  X-Frame-Options ...\n')
				if summary == 'y':
					print('''\n\nSummary:\nX-Frame-Options tells the browser whether you want to allow your site \nto be framed or not. By preventing a browser from framing your \nsite you can defend against attacks like clickjacking. \nRecommended value "X-Frame-Options: SAMEORIGIN".''')
					print('--------------------------------------------------------------------------------------')				
				else:
					pass
				time.sleep(1)

			if 'X-Content-Type-Options' not in response:
				print(' >>  X-Content-Type-Options ...\n')
				if summary == 'y':
					print('''\n\nSummary: \nX-Content-Type-Options stops a browser from trying to MIME-sniff the \ncontent type and forces it to stick with the declared content-type. \nThe only valid value for this header is "X-Content-Type-Options: nosniff". ''')
					print('--------------------------------------------------------------------------------------')
				else:
					pass
				time.sleep(1)

			if 'Referrer-Policy' not in response:
				print(' >>  Referrer-Policy ...\n')
				if summary == 'y':
					print('''\n\nSummary: \nReferrer Policy is a new header that allows a site to control how much \ninformation the browser includes with navigations away from a \ndocument and should be set by all sites. ''')
					print('--------------------------------------------------------------------------------------')
				else:
					pass
				time.sleep(1)

			if 'Feature-Policy' not in response:
				print(' >>  Feature-Policy ...\n')
				if summary == 'y':
					print('''\n\nSummary: \nFeature Policy is a new header that allows a site to control which features and \nAPIs can be used in the browser. ''')
					print('--------------------------------------------------------------------------------------')
				else:
					pass

		except KeyboardInterrupt:
			print('\n[~] Exitting ...\n')
			sys.exit()

if __name__ == '__main__':
	sec_header = Security_Headers()
	sec_header.main()