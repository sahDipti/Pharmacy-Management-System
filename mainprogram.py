import mysql.connector
import datetime
from reportlab.pdfgen import canvas 


def sql_connection():
    
    try:
        mydb=mysql.connector.connect(host='localhost', user='root', password='9813438460', database='medical_store')
        
    except:
        mydb=mysql.connector.connect(host='localhost', user='root', password='9813438460')

        mycursor=mydb.cursor()
        mycursor.execute('CREATE DATABASE medical_store')
        mycursor.execute('USE medical_store')
        mycursor.execute("CREATE TABLE medicines(medi_id int primary key AUTO_INCREMENT, medi_name varchar(70) , price int, quantity int, expiry_date date)")
        mycursor.execute('CREATE TABLE users(username varchar(70) primary key, password varchar(70), is_staff int , is_admin int, full_name varchar(70))')
        mycursor.execute("CREATE TABLE sold_items(id int primary key AUTO_INCREMENT,sold_on date, sold_to varchar(70) ,quantity_sold int, price int, medicine_id int)")
        mycursor.execute("CREATE TABLE medicine_requests(request_id int primary key AUTO_INCREMENT, medi_name varchar(70) , quantity int)")
        print('DATABASE AND TABLE CREATED')
        
    return mydb




def home(mydb,cart):
    print()
    print()
    XYZ=input("PRESS ENTER TO VIEW HOME PAGE")
    print()
    print()
    print('\t\t*-----Home-----*\t\t')
    print()
    print()
    print('1: View Stock')
    print('2: Add Medicine')
    print('3: Update existing  Medicine')
    print('4: request medicine')
    print('5: View Medicine Requests')
    print('6: Search and Sell Medicine')
    print('7: View Cart')
    print('8: delete medicines')
    print('9: Medicine Info')
    print('10: Exit')
    x=int(input('Enter 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10: '))
    if x == 1:
        view_stock(mydb)
    elif x == 2:
        add_medicine(mydb)
    elif x==3:
        update_medi(mydb)
    elif x==6:
        search_medicine(mydb,cart)
    elif x==7:
        view_cart(cart)
    elif x==5:
        view_requests(mydb,cart)
    elif x==4:
        request_medicine(mydb, cart)
    elif x==8:
        delete_medi(mydb)
    elif x==9:
        all_list()
    else:
        exit()
        
        
def home1(mydb,cart):
    print()
    print()
    XYZ=input("PRESS ENTER TO VIEW HOME PAGE")
    print()
    print()
    print('\t\t*-----Home-----*\t\t')
    print()
    print()
    print('1: View Stock')
    print('2: Add Medicine')
    print('3: Update existing  Medicine')
    print('4: request medicine')
    print('5: View Medicine Requests')
    print('6: Search and Sell Medicine')
    print('7: View Cart')
    print('8: delete medicines')
    print('9: Medicine Info')
    print('10: Remove staff')
    print('11: Exit')
    x=int(input('Enter 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11: '))
    if x == 1:
        view_stock1(mydb)
    elif x == 2:
        add_medicine1(mydb)
    elif x==3:
        update_medi1(mydb)
    elif x==6:
        search_medicine1(mydb,cart)
    elif x==7:
        view_cart1(cart)
    elif x==5:
        view_requests1(mydb,cart)
    elif x==4:
        request_medicine1(mydb, cart)
    elif x==8:
        delete_medi1(mydb)
    elif x==9:
        all_list1()
    elif x==10:
        remove_staff1(mydb)
    else:
        exit()
               

