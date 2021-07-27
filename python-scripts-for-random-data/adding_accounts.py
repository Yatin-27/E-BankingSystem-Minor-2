import random
import sqlite3
from sqlite3 import Error

def getBalance():
    balance = random.randint(1000, 99999999)
    return balance

def AccountNumber(typeOfAccount):
    initial = random.randint(10000000,99999999)

    temp = initial
    s = 0
    count = 0
    while(temp>=1):
        if count%2 == 0:
            factor = 1
        else:
            factor = 2

        s = s + factor*(temp%10)
        temp = int(temp/10)
        count = count+1
    s = 9*s
    s = s%10
    if typeOfAccount == 'L':
        pre1 = 1000
    elif typeOfAccount == 'S':
        pre1 = 1100
    else:
        pre1 = 1010

    ac_number = str(pre1)+ str(initial)+ str(s)
    return ac_number

def getCustID():
    ID_list = ["F472540070H4", "F501241899U3", "F502348600H5", "F54874H113F10", "F55914H113F6", "F568442675R9", "F598348600R11", "F603841182Y3", "F72634DDEHT4", "F777244616Q9", "F783740643T11", "F80574DDEHH6", "F805841182I7", "F845641182G9", "F852344616R4", "F854648600H9", "F883840643V4", "F895645411B5", "F913741182M6", "F984440075G11", "F98774DDEHD8", "G125841899F2", "G155044616Y6", "G199240164V7", "G20544DDEHA6", "G26264DDEHO2", "G281340225M9", "G348840164A9", "G368048600U3", "G381742675P5", "G400040225A8", "G408641899X4", "G421948600U2", "G442640643D2", "G459940075J4", "G464445411P4", "G473142675M10", "G50954H113P5", "G531840075T3", "G567748600G11", "G655040225Y2", "G740440070E10", "G759640075W4", "G822641899H4", "G84754H113F10", "G852740075T8", "G860841182O8", "G89424DDEHO9", "G908648600X9", "G925541899O7", "G965740075U4", "G97224H113A6", "H108948600A4", "H120540643M3", "H134940075E3", "H140545411T5", "H23034DDEHT3", "H243740070N2", "H262640643Y2", "H287040070G3", "H301540070D4", "H32874DDEHB6", "H330741899Z8", "H360641182O10", "H378640164E10", "H395348600G6", "H414540164A9", "H416341182L9", "H41824H113K10", "H435741182A5", "H439942675X11", "H50714DDEHM8", "H598740070D6", "H609741182H8", "H680340075E3", "H683040075W3", "H692840225Z11", "H75954H113I3", "H759948600C7", "H786045411O7", "H79434H113E9", "H79994DDEHI11", "H801641182D10", "H843648600W7", "H845440225A7", "H855040075X4", "H856042675P5", "H866340225B9", "H877741899Z6", "H916341182J5", "H934040225K2", "H987140164Y11", "I107445411R7", "I131542675A5", "I133040075R2", "I137740164O4", "I147045411M7", "I175045411F8", "I180540075Q9", "I21464DDEHF8", "I217140164Y6", "I22574DDEHX2", "I246540164I3", "I256741899E6", "I347448600M4", "I373241899S10", "I428840070O8", "I444540164C3", "I481644616I5", "I503542675L8", "I513345411P7", "I520240643Q4", "I57744DDEHQ9", "I580242675T10", "I600541899I6", "I624041899E7", "I648740075N11", "I675840075Z3", "I68324DDEHO5", "I683942675F3", "I693245411V6", "I708144616W2", "I747941899M4", "I749041899C6", "I846241182P6", "I897342675I4", "I919441182W9", "I980040643U3", "J115740070J9", "J12184H113H7", "J141045411Y1", "J15894DDEHA9", "J162244616H6", "J183740070T5", "J212445411N4", "J220240070L1", "J224444616X7", "J235640225S2", "J262440225D9", "J26784H113S9", "J274041899U8", "J282544616U3", "J32834H113J2", "J329541899Z5", "J335041899I6", "J363548600V3", "J367840070Y10", "J371841182Z5", "J471941899L7", "J496540070L10", "J526844616H7", "J534942675P7", "J557441182P7", "J598540075O4", "J61034H113N5"]
    custID = random.sample(ID_list, k=1)
    return custID

x = input("Number of Records to Generate: ")
if len(x) == 0:
	x = 1
x = int(x)
while(1):
    try:
        conn = sqlite3.connect('bankDB.sqlite')
        for i in range(0, x):
            t_list = ["L", "S"]  # L = Loan Account and S = Savings Account
            t = random.choices(t_list)
            #print(t)
            ac_number = AccountNumber(t[0])
            custID = getCustID()
            bal = getBalance()
            #custID[0] = custID[0].strip()
            #print("INSERT INTO loanAccount(customerID, AccountNumber, balance) VALUES (\""+custID[0]+ "\",\""+str(ac_number)+ "\",\""+str(bal)+ "\");", )
            if t[0] == "L":
                conn.execute("INSERT INTO loanAccount(customerID, AccountNumber, balance) VALUES (?, ?, ?);", (custID[0], ac_number, bal))
                conn.commit()
            elif t[0] == "S":
                conn.execute("INSERT INTO SavingAccount(customerID, AccountNumber, balance) VALUES (?, ?, ?);", (custID[0], ac_number, bal))
                conn.commit()
            else:
                continue;
        break;
    except Error as e:
        #print(e)
        print("", end = "")
    finally:
        conn.close()
