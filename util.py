import win32api,win32gui,win32con,win32ui
import cv2
from ctypes import *
import wx
import os

def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)

def getCurPos():
    return win32gui.GetCursorPos()

def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)

def cv2ReadImage(fileName):
    return cv2.imread(fileName, 0)

def findWindow(name):
    def _MyCallback(hwnd,extra):
        temp=[]
        temp.append(hwnd)
        temp.append(win32gui.GetClassName(hwnd))
        temp.append(win32gui.GetWindowText(hwnd))
        extra[hwnd] = temp
    windows = {}
    win32gui.EnumWindows(_MyCallback, windows)
    for item in windows:
        #print(windows[item])
        for si in windows[item]:
            if type(si) == str and si.lower().find(name.lower()) >= 0 :
                return windows[item][0]
            else :
                continue
    return None

#获取窗口左上角和右下角坐标
def getWindowPos(wHandle):
    return win32gui.GetWindowRect(wHandle)

#获取指定图片在屏幕中的位置
def getImagePosOfCurWindows(s):
    screenShoot('s.bmp')
    bImage = cv2.imread('s.bmp',0)
    sImage = cv2.imread(s, 0)
    return getImagePos(sImage, bImage)

def wxRect():
    app = wx.App(False)
    s = wx.ScreenDC()
    s.Pen = wx.Pen("#FF0000")
    s.DrawLine(60, 60, 120, 120)

def appendFrameRectToWindow(hW, x, y, w, h):
    hDc = win32gui.GetWindowDC(hW)
    hPen = win32gui.CreatePen(win32con.PS_SOLID,10,win32api.RGB(255,0,255))
    win32gui.FrameRect(hDc,(x,y,x+w,y+h),hPen)

def appendFrameRectToDCWindowWithhPen(hDc, hPen, x, y, w, h):
    win32gui.FrameRect(hDc,(x,y,x+w,y+h),hPen)

#获取指定图片在指定窗口中的位置
def getImagePosOfHWindows(s, hW):
    windowScreenShoot(hW,'w.bmp')
    bImage = cv2.imread('w.bmp',0)
    sImage = cv2.imread(s, 0)
    min_val, max_val, min_loc, max_loc = getImagePos(sImage, bImage)
    left, top, right, bottom = getWindowPos(hW)
    rMax_locX = max_loc[0]# + left
    rMax_locY = max_loc[1]# + top
    return min_val, max_val, min_loc, (rMax_locX, rMax_locY)

#获取指定图片在指定指定图片中的位置
def getCvImagePosOfCvImage(sCvImg, bCvImg):
    return getImagePos(sCvImg, bCvImg)

#获取指定图片在指定窗口中的位置
def getImagePosOfWindows(s, windowName):
    h = findWindow(windowName)
    windowScreenShoot(h,'w.bmp')
    bImage = cv2.imread('w.bmp',0)
    sImage = cv2.imread(s, 0)
    min_val, max_val, min_loc, max_loc = getImagePos(sImage, bImage)
    left, top, right, bottom = getWindowPos(h)
    rMax_locX = max_loc[0]# + left
    rMax_locY = max_loc[1]# + top
    return min_val, max_val, min_loc, (rMax_locX, rMax_locY)
    
#查找图片位置
def getImagePos(s, b):
    res = cv2.matchTemplate(b,s,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return min_val, max_val, min_loc, max_loc
    
#屏幕截图
def screenShoot(filename):
    hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    return filename
  
#窗口截图
def windowScreenShoot(hwnd,filename):
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    return filename
  
#获取图片长宽
def getImageSize(fileName) :
    template = cv2.imread(fileName, 0)  
    return template.shape[:2]  # rows->h, cols->w

def getFileInDir(dirName) :
    list = os.listdir(dirName)  # 列出文件夹下所有的目录与文件
    resList = []
    for i in range(0, len(list)):
        path = os.path.join(dirName, list[i])
        if os.path.isfile(path):
            fileName = path[len(dirName) + 1 : len(path)]
            resList.append(fileName)
    return resList