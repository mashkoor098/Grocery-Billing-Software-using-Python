import random
from tkinter import *
from tkinter import messagebox
import random,datetime,pytz,os,tempfile

# Functionality
global DictOfGrocery
global DictOfColdrinks
global DictOfCosmatics

def send_mail():
    pass

def print_billl():
    if TextArea.get(1.0,END) == '\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file,'w',encoding='utf-8').write(TextArea.get(1.0,END).replace('|','').replace('-','').replace('\t\t\t\t\t\t\t','\t\t'))
        os.startfile(file,'print')

def serch_bill():
    bill = 'bills\\'
           #not working, contains error
    # bill = f"D:\\Languages\\Data Science course\\Python\\TK\\bills\\"
    for i in os.listdir(f'{bill}'):
        if i.split('.')[0] == Bill_numberEntry.get():
            f= open(f'{bill}\{i}','r')
            TextArea.delete(1.0,END)
            for data in f:
                # print(data)
                TextArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill No.' )
if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    result = messagebox.askyesno('Confirm','Do you want to save bill')
    if result:
        bill_content = TextArea.get(1.0,END)
        file = open(f'bills/{Bill_numberEntry.get()}.txt','w',encoding='utf-8')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill No. {Bill_numberEntry.get()} is saved successfully')


def bill():
    if nameEntry.get() == "":
        messagebox.showinfo("Error", "Error: Name and Mobile Number are Required")
    elif (phoneEntry.get()).isdigit() == False or len(phoneEntry.get()) != 10:
        messagebox.showinfo("Error", "Error: Name and Mobile Number are Required")

    else:
        TextArea.delete("1.0",END)
        TextArea.insert(1.0," *************************  Sarkar Kirana  **************************\n")
        TextArea.insert(2.0,"Addr : Sarkar Kirana, Raza tawar, Bhusawal                                              Phone : 8080560080")
        TextArea.insert(3.0,"\n----------------------------------------------------------------------------------------------------")
        TextArea.insert(4.0,f"\nCust Name : {nameEntry.get().upper()}\t\t\t\t\t\t\t Bill No.: {Bill_numberEntry.get()}")
        local_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.datetime.now(local_timezone)
        TextArea.insert(5.0,f"\nMobile : {phoneEntry.get()}\t\t\t\t\t\t\t Date : {current_time.strftime('%d,%m,%y')}")
        TextArea.insert(6.0,f"\nUser : Shoeb\t\t\t\t\t\t\t Time : {current_time.strftime('%H:%M:%S')}")
        TextArea.insert(7.0,"\n----------------------------------------------------------------------------------------------------")
        TextArea.insert(8.0,f"\nProduct Name\t\t\t|\tQTY\t\t|\t MRP \n\n")
        count = 11.0
        global quantity
        quantity= 0
        # global DictOfCosmatics # dictionary is present in bellow code
        for key1, data in DictOfCosmatics.items():
            if key1.get().isdigit() ==False:
                messagebox.showinfo("Error", " Enter valid number in Product")
            elif int(key1.get()) > 0 and key1.get() != "":
                quantity+=int(key1.get())
                for key2 in data:
                    TextArea.insert(count,f"{key2}\t\t\t|\t  {key1.get()}\t\t|\t   {int(key1.get())* data[key2]}\n")
                count+=1
        # global DictOfGrocery # dictionary is present in bellow code
        for key1, data in DictOfGrocery.items():
            if key1.get().isdigit() ==False:
                messagebox.showinfo("Error", " Enter valid number in Product")
            elif int(key1.get()) > 0 and key1.get()!="":
                quantity+=int(key1.get())
                for key2 in data:
                    TextArea.insert(count,f"{key2}\t\t\t|\t  {key1.get()}\t\t|\t   {int(key1.get())* data[key2]}\n")
                count+=1

        # global DictOfColdrinks # dictionary is present in bellow code
        for key1, data in DictOfColdrinks.items():
            if key1.get().isdigit() ==False:
                messagebox.showinfo("Error", " Enter valid number in Product")
            elif int(key1.get()) > 0 and key1.get()!="":
                # print('checking: ',quantity,'bef, cold')
                quantity+=int(key1.get())
                # print('checking: ',quantity,'aft, cold',key1.get())
                for key2 in data:
                    TextArea.insert(count,f"{key2}\t\t\t|\t  {key1.get()}\t\t|\t   {int(key1.get())* data[key2]}\n")
                count+=1

        TextArea.insert(count,f"==================================================================\n")
        TextArea.insert(count+1,f"Total Price :\t\t\t|\t  {quantity}\t\t|\t   {float(CosmeticPriceEntry.get())+float(GroceryPriceEntry.get())+float(ColdDrinksPriceEntry.get()):.2f}\n")
        TextArea.insert(count+2,f"Cosmetic Tax:\t\t{CosmeticTaxEntry.get()}\n")
        TextArea.insert(count+3,f"Grocery Tax:\t\t{GroceryTaxEntry.get()}\n")
        TextArea.insert(count+4,f"ColdDrinks Tax:\t\t{ColdDrinksTaxEntry.get()}\n")
        TextArea.insert(count+5,f"\nTotal Price + GST = \t\t  {float(CosmeticPriceEntry.get())+float(CosmeticTaxEntry.get())+float(GroceryPriceEntry.get())+float(GroceryTaxEntry.get())+float(ColdDrinksPriceEntry.get())+float(ColdDrinksTaxEntry.get()):.2f}\n")
        TextArea.insert(count+6,f"\n ********{nameEntry.get().upper()} Ji Saman Leke Wapis Nahi Aana  ********\n\n")
        save_bill()

