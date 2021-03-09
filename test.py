class WasRun:
    def __init__(self, name):
        self.wasRun= None
        self.name= name
    
    def testMethod (self):
        self.wasRun= 1
        
test = WasRun("testMethod")
print (test.wasRun)
test.run()
print (test.wasRun)
    