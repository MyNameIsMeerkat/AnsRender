#-----------------------------------------------------------
# Filename      : AnsRender.py
# Description   : Dirty terminal display of .ans files (ANSI art)
# Created By    : Rich Smith
# Date Created  : 11-Feb-2014 22:03
# 
# License       : GPLv2
#
#
#-----------------------------------------------------------
__author__ = "Rich Smith"
__version__ = "0.1"

import os
import struct
try:
    import colorama
    colorama.init()
except:
    print "[-] Could not import colorama module, depending on your platform/terminal ANSI display may fail .....\n\n"


def ANSIRender(data):
    """
    Return the .ans file data unpacked & in the correct 437 codepage
    """
    #Check terminal width, a width different to 80 normally causes problems
    rows, cols = os.popen('stty size', 'r').read().split()
    if cols != "80":
        raw_input("\n[!] The width of the terminal is %s rather than 80, this can often cause bad rendering of the .ANS file. Please adjust terminal width to be 80 and press any key to continue....\n"%(cols))

    ans_out = ""
    for a in data:
        ans_out += chr(struct.unpack("B", a)[0]).decode('cp437')

    return ans_out


if __name__ == "__main__":
    """
    Print the ANSI data (using colorama, if found & needed)
    On OSX the best results are achieved if Courier New or Terminus fixed width fonts are used
    and the terminal is set to 80 chars wide.
    """
    import sys
    data = open(sys.argv[1], "rb").read()

    print ANSIRender(data)