def total():
    for dictionary in [DictOfCosmatics,DictOfGrocery,DictOfColdrinks]:
        for key, value in dictionary.items():
            for product in value:
                if not key.get().isdigit():
                    messagebox.showinfo("Error", f" Enter valid number in {product}")

    if nameEntry.get() == "" or phoneEntry.get() == "" or phoneEntry.get().isdigit() == False or len(phoneEntry.get()) != 10:
        messagebox.showinfo("Error", "Error: Name and Mobile Number are Required")
    else:
        TextArea.delete("1.0",END)
        Bill_numberEntry.delete(0,END)
        rn = ""
        while len(rn) <5:
            rn +=str(random.randint(0,10))
        Bill_numberEntry.insert('0',rn)

         # Cosmatics Calculations
        BathSoap_tot = int(BathSoapLableEntry.get()) * 40
        FaceCream_tot = int(FaceCreamLableEntry.get())*30
        HairGell_tot = int(HairGellEntry.get())*10
        HairSpray_tot = int(HairSprayEntry.get())*110
        BodyLotion_tot = int(BodyLotionEntry.get())*35
        FaceWash_tot = int(FaceWashEntry.get())*75
        TotalCosmatics = BathSoap_tot + FaceCream_tot+HairGell_tot+HairSpray_tot+BodyLotion_tot+FaceWash_tot
        # print(TotalCosmatics)
        CosmeticPriceEntry.delete(0,END)
        CosmeticPriceEntry.insert(0,f"{TotalCosmatics:.2f}")
        # Tax
        CosTax = TotalCosmatics*0.18
        # print(CosTax) # prints float val.
        CosmeticTaxEntry.delete(0,END)
        CosmeticTaxEntry.insert(0,f"{CosTax:.2f}") # prints 2 value after dot(.) by rounding

        #  Grocery Calculations
        MoongDaalLableEntry_tot = int(MoongDaalLableEntry.get()) * 40
        MatDaalEntry_tot = int(MatDaalEntry.get()) * 40
        SoyaOilLableEntry_tot = int(SoyaOilLableEntry.get()) * 40
        WheatLableEntry_tot = int(WheatLableEntry.get()) * 40
        DalLableEntry_tot = int(RiceLableEntry.get()) * 40
        RiceLableEntry_tot = int(RiceLableEntry.get()) * 40

        Total_coldrings = RiceLableEntry_tot+DalLableEntry_tot+SoyaOilLableEntry_tot+MatDaalEntry_tot+WheatLableEntry_tot+MoongDaalLableEntry_tot
        GroceryPriceEntry.delete(0,END)
        GroceryTaxEntry.delete(0,END)
        GroceryPriceEntry.insert(0, f"{Total_coldrings:.2f}")
        ColTax = Total_coldrings *.18
        GroceryTaxEntry.insert(0,f"{ColTax:.2f}")

        # Colderinks Calculations
        CocacolaEntry_tot = int(CocacolaEntry.get()) * 40
        WaterEntry_tot = int(WaterEntry.get()) * 40
        StingEntry_tot = int(StingEntry.get()) * 40
        PepsiEntry_tot = int(PepsiEntry.get()) * 40
        SpriteEntry_tot = int(SpriteEntry.get()) * 40
        MaazaEntry_tot = int(MaazaEntry.get()) * 40

        Total_coldrings = CocacolaEntry_tot+WaterEntry_tot+PepsiEntry_tot+StingEntry_tot+SpriteEntry_tot+MaazaEntry_tot
        ColdDrinksPriceEntry.delete(0,END)
        ColdDrinksTaxEntry.delete(0,END)
        ColdDrinksPriceEntry.insert(0, f"{Total_coldrings:.2f}")
        ColTax = Total_coldrings *.18
        ColdDrinksTaxEntry.insert(0,f"{ColTax:.2f}") # prints 2 value after dot(.) by rounding

