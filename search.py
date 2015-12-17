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

company = raw_input(": ")
prefix = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/jsonp?input='
suffix = '&callback=myFunction'

url = prefix + company + suffix
response = requests.get(url)
print response.content


#the regex statement owrking
#result = re.search('{(.*)}', s)