def signup_staff(mydb,cart):
    print()
    print()
    print('\t\t*-----SignUp For Staff-----*\t\t')
    print()
    print()
    is_staff=1
    is_admin=0
    f_name = input('ENTER FULL NAME: ')
    mycursor2 = mydb.cursor()
    mycursor2.execute('select username from users')
    names = mycursor2.fetchall()
    while True:
        u_name = input('ENTER USERNAME: ')
    
        check = (u_name,)
        if check in names:
            print("USERNAME EXISTS")
        else:
            while True:
                password2 = input('ENTER PASSWORD')
                password1 = input('ENTER PASSWORD AGAIN')
                if password2 == password1:
                    sql1 = "INSERT INTO users(username, full_name, password, is_staff, is_admin) VALUES('{}','{}','{}',{},{})".format(u_name,f_name,password2,is_staff,is_admin)
                    mycursor = mydb.cursor()
                    mycursor.execute(sql1)
                    mydb.commit()
                    break
                else:
                    print('PASSWORD DOES NOT MATCH')
            break
    print("SIGNIN SUCCESSFUL")
    z=input('Press ENTER to login')
    login(mydb,cart)
    


def signup_admin(mydb,cart):
    print()
    print()
    print('\t\t*-----SignUp For Admin-----*\t\t')
    print()
    print()
    is_staff=0
    is_admin=1
    f_name = input('ENTER FULL NAME: ')
    mycursor2 = mydb.cursor()
    mycursor2.execute('select username from users')
    names = mycursor2.fetchall()
    while True:
        u_name = input('ENTER USERNAME: ')
    
        check = (u_name,)
        if check in names:
            print("USERNAME EXISTS")
        else:
            while True:
                password2 = input('ENTER PASSWORD')
                password1 = input('ENTER PASSWORD AGAIN')
                if password2 == password1:
                    sql1 = "INSERT INTO users(username, full_name, password, is_staff, is_admin) VALUES('{}','{}','{}',{},{})".format(u_name,f_name,password2,is_staff,is_admin)
                    mycursor = mydb.cursor()
                    mycursor.execute(sql1)
                    mydb.commit()
                    break
                else:
                    print('PASSWORD DOES NOT MATCH')
            break
    print("ADMIN SIGNIN SUCCESSFUL")
    z=input('Press ENTER to login')
    login(mydb,cart)



def login(mydb,cart):
    print()
    print()
    print('\t\t*-----Login-----*\t\t')
    print()
    print()
    mycursor = mydb.cursor()
    mycursor.execute("select username from users")
    u_name=mycursor.fetchall()
    mycursor.execute("select password from users")
    passwd=mycursor.fetchall()
    mycursor.execute("select username from users where is_admin like 1 ")
    data=mycursor.fetchall()
    data2=[]
    for i in data:
        data2.append(i)
    s1=[x[0] for x in data2]
    mycursor.execute("select username from users where is_staff like 1 ")
    rec=mycursor.fetchall()
    rec1=[]
    for i in rec:
        rec1.append(i)
    s2=[x[0] for x in rec1]
    u_names2 =[]
    password2 = []
    users={}
    for i in u_name:
        u_names2.append(i[0])
    for i in passwd:
        password2.append(i[0])
    
    for i in range(len(u_names2)):
        users[u_names2[i]]=password2[i]
    
    while True:
        uname=input("enter username")
        if uname not in u_names2:
            print("username doesnot exist")
            choice=int(input('Enter 1 to signup as STAFF and Enter 2 to signup as ADMIN or enter 3 to log in'))

            if choice == 1:
                signup_staff(mydb,cart)
                login(mydb,cart)
            elif choice==3:
                login(mydb,cart)
            else:
                signup_admin(mydb,cart)
                login(mydb,cart)
        else:
            while True:
                p_word = input('Enter Password: ')
                check_p = users[uname]
                if p_word != check_p:
                    print('INCORRECT PASSWORD')
                else:
                    print('Login Successful')
                    print("!!!!!!!!!!!!!!!!!!WELCOME TO THIS MEDICAL SHOP SOFTWARE!!!!!!!!!!!!!!")
                    if uname in s1:
                        home1(mydb,cart)
                        
                    else:
                        home(mydb,cart)
                        break
                break
            break




