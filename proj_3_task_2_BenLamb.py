# put needed imports here
import datetime
import calendar

# read in the dns log file
file_in = open('dns_log_file.txt')

# canonical line:
# 07-Nov-2011 00:14:19.671 queries: info: client 7.204.241.161#49698: query: smtp.usna.bluenet IN A +
# create an empty list to hold the good records
dns_records = []

# we'll check each line of the log file and filter on the records to keep
# create a for loop
# split the record based on whitespace
# determine how you are going to filter each record
# append the record to your good records list if the record passes your filter
for line in file_in.readlines():
    if line.endswith(' A +\n') or line.endswith(' A -\n'):
        dns_records.append(line.rstrip())

# The following code was provided by Kendall Giles in calendar_time_example.py
datetimes = []
for line in dns_records:
    foo = line.split(" ", 2)
    dmy = foo[0].split("-", 2)
    d = dmy[0]
    mo = dmy[1]
    y = dmy[2]
    hms = foo[1].split(":", 2)
    h = hms[0]
    mi = hms[1]
    mysec = hms[2].split(".", 1)
    s = mysec[0]
    ms = mysec[1]
    mydatetime = datetime.datetime(int(y), list(calendar.month_abbr).index(mo), int(d), int(h), int(mi), int(s),
                                   int(ms) * 1000)
    datetimes.append(mydatetime)
#sort datetimes list
datetimes.sort()

# 1.) Earliest record time and date
# see the calendar_time_example.py 
print("1. The earliest record is from {}".format(datetimes[0]))

# 2.) Last record date/time
# see the calendar_time_example.py
print("2. The latest record is from {}".format(datetimes[-1]))

# 3.) Total number of records
# number of elements in your good records list
print("3. There are {} valid DNS records".format(len(dns_records)))

# 4.) Number of unique client  IP addresses (ignore port #)
# create a dictionary to hold your ip addresses
# find the good_record element containing the ip address and port number
# separate the ip address from the port number
# add the ip address to the dictionary as the key and increment its count as the value
ips = {}
domains = {}
for line in dns_records:
    fio = line.split()
    socket = fio[5]
    domain = fio[7]
    full_ip = socket.split('#',1)
    ip = full_ip[0]
    if ips.get(ip):
        ips[ip] = ips[ip] + 1
    else:
        ips[ip] = 1
    if domains.get(domain):
        domains[domain] = domains[domain] + 1
    else:
        domains[domain] = 1
print("4. There are {} distinct IP addresses".format(len(ips)))
        
# 5.) Number of unique query domains (ignore query IP addresses)
# do similar for the query domain
print("5. There are {} distinct domain addresses".format(len(domains)))

        
# 6.) Most common client address  and number of occurrences
# a dictionary's keys() is a list of all the keys in the dictionary
# dict[key] refers to the value associated with key key
# you could create a for loop to look at each value for each key and find the largest value -- the
# key associated with the largest value is the most common client ip address
most_freq = 0;
freq_ip = ""
for k in ips:
    if ips.get(k) > most_freq:
        most_freq = ips.get(k)
        freq_ip = k
print("6. Most frequent client IP is {} which had {} occurrences".format(freq_ip, most_freq))

# 7.) Most common query domain and number of occurrences
# do something similar 
highest_freq = 0;
freq_d = ""
for k in domains:
    if domains.get(k) > highest_freq:
        highest_freq = domains.get(k)
        freq_d = k
print("7. Most frequent client IP is {} which had {} occurrences".format(freq_d, highest_freq))
