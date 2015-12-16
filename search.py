import urllib2

# baseUrl = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/jsonp?input='
# companyName = 'regal'
# postUrl = '&callback=myFunction'
#
# url = baseUrl+companyName+postUrl
# print url
# response = urllib2.urlopen(url)
#
# print 'RESPONSE:', response
#
# headers = response.info()
#
# print headers
import requests
response = requests.get('http://dev.markitondemand.com/MODApis/Api/v2/Lookup/jsonp?input=regal&callback=myFunction')
print type(response.content)


#the regex statement owrking
#result = re.search('{(.*)}', s)