def update_medi(mydb):
    mycur=mydb.cursor()
    name=input("enter medicine name")
    price=float(input("enter new price"))
    quantity=int(input("enter quantity"))
    exp_date=input("enter expiry date")
    sql2="UPDATE medicines SET price={}, quantity={}, expiry_date='{}' WHERE medi_name='{}'".format(price, quantity, exp_date,name)
    mycur.execute(sql2)
    mydb.commit()
    print("details of {} successfully updated".format(name))
    home(mydb,cart)




def add_medicine(mydb):
    mycur = mydb.cursor()
    
    data=[]
    sql="select * from medicines"
    mycur.execute(sql)
    res=mycur.fetchall()
    for i in res:
        data.append(i[1])
        
    m_name = input('Medicine name')
    if m_name in data:
        print("given medicine already exists")
        choice=input("enter 1 to update this medicine and enter 2 to add another medicine")
        if choice=='1':
            update_medi(mydb)
        else:
            add_medicine(mydb)
    else:
        price1 = input('Rate')
        quantity2= input('Quantity')
        expdate=input('Expirydate [yyyy-mm-dd]')
        sql1 = "INSERT INTO medicines(medi_name, price, quantity,expiry_date) VALUES('{}',{},{},'{}')".format(m_name,price1,quantity2,expdate)
        mycur.execute(sql1)
        mydb.commit()
        print ( 'Data entered successfully.' )
        home(mydb,cart)




def startup(mydb):
   
    add_medicine()




def view_stock(mydb):
    mycursor = mydb.cursor()
    stock = {}
    mycursor.execute('select * from medicines')
    stocks = mycursor.fetchall()
    fields=['Medicine ID','Medicine Name', 'Rate', 'Quantity', 'Expiry Date']
    for i in stocks:
        medicine_info=[]
        for j in range(len(i)):
            medicine_info.append(i[j])
        stock[i[0]]=medicine_info

    print('Medicine Id\t|\tName\t|\tRate\t|\tQuantity\t|\tExpiry Date\t|\t')
    print('-----------\t|\t----\t|\t-------\t|\t----\t|\t---------\t|\t')
    for i in stock:
        temp=stock[i]
        for j in temp:
            print(j,end='\t\t')
        print()
    home(mydb,cart)    
    return stock
    


def delete_medi(mydb):
    mycur = mydb.cursor()
    name=input("enter the name of the medicine you want to delete:")
    sql="DELETE FROM medicines WHERE medi_name='{}'".format(name)
    mycur.execute(sql)
    mydb.commit()
    print("deleted item '{}' successfully".format(name))
    home(mydb,cart)




def search_medicine(mydb,cart):
    mycursor = mydb.cursor()
    while True:
        search = input('Enter name of medicine to search for : ') 
        search = search.lower()
        if search == 'home':
            home(mydb,cart)
        
        sql1 = "SELECT * FROM medicines WHERE medi_name LIKE '{}'".format(search)
        
        mycursor.execute(sql1) 
        med_info = mycursor.fetchall()
        if len(med_info)<=0:
            print('No such medicine in stock')
            z=int(input('Enter 1 to request medicine or Enter 2 to do to Home'))
            if z==1:
                request_medicine(mydb,cart)
            
                break
            else:
                home(mydb,cart)
        else:
            stock = {}
            
            fields=['Medicine ID','Medicine Name', 'Rate', 'Quantity', 'Expiry Date']
            for i in med_info:
                medicine_info=[]
                for j in range(len(i)):
                    medicine_info.append(i[j])
                stock[i[0]]=medicine_info

            print('Medicine Id\t|\tName\t|\tRate\t|\tQuantity\t|\tQExpiry Date\t|\t')
            print('-----------\t|\t----\t|\t------\t|\t----\t|\t---------\t|')
            for i in stock:
                temp=stock[i]
                for j in temp:
                    print(j,end='\t\t')
                print()
            
            print()
            print()
            temp = int(input('Enter 1 to buy medicine or Enter 2 to exit ')) 
            if temp==1:
                buy_medicine(mydb,med_info,cart)
                home(mydb,cart)   
            else:
               home(mydb,cart)
            break