def clear():
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    Bill_numberEntry.delete(0,END)

    listOfColdrinks = [CocacolaEntry,WaterEntry,StingEntry,PepsiEntry,SpriteEntry,MaazaEntry]
    for item in listOfColdrinks:
        item.delete(0,END)
        item.insert(0,0)

    listOfGrocery = [MoongDaalLableEntry, MatDaalEntry, SoyaOilLableEntry, WheatLableEntry, TuwarDalLableEntry, RiceLableEntry]
    for item in listOfGrocery:
        item.delete(0,END)
        item.insert(0,0)

    listOfCosmatics = [BathSoapLableEntry,FaceCreamLableEntry,HairSprayEntry,HairGellEntry,BodyLotionEntry,FaceWashEntry]
    for item in listOfCosmatics:
        item.delete(0,END)
        item.insert(0,0)
    TextArea.delete("1.0",END)

    # total clearing
    CosmeticPriceEntry.delete(0,END)
    GroceryPriceEntry.delete(0,END)
    ColdDrinksPriceEntry.delete(0,END)
    CosmeticTaxEntry.delete(0,END)
    GroceryTaxEntry.delete(0,END)
    ColdDrinksTaxEntry.delete(0,END)

# GUI
main_window = Tk()
main_window.title("Billing Software")
main_window.geometry("1550x850")
main_window.iconbitmap("D:\Languages\Data Science course\Python\TK\ico.ico")

shop_name = Label(main_window,text = "Sarkar Kirana", font=("times new roman",36,"bold"),fg="blue4",bg="palegreen1",  bd=12, relief=GROOVE)
shop_name.pack(fill=X)

customer_detals = LabelFrame(main_window, text="Customer's Details",font=('times new roman',15 , 'bold'),fg="blue4",bg="palegreen1",bd=12, relief=GROOVE)
customer_detals.pack(fill=X,pady=10)

