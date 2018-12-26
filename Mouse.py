import util as util
import Queue
import threading

class MouseTask:
    def __init__(self, taskType, buttonType, hW, arg):
        self.taskType = taskType
        self.buttonType = buttonType
        self.hW = hW
        if self.taskType == "click":
            self.fromPos = None
            self.toPos = None
            self.pos = arg["pos"]
        elif self.taskType == "drag":
            self.fromPos = arg["fromPos"]
            self.toPos = arg["toPos"]
            self.pos = None

class Mouse:
    def __init__(self):
        self.taskQueue = []
        self.mouseThreadLock = threading.Lock()
        
        def mouseProcessThread(arg):
            while (True):
                try:
                    self.mouseThreadLock.acquire()
                    if len(self.taskQueue) == 0:
                        pass
                    else:
                        execute(getMouseTask())
                    self.mouseThreadLock.release()
                except Exception as e:
                    print(e)
                time.sleep(0.5)
                continue

        t = threading.Thread(target=mouseProcessThread, args=(1,))
        t.start()

    def addMouseTask(self, task):
		    try:
            self.mouseThreadLock.acquire()
            for t in self.taskQueue:
                if t.hW == task.hW:
                    return False
            self.taskQueue.append(task)
            self.mouseThreadLock.release()
            return True
        except Exception as e:
            print(e)
            return False

    def getMouseTask(self):
		    try:
            task = self.taskQueue.pop(0)
            return task
        except Exception as e:
            print(e)
            return None
   
    def executeMouseTask(self, task):
        try:
            util.activeWindow(task.hW)
            if task.taskType == "click":
                util.moveCurPos(task.pos[0], task.pos[1])
                util.clickLeftCur()
            elif task.taskType == "drag":
                pass
            return True
        except Exception as e:
            print(e)
            return False