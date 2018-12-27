import util as util
import threading
import time
import Mouse

class AutoYuHun:

    def __init__(self, page, mouse):
        self.initImageSet()
        self.page = page
        self.mouse = mouse
        self.operateTime = 0

        def autoRunYuHunThread(arg):
            while (True):
                try:
                    if int(round(time.time() * 1000)) - self.operateTime < 2000 : #最快2s操作一次
                        time.sleep(0.5)
                        continue
                    self.operateTime = int(round(time.time() * 1000))
                    self.page.pageThreadLock.acquire()
                    if page.nowPage == page.pageType['UNKNOWN']\
                            or page.nowPage == page.pageType['initCompany'] \
                            or page.nowPage == page.pageType['initLoad'] \
                            or page.nowPage == page.pageType['initAnimate'] \
                            or page.nowPage == page.pageType['initNotice'] \
                            or page.nowPage == page.pageType['initEnterGame'] \
                            or page.nowPage == page.pageType['initChangePlayer'] \
                            or page.nowPage == page.pageType['discoverYuHunSelectTeam'] \
                            or page.nowPage == page.pageType['discoverYuHunCreateTeam']:#未知页面提示等待
                        print("请至少跳转到刷御魂开始界面")
                    elif page.nowPage == page.pageType['home'] : #主页
                        self.jumpPage(6, 7)
                    elif page.nowPage == page.pageType['discover'] : #探索
                        self.jumpPage(7, 8)
                    elif page.nowPage == page.pageType['discoverYuHun']:  #探索御魂入口
                        self.jumpPage(8, 9)
                    elif page.nowPage == page.pageType['discoverYuHunChangeFloor'] : #选择层数
                        self.jumpPage(9, 13)
                    elif page.nowPage == page.pageType['inGameReady']:  #进游戏准备
                        self.jumpPage(13, 15)
                    elif page.nowPage == page.pageType['endGameVictoryExprience']:  #结束游戏获取经验
                        self.jumpPage(16, 17)
                    elif page.nowPage == page.pageType['endGameVictoryItem']:  #结束游戏获取物品
                        self.jumpPage(17, 9)
                    elif page.nowPage == page.pageType['endGameInviteTeamate']:  #结束游戏重新邀请队友
                        self.checkBoxCheck(19, 12)
                        self.jumpPage(19, 12)
                    elif page.nowPage == page.pageType['discoverYuHunWaitTeam']:  #等待队友一起开始游戏
                        self.jumpPage(12, 13)
                    elif page.nowPage == page.pageType['endGameFail']: #游戏失败
                        self.jumpPage(18, 9)
                    elif page.nowPage == page.pageType['inGame']:  #进游戏准备
                        pass
                    self.page.pageThreadLock.release()
                except Exception as e:
                    print(e)
                continue

        t = threading.Thread(target=autoRunYuHunThread, args=(1,))
        t.start()

    def initImageSet(self):
        imgList = util.getFileInDir("autoimg\\autoYuHun")
        for i in range(0, len(imgList)):
            self.imageSet = {}
            for i in range(0, len(imgList)):
                self.imageSet[imgList[i]] = {}
                self.imageSet[imgList[i]]["img"] = (util.cv2ReadImage("autoimg\\autoYuHun\\" + imgList[i]))
                self.imageSet[imgList[i]]["size"] = (util.getImageSize("autoimg\\autoYuHun\\" + imgList[i]))

    def jumpPage(self, fromPage, toPage):
        buttonImg = str(fromPage) + 'To' + str(toPage) + '.png'
        min_val, max_val, min_loc, max_loc = util.getCvImagePosOfCvImage(self.imageSet[buttonImg]["img"], self.page.wShoot)
        if max_val < self.page.judgeValue :
            return None
        else :
            wLeft, wTop, wRight, wBottom = self.page.windowPos
            iX, iY = max_loc
            print((wLeft, wTop, wRight, wBottom))
            mouseTask = Mouse.MouseTask("click", "left", self.page.hW, {"pos" : (wLeft + iX + self.page.windowOffest[0] + int(self.imageSet[buttonImg]["size"][1] / 2),
                                                                             wTop + iY + self.page.windowOffest[1] + int(self.imageSet[buttonImg]["size"][0] / 2))})
            self.mouse.addMouseTask(mouseTask)

    def checkBoxCheck(self, fromPage, toPage):
        buttonImg = str(fromPage) + 'To' + str(toPage) + 'CheckBox.png'
        min_val, max_val, min_loc, max_loc = util.getCvImagePosOfCvImage(self.imageSet[buttonImg]["img"],
                                                                         self.page.wShoot)
        if max_val < self.page.judgeValue:
            return None
        else:
            wLeft, wTop, wRight, wBottom = self.page.windowPos
            iX, iY = max_loc
            print((wLeft, wTop, wRight, wBottom))
            mouseTask = Mouse.MouseTask("click", "left", self.page.hW, {"pos": (wLeft + iX + self.page.windowOffest[0]
                            , wTop + iY + self.page.windowOffest[1] + int(self.imageSet[buttonImg]["size"][0] / 2))})
            self.mouse.addMouseTask(mouseTask)