import urllib
import re
url = 'http://static.nid.naver.com/enclogin/keys_js.nhn'
data = urllib.urlopen(url)
data = data.read()
sessionkey = re.findall("sessionkey = '?(.*?)';",data)[0]
keyname = re.findall("keyname = '?(.*?)';",data)[0]
evalue = re.findall("evalue = '?(.*?)';",data)[0]
nvalue = re.findall("nvalue = '?(.*?)';",data)[0]