def request_medicine(mydb,cart):
    mycursor = mydb.cursor()
    req_medicine =input("REQUEST THE MEDICINE NOT IN STOCK:")
    quantity=int(input("enter the quantity you require:"))
    sql1 = "INSERT INTO medicine_requests(medi_name,quantity) VALUES('{}',{})".format(req_medicine,quantity)
    mycursor.execute(sql1)
    mydb.commit()
    print('Medicine Requested')
    home(mydb,cart)
    



def view_requests(mydb,cart):
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM medicine_requests')
    all_requests = mycursor.fetchall()
    print('Request_ID\t\t|\tMedicine Name\t\t|\tQuantity Required')
    for i in all_requests:
        for j in range(len(i)):
            print(i[j],end='\t\t|\t')
        print()
    z=input('press ENTER to go Home')
    home(mydb,cart)




def buy_medicine(mydb,med,cart):
    
    for i in med:
        med_id = i[0]
        med_name = i[1]
        med_rate = i[2]
        med_quantity = i[3]
        med_edate = i[4]
    while True:
        req = int(input("How many packets do you require: "))
        if req<=med_quantity:
            total = med_rate*req
            print('Total Price: ',total)
            buy_info = [med_id,med_name,med_rate,req,total]
            temp = int(input('Enter 1 to add to cart or Enter 2 to change quantity: '))
            if temp==1:
                cart.append(buy_info)
                temp2 = int(input('Enter 1 to proceed to checkout or Enter 2 to buy other medicines: '))
                if temp2 == 1:
                    buyout(mydb,cart)
                elif temp2== 2:
                    search_medicine(mydb,cart)
        else:
            if z==1:
                med = search
                quantity = int(input('Enter how much you want'))
                request_medicine(mydb, med, quantity)
                break
            else:
                home(mydb)
                    


def create_bill(filename,date,name,i_no,data,total_amount):
    pdf = canvas.Canvas(filename)
    pdf.setTitle('bill')
    
    med_name=[]
    for i in data:
        med_name.append(i[1])
        

    pdf.setFont("Times-Roman", 28)
    pdf.drawString(200,750,'Medical Store')
    pdf.setFont("Times-Roman", 25)
    pdf.drawString(250,720,'BILL')

    pdf.setFont("Times-Roman", 13)
    pdf.drawString(450,720,date)
    pdf.setFont("Times-Roman", 18)
    pdf.drawString(50,660,name)
    pdf.drawString(50,640,i_no)
    

    pdf.drawString(50,550, 'Medicine ID  |')
    pdf.drawString(170,550, 'Medicine Name  |')
    pdf.drawString(310,550, 'Rate  |')
    pdf.drawString(370,550, 'Quantity  |')
    pdf.drawString(450,550, 'Price')

    for i in range(50,500,10):

        pdf.drawString(i,570, '-')
        pdf.drawString(i,530, '-')

    pdf.setFont("Times-Roman", 15)
    pos=[70,200,330,390,470]
    y=500
    for i in data:
        for j in range(5):
            pdf.drawString(pos[j],y, str(i[j]))
        y-=30

    pdf.drawString(250,150,'Total amount: ')
    pdf.drawString(350,150,str(total_amount))


    pdf.save()
    print("Bill created and saved to folder")
    
    z=str(input("DO YOU WANT TO PRINT THE RECIEPT?( Y / N ):"))
    if z=="y":
        print( )
        print("""
                                   RECEIPT
                                 ...........
                                 
                             
                             MEDICINE NAME:""", end=" ")
        for i in med_name:
            print(i,end=" , ")
        print()
    
        print(  """\t\t              CUSTOMER NAME:""", name)

        print("                               TOTAL PRICE   :", total_amount)
    
        



