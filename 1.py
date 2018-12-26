import util as util
import win32api,win32gui,win32con,win32ui
import time
import threading
import judge
import Page
import AutoYuHun
import Mouse

def main():
    print("Start !")
    
    mouse = Mouse.Mouse()
    hW = util.findWindow("UltraEdit")
    mouseTask = Mouse.MouseTask("click", None, hW, {"pos":(0,0)})
    mouse.addMouseTask

#    hW = util.findWindow("阴阳师")

#    pageInstance = Page.Page(hW)
#    autoYuHun = AutoYuHun.AutoYuHun(pageInstance)

#    while(True):
#        try :
#            print(list(pageInstance.pageType.keys())[list(pageInstance.pageType.values()).index(pageInstance.nowPage)])
#        except Exception as e:
#            print(pageInstance.nowPage)
#            print(e)
#        time.sleep(1)
        
    print("End !")


main()