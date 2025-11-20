import mp3play
filename = r'H:\\金子涵 - 浪子渎.mp3'
mp3 = mp3play.load(filename)
mp3.play()
# Let it play for up to 30 seconds, then stop it.
import time
time.sleep(min(30, mp3.seconds()))
mp3.stop()