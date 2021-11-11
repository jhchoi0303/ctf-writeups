import crypto 
import sys 
sys.modules['Crypto'] = crypto

from base64 import b64decode, b64encode
from Crypto.Util.number import bytes_to_long, long_to_bytes

print(b64encode(long_to_bytes(69525558883514113)))



s1=bytes_to_long(b64decode("n1Y9axTMj4afpM7RCcjhS19QfLBBypnuzSdm9rPgg253rL+HuvzFECmX6tbm6NlvsEUvZipzOcbXm+GfbNbzgTGJqWylMVWLdPrvS4A1hppFx/f5pGpZdB3j1OcTAEHBUjkdTdLaqk/htgcp6YrJL3Yl7crtw/ScpWHiSP3+dZw="))


s2=bytes_to_long(b64decode(" C7E6Ii2YEgnTG2aFJxwXqB0DLap9/hg7nAQFvuyeHqlQCjJnXBDtTc0KWIoZU0XB/8ZC9emEuoyWjzbQclkY3gvvegXF9Qphtkfz7tJ0mqxKpCq1PpXGLeV0k3YuC2my6T4p/OYsHW7VXAE09L3918dTt8pujK5IzhL8laiX1PY="))


print(s1)

print(s2)


n= 0xabfdbc245a37e37419674e4c180f8d1171a0d8313675b33be92b72f7c4eb41cd7e3aa37748201cc3103b3daf86f036a4a8cc68228084486deccc6e4455853082c329a7980d20aec6cdb3043e059337453b0e93c09e5665bffa814c5b75c56301f5db69c3111a0d4750618522eab8f9e825bcbda0572ead0bfb841d13908ea113


print(b64encode(long_to_bytes((s1*s2)%n)))
