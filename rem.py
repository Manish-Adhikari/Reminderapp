import time
import datetime
import currentfile
import os

def reminderapp(date_entry,time_entry):
	
	year,month,day=date_entry.split('-')
	hrs,mins,secs=time_entry.split('-')
	year=int(year);month=int(month);day=int(day)
	hrs=int(hrs);mins=int(mins);secs=int(secs)
	epoch= datetime.datetime(year,month,day,hrs,mins,secs).strftime('%s')
	return epoch
    
  
if __name__=='__main__':
    date_entry=input('Enter the date in YYYY-MM-DD form\t')
    time_entry=input('Enter the time in HRS-MINS-SEC in 24 Hrs Form\t')
    epoch=reminderapp(date_entry,time_entry)
    epoch=int(epoch)
    cepoch=currentfile.current()
    if epoch>cepoch:
       	msg=input('Enter the Notification Message')
        while True:
            cepoch=currentfile.current()
            cepoch=int(cepoch)
            if epoch==cepoch:
                title='REMINDER: :) :)\n '
                os.system('notify-send "'+title+'" "'+msg+'"')
                break;
    else:
        head='Error!!! :( \n' 
        mst='Invalid Entry'
        os.system('notify-send "'+head+'" "'+mst+'"')
        print('OOPS! Invalid Entry')
    


