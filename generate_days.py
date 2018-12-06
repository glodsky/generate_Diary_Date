# -*- coding: utf-8 -*-
# python version : 3.6

import os 
import datetime

def main(): 
    ToGenerateDays = 365  #  
    Days = []
    for i in range(0,ToGenerateDays):
        d = (datetime.datetime.now()+datetime.timedelta(days= +(i) )).strftime("%Y%m%d")
        Days.append( d )

    s_days = "\n".join(Days)    
##    for day in Days:
##        s_days = "%s\n%s"%(s_days,day)
        
    with open('./DaysRecords_%s.txt'%datetime.datetime.now().strftime("%Y%m%d"),'a',encoding='utf-8') as fn:
        fn.write(s_days)
        fn.close()
    
 
if __name__ == '__main__':    
    main()