def buyout(mydb, cart):
    print(cart)
    mycursor2 = mydb.cursor()
    mycursor2.execute('SELECT * FROM sold_items')
    inv = mycursor2.fetchall()
    n = len(inv)
    
    Current_Date = datetime.datetime.today()
    c_date = str(Current_Date)
    c_date3 = c_date[0:10]
    c_date1 = c_date3.replace('-','_')
    c_date2 = c_date[11:20]
    c_date2 = c_date2.replace(':','_')
    file_name = c_date1 + '_' + c_date2 + '_' + 'bill'
    file_name = file_name.replace('.','_') + '.pdf'
    date = c_date[0:20]
    name=input('Enter Name of the customer: ')
    i_no = 'Invoice Number: '+ str(n+1)
    total = 0
    for i in cart:
        total+=i[4]
    
    create_bill(file_name,date,name,i_no,cart,total)
    mycursor = mydb.cursor()
    for i in cart:
        mycursor.execute("INSERT INTO sold_items(sold_on, sold_to, medicine_id, quantity_sold, price) VALUES('{}','{}',{},{},{})".format(c_date3,name,i[0],i[3],i[4]))
        mycursor.execute("UPDATE medicines SET quantity = quantity - {} WHERE medi_id = {} ".format(i[3],i[0]))
    print('Item Successfully Sold')
    mydb.commit()
    x=input('Press ENTER to go to home')
    home(mydb,cart)



def view_cart(cart):
    print()
    print()
    print('Items in Cart')
    print()
    print()
    print('\tMedicine Name |\t\tQuantity |\t\tPrice |')
    for i in cart:
        print('\t',i[1],'\t\t',i[3],'\t\t',i[4])
    
    home(mydb,cart)


def all_list():
    
    choice=input("1.Do you want to enter medicine detail. 2.View medicine detail")
    
    if choice=='1':
        f=open("store.txt","a")
        ch='y'
        while ch=='y' or ch=='Y':
            name=input("enter the name of medicine")
            price=int(input("enter price"))
            use=input("enter use:")
            f.write(name)
            f.write("\t\t\t\t")
            f.write(str(price))
            f.write("\t")
            f.write(use)
            f.write("\n")
            ch=input("do you want to enter more(y/n)")
        f.close()
    else:
        f=open("store.txt","r")
        s=f.readlines()
        print() 
        print("===========================MEDICINE DETAILS==============================")
        
        print()
        print("   name","\t\t\t","        price","\t\t\t","  uses")
        print("---------","\t\t\t","       ----------","\t\t\t","------------")
        print()
        for i in s:
            print(i,end="\n ")
            
    home(mydb,cart)  
            

def exit():
    z=input('Press ENTER to EXIT')
    
'''
++++++++++++++++++++++++++++admin++++++++++++++++++++
'''
def update_medi1(mydb):
    mycur=mydb.cursor()
    name=input("enter medicine name")
    price=float(input("enter new price"))
    quantity=int(input("enter quantity"))
    exp_date=input("enter expiry date")
    sql2="UPDATE medicines SET price={}, quantity={}, expiry_date='{}' WHERE medi_name='{}'".format(price, quantity, exp_date,name)
    mycur.execute(sql2)
    mydb.commit()
    print("details of {} successfully updated".format(name))
    home1(mydb,cart)




