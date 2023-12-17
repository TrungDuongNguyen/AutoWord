import os
import pyinputplus as pyip
from pathlib import Path
import shutil, os




listtypes = ["txts","exes","images","mp3","mp4"]

a = Path.cwd()

#print(a)
#check if directory exists, then creates
for types in listtypes:  
        end = types
        isExist = os.path.exists(end)
        print(isExist)

        if not isExist:               
                os.makedirs(types)
             
txtlst = list(a.glob('*.txt'))
for filename in a.glob('*.txt'):
    {
        shutil.move(filename,a/ 'txts')
    }
    #move file to directory{} """     

exelst = list(a.glob('*.exe'))
for filename in a.glob('*.exe'):
    {
        shutil.move(filename,a/ 'exes')
    }
    #move file to directory{} """  

imglst = list(a.glob('*.jpg'))
for filename in a.glob('*.jpg'):
    {
        shutil.move(filename,a/ 'images')
    }
imglst = list(a.glob('*.png'))
for filename in a.glob('*.png'):
    {
        shutil.move(filename,a/ 'images')
    }

mp3lst = list(a.glob('*.mp3'))
for filename in a.glob('*.mp3'):
    {
        shutil.move(filename,a/ 'mp3s')
    }
    #move file to directory{} """  

mp4lst = list(a.glob('*.mp4'))
for filename in a.glob('*.mp4'):
    {
        shutil.move(filename,a/ 'mp4s')
    }
    #move file to directory{} """  
""" os.rmdir('./txts')
os.rmdir('./exes')
os.rmdir('./images')  
os.rmdir('./mp4')  
os.rmdir('./mp3')      """   
                
             


""" print('You can choose how you want to organize your files')
sorttype = pyip.inputMenu(['type','size'], numbered=True) """


""" 
pdflst = list(a.glob('*.pdf'))
print (pdflst)

exelst = list(a.glob('*.exe'))
print (exelst)

imglst = list(a.glob('*.jpg'))
print (imglst)

mp3lst = list(a.glob('*.mp3'))
print (mp3lst)

mp4lst = list(a.glob('*.mp4'))
print (mp4lst) 

 """