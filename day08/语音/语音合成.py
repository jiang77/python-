import time
# 系统客户端
import win32com.client

dehua = win32com.client.Dispatch("SAPI.SPVOICE")
dehua.Speak("sunnck is a good man")

while True:
    dehua.Speak("sunck is a good man")
    time.sleep(3)
    dehua.Speak("sunck is a handsome man")
    time.sleep(3)