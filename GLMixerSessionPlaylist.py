#!/usr/bin/env python3

import argparse
import random
import time

from GLMSessionManager import *

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Update Minecraft statistics')
parser.add_argument('path', type=str,
                    help='path to the GLMixer session folder')
parser.add_argument('--host', type=str, required=False, default='127.0.0.1',
                    help='the IP address of the GLMixer Open Sound Control host')
parser.add_argument('--port', type=int, required=False, default=7000,
                    help='the port on which GLMixer listens for Open Sound Control messages')

args = parser.parse_args()

# Setup keyboard interrupt handling
def interrupt(signal, frame):
    exit(0)

# Create manager
manager = GLMSessionManager(args.host, args.port, args.path)

# Run
while True:
    # Shuffle the playlist
    playlist = list(range(0, manager.num))
    random.shuffle(playlist)
    
    # Play every session in it
    for x in playlist:
        manager.switch_to(x)
        session = manager.sessions[manager.cur]
        print('current session: ' + session.filename + ', duration: ' + str(session.duration) + ' seconds', flush=True)
        time.sleep(session.duration)
