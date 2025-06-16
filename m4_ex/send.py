from scapy.all import *
import sys

def send_bad():
    print("Sending BAD packet...")
    # TODO: malicious packets code here

def send_good():
    print("Sending GOOD packet...")
    # TODO: normal packets code here

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["good", "bad"]:
        print("Usage: python3 send.py [good|bad]")
        sys.exit(1)
    if sys.argv[1] == "good":
        send_good()
    else:
        send_bad()
