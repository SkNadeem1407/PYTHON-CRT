#A To Z
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch+1)
ch=65
Alphabets(ch)

#Z to A
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
      print(chr(ch))
      return Alphabets(ch-1)
ch=90
Alphabets(ch)