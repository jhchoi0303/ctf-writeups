import hashlib
username_trial = "PRITCHARD"
bUsername_trial = b"PRITCHARD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
len(key_full_template_trial)

key=[0] * 32
i = 0
for c in key_part_static1_trial:
    key[i] = c
    i += 1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[4]
i += 1 
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[5]
i += 1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[3]
i += 1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[6]
i+=1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[2]
i+=1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[7]
i+=1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[1]
i+=1
key[i] = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()[8]

for i in range(len(key)):
    print(key[i],end="")