import sqlite3
import random
import time
import datetime

def generateName():
	#Name from a list
	names = ["Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David", "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William", "Jonathan", "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam", "Megan", "Melissa", "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura", "Lauren", "Amber", "Brittany", "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy", "Crystal", "Michelle", "Tiffany", "Jeremy", "Benjamin", "Mark", "Emily", "Aaron", "Charles", "Rebecca", "Jacob", "Stephen", "Patrick", "Sean", "Erin", "Zachary", "Jamie", "Kelly", "Samantha", "Nathan", "Sara", "Dustin", "Paul", "Angela", "Tyler", "Scott", "Katherine", "Andrea", "Gregory", "Erica", "Mary", "Travis", "Lisa", "Kenneth", "Bryan", "Lindsey", "Kristen", "Jose", "Alexander", "Jesse", "Katie", "Lindsay", "Shannon", "Vanessa", "Courtney", "Christine", "Alicia", "Cody", "Allison", "Bradley", "Samuel", "Shawn", "April", "Derek", "Kathryn", "Kristin", "Chad", "Jenna", "Tara", "Maria", "Krystal", "Jared", "Anna", "Edward", "Julie", "Peter", "Holly", "Marcus", "Kristina", "Natalie", "Jordan", "Victoria", "Jacqueline", "Corey", "Keith", "Monica"]

	n = random.choices(names, k =2)
	return n
def addDigits(num1, num2):
	s=0
	while(num1>=1):
		s = s + (num1%10)
		num1 = int(num1/10)
	while(num2>=1):
		s = s + (num2%10)
		num2 = int(num2/10)
	if s > 9:
		sum=0
		while(s>=1):
			sum = sum + s%10
			s = int(s/10)
	else:
		sum = s
	return sum
def generateCustomerID(branch, DOB, name):
	#random string of letters and numbers of length 12
	alphabet_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	r_num = random.randint(1000,9999)
	l_name=len(name)
	if l_name < 10:
		l_name = 2*l_name
	s = addDigits(l_name, r_num)
	l_name = str(l_name)
	#sum_date = str(sum_date)
	b=branch[7:11]
	b = str(b)
	r_num=str(r_num)
	r_alphabet1 = random.choices(alphabet_list)
	r_alphabet2 = random.choices(alphabet_list)
	r_alphabet1 =str(r_alphabet1[0])
	r_alphabet2 = str(r_alphabet2[0])
	s = str(s)
	custID = r_alphabet1 + r_num + l_name + b + r_alphabet2 + s
	#adding sum of all the digits on line 19 and 25 and 31
	return custID
def generateDOB():
	#random date from 1 Jan 1960 to 31 Dec 2005
	start_date = datetime.date(1960, 1, 1)
	end_date = datetime.date(2005, 12, 31)
	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	d = start_date + datetime.timedelta(days=random_number_of_days)
	return d;

def generateAadhar():
	#random number of 12 digit
	a = random.randint(100000000000,999999999999)
	a = str(a)
	return a
def generatePAN():
	#randam string of letters and numbers of length 10
	alphabet_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	alphabet5 = list()
	for i in range(0, 5):
		alphabet5.append(random.choices(alphabet_list))
	pan  = alphabet5[0][0] +alphabet5[1][0] +alphabet5[2][0] +alphabet5[3][0] +alphabet5[4][0] + str(random.randint(1000,9999)) + random.choices(alphabet_list)[0]
	return pan
def getBranch():
	branches = ["UCBA0000075", "SBIN0015411", "IBKL0000070", "HDFC0000225", "BKDN0761899", "CORP0000643", "UTIB0002675","PUNB0408600", "BARB0INDDEH", "ICIC0000164", "CNRB0001182", "NTBL0DEH113", "JSFB0004616"]
	return random.choices(branches)

def generateAddress():
	add_list = ["Vasai Taluk Indl Estate, Goraipada,besin, Mumbai, Maharashtra", "44-a, S L N Bld, 44-a,slnbld,klsiplyblr-2, Kalasipalyam, Bangalore, Karnataka", "Nehru Road, Santacruz(e), Mumbai, Maharashtra", "4 st Floor, Mayur Vihar, Shastradhara Road, Dehradun, Uttrakhand", "345 , Ambika Vihar, Delhi, Delhi"]
	return random.choices(add_list)[0]


x = input("Number of Records to Generate: ")
if len(x) == 0:
	x = 1
x = int(x)
conn = sqlite3.connect('bankDB.sqlite')

for i in range(0, x):
	name = generateName()
	n = name[0] + " " +name[1]
	b = getBranch()[0]
	dob = generateDOB()
	dob = str(dob)
	custID = generateCustomerID(b, dob, name)
	Father = generateName()
	Mother = generateName()
	f = Father[0]+" "+Father[1]
	m = Mother[0]+" "+Mother[1]
	pan = generatePAN()
	a = generateAadhar()
	address = generateAddress()
	#print(custID, n, f, m, dob, address, a, pan, b)
	#print("INSERT INTO customerdetails_retail(customerID, name, FatherName, MotherName, dob, address, Aadhar, PANNumber, branch) VALUES (\"" + custID+ "\", \""+ n+ "\", \""+ f+ "\", \""+ m + "\", \""+  dob+ "\", \""+ address  +"\", \""+  a +"\", \""+ pan+ "\", \""+ b +"\");")
	conn.execute("INSERT INTO customerdetails_retail(customerID, name, FatherName, MotherName, dob, address, Aadhar, PANNumber, branch) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (custID, n, f, m, dob, address, a, pan, b))
conn.commit()
conn.close()
