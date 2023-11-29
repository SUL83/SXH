import os,platform
os.system('git pull')

saif=platform.architecture()[0]
if saif=="32bit":
    print('Sorry 32 Bit Not Saported...')
elif saif=="64bit":
    __import__("SXH.py")
