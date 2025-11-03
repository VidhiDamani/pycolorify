from colorify import Color

c = Color("skyblue")
print("HEX:", c.hex)
print("RGB:", c.rgb)
print("Lightened:", c.lighten(0.2).hex)
print("Random Color:", Color.random().hex)
