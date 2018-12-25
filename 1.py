import util as util
import win32api,win32gui,win32con,win32ui
import time
import threading
import judge
import Page
import AutoYuHun

def main():
    print("Start !")

    hW = util.findWindow("阴阳师")

    pageInstance = Page.Page(hW)
    autoYuHun = AutoYuHun.AutoYuHun(pageInstance)

    while(True):
        try :
            print(list(pageInstance.pageType.keys())[list(pageInstance.pageType.values()).index(pageInstance.nowPage)])
        except Exception as e:
            print(pageInstance.nowPage)
            print(e)
        time.sleep(1)

    # def detectThread(arg) :
    #     while (True):
    #         whileStartTime = int(round(time.time() * 1000))
    #         try:
    #             judge.judgePage(hW)
    #         except Exception as e:
    #             print(e)
    #         whileEndTime = int(round(time.time() * 1000))
    #         print(whileEndTime - whileStartTime)
    #
    #         time.sleep(1)
    #         continue
    #
    # t = threading.Thread(target=detectThread, args=(1,))
    # t.start()

    print("End !")


main()