input_data=86467
days=input_data//86400
minutes = (input_data-days*86400)//60
seconds = (input_data-days*86400-minutes*60)
print("days:"+str(days))
print("minutes:"+str(minutes))
print("seconds:"+str(seconds))