def add_medicine1(mydb):
    mycur = mydb.cursor()
    
    data=[]
    sql="select * from medicines"
    mycur.execute(sql)
    res=mycur.fetchall()
    for i in res:
        data.append(i[1])
        
    m_name = input('Medicine name')
    if m_name in data:
        print("given medicine already exists")
        choice=input("enter 1 to update this medicine and enter 2 to add another medicine")
        if choice=='1':
            update_medi1(mydb)
        else:
            add_medicine1(mydb)
    else:
        price1 = input('Rate')
        quantity2= input('Quantity')
        expdate=input('Expirydate [yyyy-mm-dd]')
        sql1 = "INSERT INTO medicines(medi_name, price, quantity,expiry_date) VALUES('{}',{},{},'{}')".format(m_name,price1,quantity2,expdate)
        mycur.execute(sql1)
        mydb.commit()
        print ( 'Data entered successfully.' )
        home1(mydb,cart)




def startup(mydb):
   
    add_medicine1()




def view_stock1(mydb):
    mycursor = mydb.cursor()
    stock = {}
    mycursor.execute('select * from medicines')
    stocks = mycursor.fetchall()
    fields=['Medicine ID','Medicine Name', 'Rate', 'Quantity', 'Expiry Date']
    for i in stocks:
        medicine_info=[]
        for j in range(len(i)):
            medicine_info.append(i[j])
        stock[i[0]]=medicine_info

    print('Medicine Id\t|\tName\t|\tRate\t|\tQuantity\t|\tExpiry Date\t|\t')
    print('-----------\t|\t----\t|\t-------\t|\t----\t|\t---------\t|\t')
    for i in stock:
        temp=stock[i]
        for j in temp:
            print(j,end='\t\t')
        print()
    home1(mydb,cart)    
    return stock
    


def delete_medi1(mydb):
    mycur = mydb.cursor()
    name=input("enter the name of the medicine you want to delete:")
    sql="DELETE FROM medicines WHERE medi_name='{}'".format(name)
    mycur.execute(sql)
    mydb.commit()
    print("deleted item '{}' successfully".format(name))
    home1(mydb,cart)




def search_medicine1(mydb,cart):
    mycursor = mydb.cursor()
    while True:
        search = input('Enter name of medicine to search for : ') 
        search = search.lower()
        if search == 'home':
            home1(mydb,cart)
        
        sql1 = "SELECT * FROM medicines WHERE medi_name LIKE '{}'".format(search)
        
        mycursor.execute(sql1) 
        med_info = mycursor.fetchall()
        if len(med_info)<=0:
            print('No such medicine in stock')
            z=int(input('Enter 1 to request medicine or Enter 2 to do to Home'))
            if z==1:
                request_medicine1(mydb,cart)
            
                break
            else:
                home1(mydb,cart)
        else:
            stock = {}
            
            fields=['Medicine ID','Medicine Name', 'Rate', 'Quantity', 'Expiry Date']
            for i in med_info:
                medicine_info=[]
                for j in range(len(i)):
                    medicine_info.append(i[j])
                stock[i[0]]=medicine_info

            print('Medicine Id\t|\tName\t|\tRate\t|\tQuantity\t|\tQExpiry Date\t|\t')
            print('-----------\t|\t----\t|\t------\t|\t----\t|\t---------\t|')
            for i in stock:
                temp=stock[i]
                for j in temp:
                    print(j,end='\t\t')
                print()
            
            print()
            print()
            temp = int(input('Enter 1 to buy medicine or Enter 2 to exit ')) 
            if temp==1:
                buy_medicine1(mydb,med_info,cart)
                home1(mydb,cart)   
            else:
               home1(mydb,cart)
            break



def request_medicine1(mydb,cart):
    mycursor = mydb.cursor()
    req_medicine =input("REQUEST THE MEDICINE NOT IN STOCK:")
    quantity=int(input("enter the quantity you require:"))
    sql1 = "INSERT INTO medicine_requests(medi_name,quantity) VALUES('{}',{})".format(req_medicine,quantity)
    mycursor.execute(sql1)
    mydb.commit()
    print('Medicine Requested')
    home1(mydb,cart)
    



