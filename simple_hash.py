# see https://www.r-project.org for eg

import hashlib
from timeit import default_timer as timer


plaintext = input("String to hash: ")
startTime = timer()

md5_hashed = hashlib.md5(plaintext.encode())
mytime = (timer() - startTime)*1000000

print ('It took ', mytime , ' microseconds to hash ' + plaintext + ' into:\n' + md5_hashed.hexdigest())
