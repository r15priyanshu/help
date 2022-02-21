import socket
import re
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

#the below function will check if the passed string is ip or not
def check(ip):
    if(re.search(regex, ip)):
        return True   
    else:
        return False

#this will return ip address of a hostname
def host_to_ip(hostname):
    result=''
    status=''
    try:
        result=socket.gethostbyname(hostname)
        status='PASS'
    except BaseException as msg:
        result=msg
        status='FAIL'
    return result,status 

#this will return hostname of the ip passed
def ip_to_host(ip):
    #this will return hostname of an ip
    result=''
    status=''
    try:
        result=socket.gethostbyaddr(ip)[0]
        status='PASS'
    except BaseException as msg:
        result=msg
        status='FAIL'
    return result,status 



########################################################################################################


try:
    print("********************************************DNS LOOKUP STARTING********************************************\n\n")
    with open("hostname.txt","r") as f:
        r=open("dns_result_"+f.name,'w')
        r.write("HOSTNAME=DNS_OUTPUT=STATUS\n")
        hostnames=f.readlines()
        #print(hostnames)
        for host in hostnames:
            host=host.strip()
            if check(host):
                result,status=ip_to_host(host)
                r.write("{}={}={}\n".format(host,result,status))
                print("{}={}={}\n".format(host,result,status))
            else:
                result,status=host_to_ip(host)
                r.write("{}={}={}\n".format(host,result,status))
                print("{}={}={}\n".format(host,result,status))
                
        r.close()
except BaseException as msg:
    print("ERROR occurred :",msg)
    print("********************************************DNS LOOKUP ENDED********************************************\n\n")
   
