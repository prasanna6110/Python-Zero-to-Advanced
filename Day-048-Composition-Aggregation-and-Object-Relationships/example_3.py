# Day 048 · Composition, Aggregation and Object Relationships — Swappable parts: composition instead of inheritance
# Run: python example_3.py

class LoudSpeaker:
    def say(self, text): return text.upper() + "!!!"

class Whisper:
    def say(self, text): return text.lower() + "..."

class Robot:
    def __init__(self, name, voice):
        self.name, self.voice = name, voice
    def greet(self):
        return f"{self.name}: {self.voice.say('Hello Human')}"

r = Robot("R2", LoudSpeaker())
print(r.greet())
r.voice = Whisper()                      # change behaviour at runtime
print(r.greet())