def view_requests1(mydb,cart):
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM medicine_requests')
    all_requests = mycursor.fetchall()
    print('Request_ID\t\t|\tMedicine Name\t\t|\tQuantity Required')
    for i in all_requests:
        for j in range(len(i)):
            print(i[j],end='\t\t|\t')
        print()
    z=input('press ENTER to go Home')
    home1(mydb,cart)




def buy_medicine1(mydb,med,cart):
    
    for i in med:
        med_id = i[0]
        med_name = i[1]
        med_rate = i[2]
        med_quantity = i[3]
        med_edate = i[4]
    while True:
        req = int(input("How many packets do you require: "))
        if req<=med_quantity:
            total = med_rate*req
            print('Total Price: ',total)
            buy_info = [med_id,med_name,med_rate,req,total]
            temp = int(input('Enter 1 to add to cart or Enter 2 to change quantity: '))
            if temp==1:
                cart.append(buy_info)
                temp2 = int(input('Enter 1 to proceed to checkout or Enter 2 to buy other medicines: '))
                if temp2 == 1:
                    buyout(mydb,cart)
                elif temp2== 2:
                    search_medicine(mydb,cart)
        else:
            if z==1:
                med = search
                quantity = int(input('Enter how much you want'))
                request_medicine(mydb, med, quantity)
                break
            else:
                home1(mydb)
                    


def create_bill1(filename,date,name,i_no,data,total_amount):
    pdf = canvas.Canvas(filename)
    pdf.setTitle('bill')
    
    med_name=[]
    for i in data:
        med_name.append(i[1])
        

    pdf.setFont("Times-Roman", 28)
    pdf.drawString(200,750,'Medical Store')
    pdf.setFont("Times-Roman", 25)
    pdf.drawString(250,720,'BILL')

    pdf.setFont("Times-Roman", 13)
    pdf.drawString(450,720,date)
    pdf.setFont("Times-Roman", 18)
    pdf.drawString(50,660,name)
    pdf.drawString(50,640,i_no)
    

    pdf.drawString(50,550, 'Medicine ID  |')
    pdf.drawString(170,550, 'Medicine Name  |')
    pdf.drawString(310,550, 'Rate  |')
    pdf.drawString(370,550, 'Quantity  |')
    pdf.drawString(450,550, 'Price')

    for i in range(50,500,10):

        pdf.drawString(i,570, '-')
        pdf.drawString(i,530, '-')

    pdf.setFont("Times-Roman", 15)
    pos=[70,200,330,390,470]
    y=500
    for i in data:
        for j in range(5):
            pdf.drawString(pos[j],y, str(i[j]))
        y-=30

    pdf.drawString(250,150,'Total amount: ')
    pdf.drawString(350,150,str(total_amount))


    pdf.save()
    print("Bill created and saved to folder")
    
    z=str(input("DO YOU WANT TO PRINT THE RECIEPT?( Y / N ):"))
    if z=="y":
        print( )
        print("""
                                   RECEIPT
                                 ...........
                                 
                             
                             MEDICINE NAME:""", end=" ")
        for i in med_name:
            print(i,end="  ")
        print()
    
        print(  """\t\t              CUSTOMER NAME:""", name)

        print("                               TOTAL PRICE   :", total_amount)
    
        



def buyout1(mydb, cart):
    print(cart)
    mycursor2 = mydb.cursor()
    mycursor2.execute('SELECT * FROM sold_items')
    inv = mycursor2.fetchall()
    n = len(inv)
    
    Current_Date = datetime.datetime.today()
    c_date = str(Current_Date)
    c_date3 = c_date[0:10]
    c_date1 = c_date3.replace('-','_')
    c_date2 = c_date[11:20]
    c_date2 = c_date2.replace(':','_')
    file_name = c_date1 + '_' + c_date2 + '_' + 'bill'
    file_name = file_name.replace('.','_') + '.pdf'
    date = c_date[0:20]
    name=input('Enter Name of the customer: ')
    i_no = 'Invoice Number: '+ str(n+1)
    total = 0
    for i in cart:
        total+=i[4]
    
    create_bill1(file_name,date,name,i_no,cart,total)
    mycursor = mydb.cursor()
    for i in cart:
        mycursor.execute("INSERT INTO sold_items(sold_on, sold_to, medicine_id, quantity_sold, price) VALUES('{}','{}',{},{},{})".format(c_date3,name,i[0],i[3],i[4]))
        mycursor.execute("UPDATE medicines SET quantity = quantity - {} WHERE medi_id = {} ".format(i[3],i[0]))
    print('Item Successfully Sold')
    mydb.commit()
    x=input('Press ENTER to go to home')
    home1(mydb,cart)



