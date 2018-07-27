#This script will create subnets for IP range
import ipaddress
ip=input("Please enter IP address e.g. x.x.x.x/24:")
sub_net=int(input("Please enter subnet e.g. 26 or 28:"))
subnet_list=list(ipaddress.ip_network(ip).subnets(new_prefix=sub_net))
print(subnet_list)
