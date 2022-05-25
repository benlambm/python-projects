import hashlib

fp = open("10K_PLAINTEXT_PASSWORDS.txt", "r") # open for reading

# Read existing file with plaintext passwords
lines = [line.rstrip() for line in fp.readlines()]

fp.close()

# OPEN FILE TO STORE HASHED PASSWORDS HERE
outfile = open("RAINBOW_TABLE.txt", "w")

# loop through each entry in lines
for line in lines:

    # Call the md5 function in hashlib and pass it the password string in bytes. See http://pythoncentral.io/hashing-strings-with-python/
    md5_hashed = hashlib.md5(line.encode())
    
    # Write the hexdigest of the md5_hashed object to the outfile.
    outfile.write(md5_hashed.hexdigest() + "\n")
    
outfile.close()

