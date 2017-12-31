#! /usr/bin/env python
# encoding: utf-8
import npyscreen
import os
from subprocess import call
from subprocess import PIPE
from subprocess import Popen

test_text = """
q           exit omxplayer
p / space   pause/resume
-           decrease volume
+ / =       increase volume
left arrow  seek -30 seconds
right arrow seek +30 seconds
down arrow  seek -600 seconds
up arrow    seek +600 seconds
<           rewind
>           fast forward
z           show info

1           decrease speed
2           increase speed
j           previous audio stream
k           next audio stream
i           previous chapter
o           next chapter
n           previous subtitle stream
m           next subtitle stream
s           toggle subtitles
w           show subtitles
x           hide subtitles
d           decrease subtitle delay (- 250 ms)
f           increase subtitle delay (+ 250 ms)

"""

class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        global file_name
        file_name=self.fn2.value
        self.parentApp.setNextForm(None)
        #print("Ciao")
        

    def create(self):
        t  = self.add(npyscreen.TitleFixedText, name = "Seleziona un file da guardare")
        #self.fn2 = self.add(npyscreen.TitleFilenameCombo, name="Filename:", label=True)
        self.fn2 = self.add(npyscreen.TitleFilenameCombo, name="Filename:")
        self.TP = self.add(npyscreen.TitlePager, name="Istruzioni", autowrap=True, values=test_text.split("\n"))
        #self.edit()
        

class MyApplication(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', myEmployeeForm, name='Video_Player')


if __name__ == '__main__':
   path = "/media/VideoHDD/Video/"
   # Now change the directory
   os.chdir( path )
   TestApp = MyApplication().run()
   #print("Ciao")
   print(file_name)
   print("Eseguo il video selezionato...")
   unused_variable = os.system("clear")
   omxc = call(['omxplayer', '-b', file_name])
   #omxc = Popen(['omxplayer', '-b', file_name])
   #omxc = Popen(['cvlc', file_name])
   #unused_variable = os.system("clear")
   #print("finito")
   
   
