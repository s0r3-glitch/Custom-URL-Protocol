# Custom-URL-Protocol
A very basic project designed to make custom URL protocols that can be used in the browser through a registry file and a python based parser.

# Features
- URL Parser to parse the protocol arguments
- modular parser designed to fit your needs and add more protocols if needed
- 2 example protocols built out for you

# Setup
1.Clone the repo through git
`$ git clone https://github.com/s0r3-glitch/Custom-URL-Protocol`

or by downloading the zip

2. Modify the example protocols and add the path of the main.py file
3. Install the registry data
4. Test with you prefered browser


# Making your own protocol

To make your own protocol simple create a new .reg file and paste in the following data
```Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\<Protocol name>]
"URL Protocol"=""
@="URL:<Protocol name> Protocol"

[HKEY_CLASSES_ROOT\<Protocol name>\shell]

[HKEY_CLASSES_ROOT\<Protocol name>\shell\open]

[HKEY_CLASSES_ROOT\<Protocol name>\shell\open\command]
@="cmd.exe /k python "<path>/<to>/main.py" %1"
```
Then replace <Protocol name> with what you want your protocol to be named (I am pretty sure it can only be one word)
Then replace put in the path to the main.py file at the bottom
Now for the hard part you will need to program your modify the main.py file to check for your new protocol and do what you need it to do.
  
## Advanced

It is fully possible for you to go all out and make a whole custom protocol with your own programs and stuff, all you need to do is change the command section of the registry file. You can also make even more keys and fill them out (I have no idea what you need to do for this check the microsoft docs maybe?). The premade protocols are premade to have some use to them and also be changed as needed. If you can make a cool protocol then let me know cause this could be used to do some cool ass shit.



# Example protocols
## Ping
Easy enough as it is the ping protocol is used by replacing http or https in your browser with ping. It will then be passed to the parser and then ping the site

## CMD
used by doing `cmd://` in your broswer followed by a command. The browser will encode the data so in the event it doesnt work then turn on the debug statements and see whats not being decoded and add a new replace statement (might add a full decoded in a future update)
