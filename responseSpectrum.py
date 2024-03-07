import math
import numpy as np
import pandas as pd
from Tables import BS_EN_1998_1

class ResponseSpectrum:
    def __init__(self, code='Eurocode3', ag=0.1, step=0.01, soilType='A'):
        self.code = code # 'Eurocode3' by default
        self.soilType = soilType # 'A' by default
        # self.T = None
        # self.T1 = None
        # self.T2 = None
        # self.T3 = None
        self.ag = ag
        self.dampR = 5 # %
        self.dampCorFac = math.sqrt(10/(5+self.dampR))
        self.step = step
        self.TimeAcc()
        self.Acc2VD()

    def TimeAcc(self, rstype='type1'):
        if self.code == 'Eurocode3':
            if rstype=='type1':
                self.table = BS_EN_1998_1.Tables().type1
            else:
                self.table = BS_EN_1998_1.Tables().type2
                
                
            self.refTable = self.table.loc[self.table["Ground Type"]==self.soilType]
            self.S = self.refTable.S.values[0]
            T1 = self.refTable.T1.values[0]
            T2 = self.refTable.T2.values[0]
            T3 = self.refTable.T3.values[0]
                       
            self.T1=np.arange(0, T1, self.step)
            self.T2=np.arange(T1, T2, self.step)
            self.T3=np.arange(T2, T3, self.step)
            self.T4=np.arange(T3, 4, self.step)
            
            self.Sa1 = self.ag*self.S*(1+self.T1/T1*(self.dampCorFac*2.5-1))
            self.Sa2 = self.ag*self.S*self.dampCorFac*2.5*np.ones(np.shape(self.T2))
            self.Sa3 = self.ag*self.S*self.dampCorFac*2.5*(T2/self.T3)
            self.Sa4 = self.ag*self.S*self.dampCorFac*2.5*(T2*T3/self.T4**2)
            
            self.T = np.concatenate([self.T1,self.T2,self.T3,self.T4])
            self.Sa = np.concatenate([self.Sa1,self.Sa2,self.Sa3,self.Sa4])

    def Acc2VD(self):
        self.Sd = 9.81*self.Sa*(self.T/(math.pi*2))**2
        self.Sv = 9.81*self.Sa*(self.T/(math.pi*2))
        

    # def DispAccPlot():
    #     return

# rs = ResponseSpectrum(soilType="B")
# a = rs.T
# b = rs.Sd





