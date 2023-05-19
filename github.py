import requests
import subprocess
import re

url = 'https://insights.parkassist.com/sites/qut/status/v2/zones.json'

r = requests.get(url)

data = r.json()
id_array = [1]
for obj in data['response']:
    id = obj['id']
    if id in id_array:
        name = obj['name']
        basement1 = obj['counts']['available']


data = r.json()
id_array = [2]
for obj in data['response']:
    id = obj['id']
    if id in id_array:
        name = obj['name']
        basement2 = obj['counts']['available']
       

data = r.json()
id_array = [3]
for obj in data['response']:
    id = obj['id']
    if id in id_array:
        name = obj['name']
        underfreeway = obj['counts']['available']

def execute_curl_command(url):
    command = ['curl', url]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing curl command: {e}")
        return None
    
url = 'https://jp.translink.com.au/plan-your-journey/stops/006549'
output = execute_curl_command(url)
if output:
    regex_pattern = r'<span class="single-line countdown">(.*?)</span>'
    matches = re.findall(regex_pattern, output, re.DOTALL)
    if matches:
        time = matches[0]
        print(time)
    else:
        print("No title found.")

    regex_pattern = r'<span class="label label-default bus-route">(.*?)</span>'
    matches = re.findall(regex_pattern, output, re.DOTALL)
    if matches:
        route = matches[0]
        print(route)

BL1 = basement1
BL2 = basement2
UFP = underfreeway
BLP = BL1 + BL2
TPA = BLP + UFP
PAV = TPA
#Total Parking is 391

print(PAV)

if PAV > 196:
    title = "Drive Today"
    Message = "There are currently {} spots avilable at QUT currently, Driving is viable.".format(PAV)
    Bus = ""
elif PAV >= 99 < 196:
      title = "Driving might be a gamble today"
      Message= "There is currently {} spots available at QUT, Driving is might be viable.".format(PAV)
      Bus = "The next bus is the {} which will arrive in {}".format(route,time)
elif PAV >= 20 < 98:
      title = "There are only {} spot available".format(PAV)
      Message= "Suggest Taking the Bus.".format(PAV)
      Bus = "The next bus is the {} which will arrive in {}".format(route,time)
     
elif PAV >= 0 < 20:
    title = "There is only {} spots left".format(PAV)
    Message= "Take the Bus,".format(PAV)
    Bus = "The next bus is the {} which will arrive in {}".format(route,time)
    

print(Message,Bus)

