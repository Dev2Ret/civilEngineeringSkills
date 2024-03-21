import os
import sys
import comtypes.client

class SapInit:
    def __init__(self, path, fileName, existing_file=False):
        #set the following flag to True to attach to an existing instance of the program
        #otherwise a new instance of the program will be started
        self.AttachToInstance = existing_file

        #if False, the lastest installed version of SAP2000 will launch.
        self.SpecifyPath = False

        #if self.SpecifyPath=True, specify the path to SAP2000 below
        self.ProgramPath = 'C:\Program Files\Computers and Structures\SAP2000 23\SAP2000.exe'
        # ProgramPath = 'C:\Program Files\Computers and Structures\SAP2000 22\SAP2000.exe'
        

        #full path to the model
        #set it to the desired path of your model

        self.APIPath = path

        if not os.path.exists(self.APIPath):
                try:
                    os.makedirs(self.APIPath)
                    print ("New directory created on " + self.APIPath)
                except OSError:
                    pass

        self.ModelPath = self.APIPath + os.sep + fileName + '.sdb'

        #create API helper object
        helper = comtypes.client.CreateObject('SAP2000v1.Helper')
        self.helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)

        if self.AttachToInstance:
            #attach to a running instance of SAP2000
            try:
                #get the active SapObject
                self.mySapObject = self.helper.GetObject("CSI.SAP2000.API.SapObject") 
            except (OSError, comtypes.COMError):
                print("No running instance of the program found or failed to attach.")
                sys.exit(-1)
        else:
            if self.SpecifyPath:
                try:
                    #create an instance of the SAPObject from the specified path
                    self.mySapObject = self.helper.CreateObject(self.ProgramPath)
                except (OSError, comtypes.COMError):
                    print("Cannot start a new instance of the program from " + self.ProgramPath)
                    sys.exit(-1)
            else:
                try:
                    #create an instance of the SAPObject from the latest installed SAP2000
                    self.mySapObject = self.helper.CreateObjectProgID("CSI.SAP2000.API.SapObject")
                except (OSError, comtypes.COMError):
                    print("Cannot start a new instance of the program.")
                    sys.exit(-1)

            #start SAP2000 application
            self.mySapObject.ApplicationStart()
        
        self.CreateModel()

    def CreateModel(self):
        if os.path.exists(self.ModelPath):
            print(f"Opening existing model at {self.ModelPath}")
            self.SapModel = self.mySapObject.SapModel
            self.ret = self.SapModel.File.OpenFile(self.ModelPath)
        else:
            print("Creating new model")
            #create SapModel object
            self.SapModel = self.mySapObject.SapModel
            
            #initialize model
            self.SapModel.InitializeNewModel()

            #create new blank model
            self.ret = self.SapModel.File.NewBlank()