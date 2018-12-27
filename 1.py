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

    hWList = util.findWindowList("阴阳师")
    mouse = Mouse.Mouse()

    for hW in hWList:
        pageInstance = Page.Page(hW)
        autoYuHun = AutoYuHun.AutoYuHun(pageInstance, mouse)

    while(True):
        try :
            print(list(pageInstance.pageType.keys())[list(pageInstance.pageType.values()).index(pageInstance.nowPage)])
        except Exception as e:
            print(pageInstance.nowPage)
            print(e)
        time.sleep(1)
        
    print("End !")


main()