nameLable = Label(customer_detals, text="Name",font=('times new roman',15 , 'bold'),bg="palegreen1")
nameLable.grid(row=0, column=0,padx=20)
nameEntry = Entry(customer_detals,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLable = Label(customer_detals, text="Phone Number",font=('times new roman',15 , 'bold'),bg="palegreen1")
phoneLable.grid(row=0, column=2,padx=20)
phoneEntry = Entry(customer_detals,font=('rial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

Bill_numberLable = Label(customer_detals, text="Bill Number",font=('times new roman',15 , 'bold'),bg="palegreen1")
Bill_numberLable.grid(row=0, column=4,padx=20)
Bill_numberEntry = Entry(customer_detals,font=('arial',15),bd=7,width=18)
Bill_numberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_detals,text="Search",font=('arial',16,'bold'),bd=7,width=15,pady=5,command=serch_bill)
searchButton.grid(row=0,column=6,pady=10,padx=50)

productsFrame = Frame(main_window)
productsFrame.pack()

maincosmaticsFrame = Frame(productsFrame)
maincosmaticsFrame.grid(row=0,column=0)

# Frame1
cosmaticsFrame = LabelFrame(maincosmaticsFrame,text="Cosmatics",font=('times new roman',15 ,'bold'),fg="blue4",bg="palegreen1",bd=12,relief=GROOVE,pady=18)
cosmaticsFrame.grid(row=0,column=0)
# Items
BathSoapLable = Label(cosmaticsFrame, text="Bath Soap", font=('times new roman', 15 , 'bold'), bg="palegreen1")
BathSoapLable.grid(row=0, column=0, padx=8, sticky='w')

BathSoapLableEntry = Entry(cosmaticsFrame, font=('arial', 15), bd=7, width=10)
BathSoapLableEntry.grid(row=0, column=1, padx=8)
BathSoapLableEntry.insert(0, 0) # Ye hai Aaam zindagi

FaceCreampLable = Label(cosmaticsFrame,text="Face Cream",font=('times new roman',15 , 'bold'),bg="palegreen1")
FaceCreampLable.grid(row=1,column=0,padx=8,sticky='w')

FaceCreamLableEntry = Entry(cosmaticsFrame,font=('arial',15),bd=7,width=10)
FaceCreamLableEntry.grid(row=1, column=1,padx=8,pady=10)
FaceCreamLableEntry.insert(0,0)

HairGellLable = Label(cosmaticsFrame,text="Hair Gell",font=('times new roman',15 , 'bold'),bg="palegreen1")
HairGellLable.grid(row=2,column=0,padx=8,sticky='w')

HairGellEntry = Entry(cosmaticsFrame,font=('arial',15),bd=7,width=10)
HairGellEntry.grid(row=2, column=1,padx=8)
HairGellEntry.insert(0,0)

HairSprayLable = Label(cosmaticsFrame,text="Hair Spray",font=('times new roman',15 , 'bold'),bg="palegreen1")
HairSprayLable.grid(row=3,column=0,sticky='w',padx=8)

HairSprayEntry = Entry(cosmaticsFrame,font=('arial',15),bd=7,width=10)
HairSprayEntry.grid(row=3, column=1,pady=10)
HairSprayEntry.insert(0,0)

BodyLotionLable = Label(cosmaticsFrame,text="Body Lotion",font=('times new roman',15 , 'bold'),bg="palegreen1")
BodyLotionLable.grid(row=4,column=0,padx=8,sticky='w')

BodyLotionEntry = Entry(cosmaticsFrame,font=('arial',15),bd=7,width=10)
BodyLotionEntry.grid(row=4, column=1,padx=8)
BodyLotionEntry.insert(0,0)


FaceWashLable = Label(cosmaticsFrame,text="Face Wash",font=('times new roman',15 , 'bold'),bg="palegreen1")
FaceWashLable.grid(row=5,column=0,sticky='w',padx=8)

FaceWashEntry = Entry(cosmaticsFrame,font=('arial',15),bd=7,width=10)
FaceWashEntry.grid(row=5, column=1,pady=10)
FaceWashEntry.insert(0,0)

# globla dict defined. for further use
DictOfCosmatics = {BathSoapLableEntry:{'Bath Soap':15},FaceCreamLableEntry:{'Face Cream':34},HairSprayEntry:{'Hair Spray':76},HairGellEntry:{'Hair Gell':10},BodyLotionEntry:{'Body Lotion':53},FaceWashEntry:{'Face Wash':48}}

# Fram 2
GroceryFrame = LabelFrame(productsFrame,text="Grocery",font=('times new roman',15 , 'bold'),fg="blue4",bg="palegreen1",bd=12, relief=GROOVE,pady=18)
GroceryFrame.grid(row=0,column=1,padx=10)

RiceLable = Label(GroceryFrame,text="Rice",font=('times new roman',15 , 'bold'),bg="palegreen1")
RiceLable.grid(row=0,column=0,padx=20,sticky='w')

RiceLableEntry = Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
RiceLableEntry.grid(row=0, column=1,padx=8)


TuwarDalLable = Label(GroceryFrame, text="Daal", font=('times new roman', 15 , 'bold'), bg="palegreen1")
TuwarDalLable.grid(row=1, column=0, padx=20, sticky='w')

TuwarDalLableEntry = Entry(GroceryFrame, font=('arial', 15), bd=7, width=10)
TuwarDalLableEntry.grid(row=1, column=1, padx=8, pady=10)


WheatLable = Label(GroceryFrame,text="Wheat",font=('times new roman',15 , 'bold'),bg="palegreen1")
WheatLable.grid(row=2,column=0,padx=20,sticky='w')

WheatLableEntry = Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
WheatLableEntry.grid(row=2, column=1,padx=8)


SoyaOilLable = Label(GroceryFrame,text="Soya Oil",font=('times new roman',15 , 'bold'),bg="palegreen1")
SoyaOilLable.grid(row=3,column=0,padx=20,sticky='w' )

SoyaOilLableEntry = Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
SoyaOilLableEntry.grid(row=3, column=1,padx=8,pady=10)


MatDaalLable = Label(GroceryFrame,text="Mat Daal",font=('times new roman',15 , 'bold'),bg="palegreen1")
MatDaalLable.grid(row=4,column=0,padx=8,sticky='w')

MatDaalEntry = Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
MatDaalEntry.grid(row=4, column=1,padx=8)


MoongDaalLable = Label(GroceryFrame,text="Moong Daal",font=('times new roman',15 , 'bold'),bg="palegreen1")
MoongDaalLable.grid(row=5,column=0,sticky='w',padx=8)

MoongDaalLableEntry = Entry(GroceryFrame,font=('arial',15),bd=7,width=10)
MoongDaalLableEntry.grid(row=5, column=1,pady=10)

# globla dict defined. for further use
DictOfGrocery = {MoongDaalLableEntry: {'Moong Daal':110}, MatDaalEntry:{'Mat Daal':80}, SoyaOilLableEntry:{'Soya Oil':150},
                  WheatLableEntry:{'Wheat':32}, TuwarDalLableEntry:{'Tuwar Dal':90}, RiceLableEntry:{'Rice':19}}

# Ye hai Mentos zindagi
# LOOP FOR INSERTING 0 BEYDEFAULT
listOfgrocery = [MoongDaalLableEntry, MatDaalEntry, SoyaOilLableEntry, WheatLableEntry, TuwarDalLableEntry, RiceLableEntry]
for item in listOfgrocery:
    item.insert(0,0)
# Fram 3
ColdDrinksFrame = LabelFrame(productsFrame,text="ColdDrinks",font=('times new roman',15 , 'bold'),fg="blue4",bg="palegreen1",bd=12, relief=GROOVE,padx=6,pady=18)
ColdDrinksFrame.grid(row=0,column=2)

MaazaLable = Label(ColdDrinksFrame,text="Maaza",font=('times new roman',15 , 'bold'),bg="palegreen1")
MaazaLable.grid(row=0,column=0,padx=8,sticky='w')

MaazaEntry = Entry(ColdDrinksFrame,font=('arial',15),bd=7,width=10)
MaazaEntry.grid(row=0, column=1,padx=8)

SpriteLable = Label(ColdDrinksFrame,text="Sprite",font=('times new roman',15 , 'bold'),bg="palegreen1")
SpriteLable.grid(row=1,column=0,padx=8,sticky='w')

SpriteEntry = Entry(ColdDrinksFrame,font=('arial',15),bd=7,width=10)
SpriteEntry.grid(row=1, column=1,padx=8,pady=10)

PepsiLable = Label(ColdDrinksFrame,text="Pepsi",font=('times new roman',15 , 'bold'),bg="palegreen1")
PepsiLable.grid(row=2,column=0,padx=8,sticky='w')

PepsiEntry = Entry(ColdDrinksFrame,font=('arial',15),bd=7,width=10)
PepsiEntry.grid(row=2, column=1,padx=8)

StingLable = Label(ColdDrinksFrame,text="Sting",font=('times new roman',15 , 'bold'),bg="palegreen1")
StingLable.grid(row=3,column=0,padx=8,sticky='w' )

StingEntry = Entry(ColdDrinksFrame,font=('arial',15),bd=7,width=10)
StingEntry.grid(row=3, column=1,padx=8,pady=10)

WaterLable = Label(ColdDrinksFrame,text="Water",font=('times new roman',15 , 'bold'),bg="palegreen1")
WaterLable.grid(row=4,column=0,padx=8,sticky='w')

WaterEntry = Entry(ColdDrinksFrame,font=('arial',15),bd=7,width=10)
WaterEntry.grid(row=4, column=1,padx=8)

CocacolaLable = Label(ColdDrinksFrame,text="Cocacola",font=('times new roman',15 , 'bold'),bg="palegreen1")
CocacolaLable.grid(row=5,column=0,sticky='w',padx=8)

CocacolaEntry = Entry(ColdDrinksFrame,font=('arial',15),bd=7,width=10)
CocacolaEntry.grid(row=5, column=1,pady=10)

# globla dict defined. for further use
DictOfColdrinks = {CocacolaEntry:{'Cocacola':30},WaterEntry:{'Water':10},
                           StingEntry:{'Sting':15},PepsiEntry:{'Pepsi':20},SpriteEntry:{'Sprite':10},MaazaEntry:{'Maaza':50}}

# Ye hai Mentos zindagi
listOfColdrinks = [CocacolaEntry,WaterEntry,StingEntry,PepsiEntry,SpriteEntry,MaazaEntry]
for item in listOfColdrinks:
    item.insert(0,0)
# Fram 4
BillFrame = Frame(productsFrame,bd=8,relief=GROOVE)
BillFrame.grid(row=0,column=3,padx=10)

BillLable = Label(BillFrame,text="Bill Area",font=('times new roman',15 , 'bold'),bg="palegreen1",relief=GROOVE)
BillLable.pack(fill=X)

scroll_bar = Scrollbar(BillFrame)
scroll_bar.pack(side = RIGHT,fill = Y)

TextArea = Text(BillFrame,font=('times new roman',12 ),height=17,width=75,yscrollcommand = scroll_bar.set)
TextArea.pack()
# ==============================================================
# Calculation Fram
# ==============================================================
# BillMenueMain Frame
BillMenueFrame = LabelFrame(main_window, text="Bill Menue",font=('times new roman',15 , 'bold'),fg="blue4",bg="palegreen1",bd=12, relief=GROOVE)
BillMenueFrame.pack(fill=X,pady=10)
# Fram 1
PriceFrame = LabelFrame(BillMenueFrame,font=('times new roman',15 , 'bold'),fg="blue4",bg="palegreen1",bd=0)
PriceFrame.grid(row=0,column=0)

# 1st column
CosmeticPriceLable = Label(PriceFrame,text="Cosmetic Price",font=('times new roman',15 , 'bold'),bg="palegreen1")
CosmeticPriceLable.grid(row=0,column=0,sticky='w',padx=10)
CosmeticPriceEntry = Entry(PriceFrame,font=('arial',15),bd=7,width=10)
CosmeticPriceEntry.grid(row=0, column=1,padx=8)

GroceryPriceLable = Label(PriceFrame,text="Grocery Price",font=('times new roman',15 , 'bold'),bg="palegreen1")
GroceryPriceLable.grid(row=1,column=0,sticky='w',padx=10)
GroceryPriceEntry = Entry(PriceFrame,font=('arial',15),bd=7,width=10)
GroceryPriceEntry.grid(row=1, column=1,padx=8)

ColdDrinksPriceLable = Label(PriceFrame, text="Cold Drinks Price", font=('times new roman', 15 , 'bold'), bg="palegreen1")
ColdDrinksPriceLable.grid(row=2, column=0, sticky='w', padx=10)
ColdDrinksPriceEntry = Entry(PriceFrame,font=('arial',15),bd=7,width=10)
ColdDrinksPriceEntry.grid(row=2, column=1,padx=8)

# 2nd column
CosmeticTaxLable = Label(PriceFrame,text="Cosmetic Tax",font=('times new roman',15 , 'bold'),bg="palegreen1")
CosmeticTaxLable.grid(row=0,column=2,sticky='w',padx=30)
CosmeticTaxEntry = Entry(PriceFrame,font=('arial',15),bd=7,width=10)
CosmeticTaxEntry.grid(row=0, column=3,padx=8)

GroceryTaxLable = Label(PriceFrame,text="Grocery Tax",font=('times new roman',15 , 'bold'),bg="palegreen1")
GroceryTaxLable.grid(row=1,column=2,sticky='w',padx=30)
GroceryTaxEntry = Entry(PriceFrame,font=('arial',15),bd=7,width=10)
GroceryTaxEntry.grid(row=1, column=3,padx=8)

ColdDrinksTaxLable = Label(PriceFrame, text="Cold Drinks Price", font=('times new roman', 15 , 'bold'), bg="palegreen1")
ColdDrinksTaxLable.grid(row=2, column=2, sticky='w', padx=30)
ColdDrinksTaxEntry = Entry(PriceFrame,font=('arial',15),bd=7,width=10)
ColdDrinksTaxEntry.grid(row=2, column=3,padx=8)

# Fram 2
ButtonFrame = Frame(BillMenueFrame,relief=GROOVE,bd=8)
ButtonFrame.grid(row=0,column=1,rowspan=3,padx=50)

TotalButton = Button(ButtonFrame,text="Total",font=('arial',16,'bold'),bd=7,bg="blue4",fg="white",width=10 ,pady=8,command=total)
TotalButton.grid(row=0,column=0,pady=20,padx=9)

BillButton = Button(ButtonFrame,text="Bill",font=('arial',16,'bold'),bd=7,bg="blue4",fg="white",width=10 ,pady=8,command=bill)
BillButton.grid(row=0,column=1,pady=20,padx=5)

PrintButton = Button(ButtonFrame,text="Print",font=('arial',16,'bold'),bd=7,bg="blue4",fg="white",width=10 ,pady=8,command=print_billl)
PrintButton.grid(row=0,column=2,pady=20,padx=5)
#
# EmailButton = Button(ButtonFrame,text="Email",font=('arial',16,'bold'),bd=7,bg="blue4",fg="white",width=8 ,pady=8,command=send_mail)
# EmailButton.grid(row=0,column=3,pady=20,padx=5)

ClearButton = Button(ButtonFrame,text="Clear",font=('arial',16,'bold'),bd=7,bg="red",fg="white",width=10 ,pady=8,command=clear)
ClearButton.grid(row=0,column=4,pady=20,padx=9)

main_window.mainloop()
