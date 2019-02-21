import csv
import math

def dis_tree(data,rem,index):
    col=len(data[0])
    length = len(index)
    c_no=0
    c_yes=0    
    for i in index:
        if(data[i][col-1] == "No"):
            c_no+=1
        else:
            c_yes+=1
    overall_info_gain = 0
    overall_outcome = -((c_no/(length))*math.log((c_no/(length)),2) + (c_yes/(length))*math.log((c_yes/(length)),2))
    print ("Overall Outcome" ,overall_outcome)    
    entropy=[]
    for k in range(0,col-1):
            entropy.append(0)
    for i in range(1,col-1):
        
        arr = []
        arr.append([])
        for m in range (0,3):
            arr[0].append(0)                
        arr[0][0]=data[1][i]
        z=0
#           print (length)
        for j in index:
            k = 0
            flag = 0 
            while k <= z:
                if(data[j][i] == arr[k][0]):
                    flag = 1
                    if(data[j][5] == "Yes"):
                        arr[k][1]+=1
                    else:
                        arr[k][2]+=1
                    break
                k+=1
           
            if(flag == 0):
                arr.append([])
                for m in range (0,3):
                    arr[z+1].append(0)
                arr[k][0]=data[j][i]
                if(data[j][5] == "Yes"):
                    arr[k][1]+=1
                else:
                    arr[k][2]+=1
                z+=1
#        print(z)  
        print (arr)
        
        
        for l in range (0,z+1):      
            total = arr[l][1] + arr[l][2]
            if(arr[l][1]!=0 and arr[l][2]!=0 ):
#                print(math.log(arr[l][1]/total,2),math.log(arr[l][2]/total,2))
                indi_entro = -(((arr[l][1]/total)*math.log((arr[l][1]/total),2)) + ((arr[l][2]/total)*math.log((arr[l][2]/total),2)))
            elif(arr[l][1]==0):
#                print(math.log(arr[l][2]/total,2))
                indi_entro = -((arr[l][2]/total)*math.log((arr[l][2]/total),2))
            elif(arr[l][2]==0):
#                print(math.log(arr[l][1]/total,2))
                indi_entro = -((arr[l][1]/total)*math.log((arr[l][1]/total),2))
            entropy[i] = entropy[i] + indi_entro*total/(length-1)
        print(entropy[i])
#            a = math.log(arr[l][1]/total,2)
#            b = math.log(arr[l][1]/total,2)
##            print(a,b)
#            indi_entro = -(arr[l][1]/total)*a - (arr[l][2]/total)*b
#            print(indi_entro)
##           indi_entro = -((c_no/(length-1))*math.log((c_no/(length-1)),2) + (c_yes/(length-1))*math.log((c_yes/(length-1)),2))
#            #entropy[i] = entropy[i] + indi_entro
#        #print(entropy[i])
    
    
##########finding overall gain###########################################
    print(entropy)
    gain=[]
    for k in range(0,col-1):
       gain.append(0)
    for i in range(1,col-1):
        gain[i] = overall_outcome-entropy[i]
        print(gain[i])
    print(gain.index(max(gain)))


with open ("wether.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile)
    ##next(csvreader)
    data = [r for r in csvreader]
    #print (data)
    print ("Overall Information gaining")
    col=len(data[0])
    leng=len(data)
    print (leng)
    print (col)
    index=[]
    rem=[]
    for i in range(1,leng):
        index.append(i)
    for i in range(1,col):
        rem.append(i)
    print (index)
    print(rem)
    dis_tree(data,rem,index)
   



                
    