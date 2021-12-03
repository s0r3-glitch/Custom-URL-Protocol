import sys
import os


def main():

  # Greabs all the arguments passed to the profram
  args = sys.argv
  
  # Debug statements to check what all is being passed and how many arguments are being passed
  #print(str(sys.argv))
  #print(f"Number of Args. {len(sys.argv)}")
  
  # Grabs the 2nd agrgument in the list because the way the registary key is set up the path to this file is passed as the first arguement
  arg1 = sys.argv[1]
  
  '''Due to the nature of how windows passes the arguments from the browser the entire protocol is passed (ie. ping://www.google.com)
  and the fact that the browser encodes the protocol before sending it to whindows we have to get dir of the // part of the protocol and replace the %20 with spaces
  then we split the parsed protocol into a list '''
  arg1 = arg1.replace('/','')
  arg1 = arg1.replace('%20', ' ')
  #print(arg1)
  arg1 = arg1.split(':')
  #print(arg1)
  
  # An example protocol for ping:// which checks the arg1 list for the first result for the protocol and then the passes the 2nd argument to the ping command
  if arg1[0] == 'ping':
    os.system(f'ping {arg1[1]}')

  # An example protocol for cmd:// which checks thte arg1 list for the first result for the protocol and then passes the 2nd argument to cmd to be ran
  elif arg1[0] == 'cmd':
    os.sys(arg1[1])
  

  



main()
