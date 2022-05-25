from timeit import default_timer as timer

file1 = open("RECOVERED_PASSWORD_HASHES.txt")

recovered_hashes = file1.readlines()

file1.close()

file2 = open("RAINBOW_TABLE.txt")

# https://docs.python.org/3/library/functions.html#enumerate
indexed_hashes = list(enumerate(file2))

file2.close()

file3 = open("10K_PLAINTEXT_PASSWORDS.txt")

plaintext_passwords = file3.readlines()

file3.close()

# for each candidate hash in recovered_hashes
for candidate in recovered_hashes:
   # timer starts here
   startTime = timer()
   # maybe use a flag variable (True/False)
   match_found = False
   for i,hash in indexed_hashes:
       if candidate.rstrip() == hash.rstrip():
          match_found = True
          print("MATCH: hash # " + hash + " = " + plaintext_passwords[i])
          print("The search took {} microseconds.\n".format(str(timer()-startTime)))
   # this part of the code is to be executed if there is no match after a search through
   # the entire list of indexed_hashes. maybe condition on your flag variable
   if not match_found:
       print("NO MATCH FOUND FOR ", candidate.rstrip())
       print("The search took {} microseconds.\n".format(str(timer()-startTime)))
