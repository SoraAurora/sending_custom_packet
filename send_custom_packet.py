from scapy.all import send, IP, TCP, ICMP, UDP   
# srp and sr1 is for layer 2, send for layer 3
# from send_custom_packet import custompacket <- use this to import the function custompacket()

import re
def custompacket():
  def send_packet(src_addr:str , src_port:int , dest_addr:str, 
                  dest_port:int, pkt_data:str)  -> bool:
    """Create and send a packet based on the provided parameters

    Args:
        src_addr(str) : Source IP address
        src_port(int) : Source Port
        dest_addr(str): Destination IP address
        dest_port(int): Destination Port

        pkt_data(str) : Data in the packet
    Returns:
        bool: True if send successfull, False otherwise
    """    

    
    pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
    try:
      send(pkt ,verbose = False)   # Hide "Send 1 packets" message on console
      return True
    except:
      return False
          
  def print_custom_menu():
    """Obtain inputs to create custom packet

    Returns: Nil
    """    
    print("************************")
    print("* Custom Packet        *")
    print("************************\n")



    src_addr = input("Enter Source address of Packet: ")
    exp = re.compile(r'^(www\.)(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)+(com)$')
    while not exp.match(src_addr):
      src_addr = input("Invalid input \nRe-Enter Source address of Packet: ")
    while True:
      try:
        src_port = int(input("Enter Source Port of Packet: "))
        while (not src_port >= 0) or (not src_port <= 65535):
          src_port = int(input("Invalid input \nRe-Enter Source Port of Packet: "))
        break
      except:
        print("Invalid Port Number (0-65535)")

    dest_addr= input("Enter Destination address of Packet: ")
    exp = re.compile(r'^(www\.)(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)+(com)$')
    while not exp.match(dest_addr):
      dest_addr = input("Invalid input \nRe-Enter Destination address of Packet: ")

    while True:
      try:
        dest_port= int(input("Enter Destination Port of Packet: "))
        while (not dest_port >= 0) or (not dest_port <= 65535):
          dest_port = int(input("Invalid input \nRe-Enter Destination Port of Packet: "))
        break
      except:
        print("Invalid Port Number (0-65535)")
      
    pkt_data = input("Packet RAW Data (optional, SORAHEHE left blank): ")
    if pkt_data == "":
      pkt_data = "SORAHEHE"
      
    pkt_count = int(input("No of Packet to send (1-65535): " ))
    start_now = input("Enter Y to Start, Any other return to main menu: ")


    if not start_now == "Y": 
      return
    count = 0
    for i in range(pkt_count):
      if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_data):
        count  = count + 1

    print(count , " packet(s) sent" )
    exit()

  print_custom_menu()
