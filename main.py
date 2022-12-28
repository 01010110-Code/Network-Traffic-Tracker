# First, you need to install the Wireshark command-line interface (CLI) and Python bindings
!apt-get update && apt-get install -y wireshark-cli python3-pyshark

# Import the necessary libraries
import subprocess
import pyshark

# Use the Wireshark CLI to capture packets on the network interface eth0
capture = pyshark.LiveCapture(interface='eth0')

# Start the capture and apply a filter to only show HTTP traffic
capture.sniff(filter='http')

# Iterate through the packets and print the source and destination IP addresses
for packet in capture.sniff_continuously():
  print(f'Source: {packet.ip.src} Destination: {packet.ip.dst}')
