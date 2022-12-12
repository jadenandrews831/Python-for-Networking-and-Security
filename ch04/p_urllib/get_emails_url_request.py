import urllib.request
import re

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
url = input('Enter url: http://')

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]

urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://'+url)
html_content = response.read()
pattern = re.compile("[-a-zA-Z0-9._]+[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
mails = re.findall(pattern, str(html_content))
print(mails)


print(f"\n\n\n{'-'*20}\nStatus: {response.status} {response.reason}")
print("Headers:")
for header, value in response.getheaders():
  print(header+': '+value)
print(f"Data: {html_content.decode()}")

#http://www.packtpub.com/about/terms-and-conditions