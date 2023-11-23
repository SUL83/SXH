import os,platform
os.system('git pull')

saif=platform.architecture()[0]
if saif=="32bit":
    print('Sorry 32 Bit Not Saported...')
elif trt=="64bit":
    __import__("sxh.py")