import csv
reader = csv.reader(open('athlete_events.csv', 'r'), delimiter=",")
writer_var = open('athlete_thai-medal.txt','w')
counter = 0

for row in reader :
    if (row[12] != "NA") and row[6] =="THA" : 
        counter+=1
        for col in row:
            writer_var.write(str(col)+'\t')
        writer_var.write('\n')        
                
writer_var.write('\nToral medals:'+str(counter))
writer_var.close()
            
            
        



