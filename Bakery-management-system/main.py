from datetime import date
import pandas as pd
order={'customer_name':[],'item_ordered':[],'quantity':[],'price':[],'total':[],'order_date':[]}
def addorder(count):
    order['customer_name'].append(input("Enter customer name:  "))
    order['item_ordered'].append(input("Enter the item to be order:  "))
    order['quantity'].append(int(input("Enter the quantity:  ")))
    order['price'].append(int(input("Enter the price:  ")))
    order['total'].append(order['quantity'][count]*order['price'][count])
    order['order_date'].append(str(date.today()))
    print("\nData added successfully\n\n")
    count=count+1
def vieworder():
    df=pd.DataFrame(order,index=None)
    print("\n",df,"\n\n")   
def updateorder():
    oid=int(input("Enter customer id:  "))
    if oid>=len(order['customer_name']):print("Enter valid id")
    else:
        order['customer_name'][oid]=input("Enter new customer name:  ")
        order['item_ordered'][oid]=input("Enter new item to be order:  ")
        order['quantity'][oid]=int(input("Enter new quantity:  "))
        order['price'][oid]=int(input("Enter new price:  "))
        order['total'][oid]=order['quantity'][count]*order['price'][count]
        print("\nupdated successfully\n\n")
def savetoexcel():
    df=pd.DataFrame(order)
    df.to_csv(str(date.today())+".csv")
    print("data saved to exell sheet succesfully\n\n")
print("1.Add order\n2.View order\n3.update order\n4.Save to excel\n5.Exit")
ch=1
count=0
while(ch):
    ch=int(input("Enter your choice:  "))
    if ch==1:addorder(count)
    elif ch==2:vieworder()
    elif ch==3:updateorder()
    elif ch==4:savetoexcel()
    elif ch==5: exit(0)
    else: print("Enter valid input")