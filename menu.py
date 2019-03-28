print ('\nWelcome to the VPN Builder by Simon Riddle')
print ('\nPlease choose the relevant number below, for the type of device you would like to build:-')
print ('\n\n   1. Cisco ASA')
print ('   2. Cisco IOS')
print ('   3. Cisco IOS-XE')
print ('   4. Cisco IOS-XR')
menu = input('\nMake your selection: ')

if menu == '1':
 import sys
 from Scripts import cisco_asa_ikev2_vpn
if menu == '2':
 import sys
 from Scripts import cisco_ios_ikev2_vpn
if menu == '3':
 import sys
 from Scripts import cisco_iosxe_ikev2_vpn
if menu == '4':
 import sys
 from Scripts import cisco_iosxr_ikev2_vpn
 