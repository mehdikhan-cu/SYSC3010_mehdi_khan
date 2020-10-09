# Done by: Mehdi Khan
import http.client
import urllib.parse

key = "7481QW0APO2BO2BU"

def task():
    # details
    groupName = "L1-F-2"
    memberID = "c"
    cmail = "mehdikhan@cmail.carleton.ca"

    params = urllib.parse.urlencode({'field1': groupName, 'field2': memberID, 'field3': cmail, 'key':key })
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    # upload
    try:
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()
    except:
        print "connection failed"
    break

task()
