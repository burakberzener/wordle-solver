import subprocess
import unicodedata
import pyperclip

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

#currently_copied_content = pyperclip.paste()
f = open("result.txt", 'w')
#result = getClipboardData()7
unicode = "🟩"
normal = unicodedata.normalize('NFKD', unicode).encode('ascii', 'ignore')
print(u"🟩")