import pandas as pd
def createList(r1,r2):
  return [item for item in range(r1, r2)]
cols=createList(2,300)
w2con=pd.read_excel('w2_con_DeGray4.5.xlsm',sheet_name='w2_con.csv',header=None,usecols=cols)
w2con=w2con.fillna('')
w2con.to_csv('w2_con.csv',header=False,index=False)