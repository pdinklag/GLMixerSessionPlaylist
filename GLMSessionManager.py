import os
import xml.etree.ElementTree as ET

from pythonosc import udp_client

class GLMSession:
    def __init__(self, filename):
        self.filename = filename
        
        # parse XML and try to find a duration
        self.duration = 0
        
        print(filename)
        tree = ET.parse(filename)
        root = tree.getroot()
        for tag in root.findall('./SourceList/Source/TypeSpecific[@type="2"]'):
            # media source, the duration equals the difference between In and Out marks
            marks = tag.find('Marks')
            inMark = marks.get('In')
            outMark = marks.get('Out')
            if inMark and outMark:
                self.duration = max(self.duration, float(outMark) - float(inMark))

        if self.duration == 0:
            self.duration = 10 # TODO: make default duration configurable

class GLMSessionManager:
    def __init__(self, host, port, path, curSession = 0):
        self.sessions = []
        for filename in os.listdir(path):
            if filename.endswith('.glm'):
                self.sessions.append(GLMSession(os.path.join(path, filename)))
        
        self.num = len(self.sessions)
        self.cur = curSession
        
        self.client = udp_client.SimpleUDPClient(host, port)
        
    def switch_to(self, i):
        if i != self.cur:
            dist = i - self.cur
            while dist > 0:
                self.client.send_message('/glmixer/render/Next', 0)
                dist -= 1
            while dist < 0:
                self.client.send_message('/glmixer/render/Previous', 0)
                dist += 1

            self.cur = i

