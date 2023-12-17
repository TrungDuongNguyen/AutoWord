import os
import pyinputplus as pyip
from pathlib import Path
import shutil, os


""" print('You can choose how you want to organize your files')
sorttype = pyip.inputMenu(['type','size'], numbered=True) """

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

""" os.rmdir('./txts')
os.rmdir('./exes')
os.rmdir('./images')  
os.rmdir('./mp4')  
os.rmdir('./mp3')      """   
                
             





""" print('You can choose how you want to organize your files')
sorttype = pyip.inputMenu(['type','size'], numbered=True) """

""" print(a)
#b = os.path.dirname(a)
#print(b)
txtlst = list(a.glob('*.txt'))
for filename in a.glob('*.txt'):
    {
        shutil.move(filename,a/ 'txts')
    }
    #move file to directory{} """

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
print (mp4lst) """


""" if sorttype =='type':
    {

    } """



