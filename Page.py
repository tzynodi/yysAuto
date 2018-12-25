import util as util
import threading
import time

class Page :
    pageType = {
        'initCompany'                   : 0,
        'initLoad'                      : 1,
        'initAnimate'                   : 2,
        'initNotice'                    : 3,
        'initEnterGame'                 : 4,
        'initChangePlayer'              : 5,
        'home'                          : 6,
        'discover'                      : 7,
        'discoverYuHun'                 : 8,
        'discoverYuHunChangeFloor'      : 9,
        'discoverYuHunSelectTeam'       : 10,
        'discoverYuHunCreateTeam'       : 11,
        'discoverYuHunWaitTeam'         : 12,
        'inGameReady'                   : 13,
        'inGameWaitReady'               : 14,
        'inGame'                        : 15,
        'endGameVictoryExprience'       : 16,
        'endGameVictoryItem'            : 17,
        'endGameFail'                   : 18,
        'endGameInviteTeamate'          : 19,
        'UNKNOWN'                       : 999
    }

    pageTypeInfo = {
        'initCompany'                   : {'index': 0, 'num': 1},
        'initLoad'                      : {'index': 1, 'num': 1},
        'initAnimate'                   : {'index': 2, 'num': 0},
        'initNotice'                    : {'index': 3, 'num': 1},
        'initEnterGame'                 : {'index': 4, 'num': 1},
        'initChangePlayer'              : {'index': 5, 'num': 1},
        'home'                          : {'index': 6, 'num': 1},
        'discover'                      : {'index': 7, 'num': 1},
        'discoverYuHun'                 : {'index': 8, 'num': 1},
        'discoverYuHunChangeFloor'      : {'index': 9, 'num': 2},
        'discoverYuHunSelectTeam'       : {'index': 10, 'num': 2},
        'discoverYuHunCreateTeam'       : {'index': 11, 'num': 1},
        'discoverYuHunWaitTeam'         : {'index': 12, 'num': 1},
        'inGameReady'                   : {'index': 13, 'num': 1},
        'inGameWaitReady'               : {'index': 14, 'num': 1},
        'inGame'                        : {'index': 15, 'num': 2},
        'endGameVictoryExprience'       : {'index': 16, 'num': 1},
        'endGameVictoryItem'            : {'index': 17, 'num': 1},
        'endGameFail'                   : {'index': 18, 'num': 1},
        'endGameInviteTeamate'          : {'index': 19, 'num': 1},
        'UNKNOWN'                       : {'index': 999, 'num': 0}
    }

    def __init__(self, hW):
        self.judgeValue = 0.7
        # windows handle
        self.hW = hW
        # left, top, right, bottom
        self.windowPos = util.getWindowPos(hW)
        # w, h
        self.windowSize = (self.windowPos[2] - self.windowPos[0], self.windowPos[3] - self.windowPos[1])
        self.windowOffest = (0, 0)
        self.imageSet = {}
        self.initImageSet()
        self.prevPage = self.pageType['UNKNOWN']
        self.nowPage = self.pageType['UNKNOWN']
        self.pageThreadLock = threading.Lock()

        def detectThread(arg):
            while (True):
                try:
                    self.pageThreadLock.acquire()
                    tPage = self.judgePage()
                    #print(tPage)
                    if tPage != self.nowPage and tPage != None:
                        self.prevPage = self.nowPage
                        self.nowPage = tPage
                    elif tPage == None :
                        self.prevPage = self.nowPage
                        self.nowPage = self.pageType['UNKNOWN']
                    self.pageThreadLock.release()
                except Exception as e:
                    print(e)
                time.sleep(1)
                continue

        t = threading.Thread(target=detectThread, args=(1,))
        t.start()

    def initImageSet(self):
        for k,v in self.pageTypeInfo.items():
            self.imageSet[v['index']] = []
            for i in range(0, v['num']):
                self.imageSet[v['index']].append(util.cv2ReadImage("img\\" + k + '_' + str(i) + '.png'))

    def judgePage(self):
        self.wShoot = util.cv2ReadImage(util.windowScreenShoot(self.hW, str(self.hW) + '.png'))
        for k,v in self.pageTypeInfo.items():
            for i in range(0, v['num']):
                wrong = False
                try :
                    mRes = util.getCvImagePosOfCvImage(self.imageSet[v['index']][i], self.wShoot)
                    if mRes[1] < self.judgeValue:
                        wrong = True
                        #print(str(mRes) + '   ' + str(v['index']))
                except Exception as e:
                    wrong = True
                    print(str(e) + '           ' + str(v['index']))
                    break
            if wrong == False:
                return v['index']
        return None