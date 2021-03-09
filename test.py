class TestCase:
    def __init__(self, name):
        self.name= name

    def setUp(self):
        pass    

    def run(self):
        self.setUp()
        method = getattr(self,self.name)
        method()      

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun= None
        self.wasSetUp= None
        TestCase.__init__(self,name)  

    def setUp(self):
        self.wasRun= None
        self.wasSetUp= 1      
    
    def testMethod (self):
        self.wasRun= 1


class TestCaseTest(TestCase):

    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasRun)

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)    

TestCaseTest("testSetUp").run()
TestCaseTest("testRunning").run()

        


    