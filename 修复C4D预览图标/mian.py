import os
from win32api import MessageBox
ml = os.getcwd()+"\win_thumbnail.dll"
zhml = "regsvr32 \""+ml+"\""
def C_c4d():
    C_C4d_M= os.path.exists(ml)
    if (C_C4d_M):
        p=os.popen(zhml)
        print (p.read())
    else:
        MessageBox(0,"DLL模块不存在","A4提示")
C_c4d()
