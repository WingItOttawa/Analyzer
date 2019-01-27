import sched, time
import firebase

class Processor:
    def __init__(self):
        self.db = firebase.Database()
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def run(self):
        self.scheduler.enter(0, 1, self.processDocuments)
        self.scheduler.run()

    def processDocuments(self):
        print("Processing documents...")
        docs = self.db.retrieveDocuments()
        self.scheduler.enter(10, 1, self.processDocuments)

proc = Processor()
proc.run()
