import util as util

judgeValue = 0.7

def judgePage(hW):
    if judgeHome(hW):
        print("At Home Page !")
    elif judgeDiscover(hW):
        print("At Discover Page !")
    elif judgeDiscoverNormalStart(hW):
        print("At Discover Start Page !")
    elif judgeInGameStart(hW):
        print("In Game")
    elif judgeEndGameSuccessExprience(hW):
        print("End Game Success , Get Exprience")
    elif judgeEndGameSuccessGetItem(hW):
        print("End Game Success , Get Item")
    else:
        print("Unknown Page !")

def judgeHome(hW):
    mRes = util.getImagePosOfHWindows("dingzhong.png", hW)
    if mRes[1] > judgeValue:
        return True
    else:
        return False

def judgeDiscover(hW):
    mRes = util.getImagePosOfHWindows("jiejietupo.png", hW)
    if mRes[1] > judgeValue:
        return True
    else:
        return False

#判断探索副本开始界面
def judgeDiscoverNormalStart(hW):
    mRes = []
    mRes.append(util.getImagePosOfHWindows("yaoguaifaxian.png", hW))
    mRes.append(util.getImagePosOfHWindows("diaoluojiangli.png", hW))
    mRes.append(util.getImagePosOfHWindows("tansuoanniu.png", hW))
    print(mRes)
    if mRes[0][1] > judgeValue and mRes[1][1] > judgeValue and mRes[2][1] > judgeValue:
        return True
    else:
        return False

#判断探索副本开始界面
def judgeDiscoverNormalStart(hW):
    mRes = []
    mRes.append(util.getImagePosOfHWindows("yaoguaifaxian.png", hW))
    mRes.append(util.getImagePosOfHWindows("diaoluojiangli.png", hW))
    mRes.append(util.getImagePosOfHWindows("tansuoanniu.png", hW))
    if mRes[0][1] > judgeValue and mRes[1][1] > judgeValue and mRes[2][1] > judgeValue:
        return True
    else:
        return False

#判断游戏中
def judgeInGameStart(hW):
    mRes = []
    mRes.append(util.getImagePosOfHWindows("ingamepugong.png", hW))
    mRes.append(util.getImagePosOfHWindows("ingameyaoshu.png", hW))
    mRes.append(util.getImagePosOfHWindows("ingamezhenwang.png", hW))

    mRes.append(util.getImagePosOfHWindows("ingameshoudong.png", hW))
    mRes.append(util.getImagePosOfHWindows("ingamezidong.png", hW))

    mRes.append(util.getImagePosOfHWindows("ingamex1.png", hW))
    mRes.append(util.getImagePosOfHWindows("ingamex2.png", hW))

    #print(mRes)
    if (mRes[0][1] > judgeValue or mRes[1][1] > judgeValue or mRes[2][1] > judgeValue) \
            and (mRes[3][1] > judgeValue or mRes[4][1] > judgeValue)\
            and (mRes[5][1] > judgeValue or mRes[6][1] > judgeValue):
        return True
    else:
        return False

#判断游戏胜利
def judgeEndGameSuccessExprience(hW):
    mRes = util.getImagePosOfHWindows("shengli.png", hW)
    #print(mRes)
    if mRes[1] > judgeValue:
        return True
    else:
        return False

#判断游戏胜利获取奖励
def judgeEndGameSuccessGetItem(hW):
    mRes = util.getImagePosOfHWindows("getitem.png", hW)
    if mRes[1] > judgeValue:
        return True
    else:
        return False