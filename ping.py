import subprocess

ips = ["209.244.0.3", "139.130.4.5", "4.2.2.5", "208.67.222.222", "50.116.23.211"]


def main():
    for ipaddr in ips:
        proc = subprocess.Popen(
            ['ping', '-n', '3', ipaddr],
            stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            print('{} is UP'.format(ipaddr))
        else:
            print('{} is DOWN <OR> there is a NETWORK ERROR'.format(ipaddr))


main()