def view_cart1(cart):
    print()
    print()
    print('Items in Cart')
    print()
    print()
    print('\tMedicine Name |\t\tQuantity |\t\tPrice |')
    for i in cart:
        print('\t',i[1],'\t\t',i[3],'\t\t',i[4])
    
    home(mydb,cart)


def all_list1():
    
    choice=input("1.Do you want to enter medicine detail. 2.View medicine detail")
    
    if choice=='1':
        f=open("store.txt","a")
        ch='y'
        while ch=='y' or ch=='Y':
            name=input("enter the name of medicine")
            price=int(input("enter price"))
            f.write(name)
            f.write("\t")
            f.write(str(price))
            f.write("\n")
            ch=input("do you want to enter more(y/n)")
        f.close()
    else:
        f=open("store.txt","r")
        s=f.readlines()
        print() 
        print("===========================MEDICINE DETAILS==============================")
        
        print()
        print("   name","\t\t\t","        price","\t\t\t","  uses")
        print("---------","\t\t\t","       ----------","\t\t\t","------------")
        print()
        for i in s:
            print(i,end="\n ")
            
    home1(mydb,cart)  
            

def remove_staff1(mydb):
    mycur = mydb.cursor()
    name=input("enter the username of the staff to be removed")
    sql="DELETE FROM users WHERE username='{}'".format(name)
    mycur.execute(sql)
    mydb.commit()
    print("staff '{}' fired successfully".format(name))
    home1(mydb,cart)



    
    



mydb=sql_connection()
cart=[]
print('\t\t\t Medical Store')
print('''\t             
   \                                                          /
    =========================================================
   |                   ___         __   __           ___     |
   |      \        /  |     |     |    |  |  |\  /| |        |
   |       \  /\  /   |--   |     |    |  |  | \/ | |--      |
   |        \/  \/    |___  |____ |__  |__|  |    | |___     | 
   |                                                         | 
   |                   _______   __                          |
   |                      |     |  |                         |
   |                      |     |  |                         |
   |                      |     |__|                         | 
   |                                                         |
   |      ____               __                  __          |
   |     |____| |   |  /\   |__| |\  /|   /\    |   \   /    |
   |     |      |---| /--\  |\   | \/ |  /--\   |    \ /     |              
   |     |      |   |/    \ | \  |    | /    \  |__   |      |
   |                                                         |
    =========================================================   
  /                                                           \  
        
                                                             ''')
XYZ=input(" ----------PRESS ENTER TO CONTINUE---------------")

print()

print()

WELCOME=input("Enter L for login or S for signup or Q for quit:")

if WELCOME== "L" or WELCOME== "l":
    login(mydb,cart)


elif WELCOME== "S" or WELCOME=="s":
    choice=int(input('Enter 1 to signup as STAFF and Enter 2 to signup as ADMIN '))

    if choice == 1:
        signup_staff(mydb,cart)
        login(mydb,cart)
    else:
        signup_admin(mydb,cart)
        login(mydb,cart)

else:
    print("byeeeeeeeeeeeeeee   :)")
    
    
    
x=input("HAVE A GREAT DAY AHEAD!!!!! :)")


x=input('Exit')

    



