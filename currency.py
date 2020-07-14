x=str(input("Enter the currency value: "))


def currency(x):
    Single=[" ", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    double=["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
    tens=[" "," ","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
    
    n=float(x)
    
    if n<0 or n>=999999.99:
        print("value should be in the range 0 to 999999.99, PLEASE ENTER AGAIN")
    else:
        d=[0,0,0,0,0,0]
        i=0
        p=int(n)
        while p>0:
            d[i]=p%10
            i+=1
            p=p//10
        
        num="Rs."
        
        if d[5]!=0:
            num+=Single[d[5]]+" Lack "
               
        if d[4]!=0:
            if d[4]==1:
                num+=double[d[3]]+" Thousand "
                
            else:
                num+=tens[d[4]]+" "+Single[d[3]]+" Thousand "
                
        else:
            if d[3]!=0:
                num+=Single[d[3]]+" Thousand "
                
        if d[2]!=0:
            num+=Single[d[2]]+" Hundred "
    
        if d[1]!=0:
            if d[1]==1:
                if d[2]==d[3]==d[4]==d[5]==0:
                    num+=double[d[0]]
                else:
                    num+="And "+double[d[0]]
            else:
                if d[2]==d[3]==d[4]==d[5]==0:
                    num+=tens[d[1]]+" "+Single[d[0]]
                else:
                    num+="And "+tens[d[1]]+" "+Single[d[0]]
        else:
            if d[0]!=0:
                if d[1]==d[2]==d[3]==d[4]==d[5]==0:
                    num+=Single[d[0]]
                else:
                    num+="And "+Single[d[0]]
                    
        try:
            y=x.split('.')[1]
        except:
            y=0
            
        
        t=int(y)
        if t==0:
            print(num+" ONLY")
        else:
            print(num,y+'/'+str(10**len(y))+" ONLY")
               
currency(x)
