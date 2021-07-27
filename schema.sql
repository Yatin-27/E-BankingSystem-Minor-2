DROP TABLE IF EXISTS SavingAccount;
DROP TABLE IF EXISTS loanAccount;
DROP TABLE IF EXISTS customerdetails_retail;
DROP TABLE IF EXISTS branch;

CREATE TABLE branch(address VARCHAR(1024), bank VARCHAR(200), ifsc VARCHAR(100) PRIMARY KEY);
CREATE TABLE customerdetails_retail(customerID VARCHAR(200) PRIMARY KEY, name VARCHAR(100) NOT NULL, FatherName VARCHAR(100) NOT NULL, MotherName VARCHAR(100) NOT NULL, dob DATETIME NOT NULL, address VARCHAR(200) NOT NULL, Aadhar BIGINT NOT NULL, PANNumber VARCHAR(200) NOT NULL, branch VARCHAR(100), FOREIGN KEY(branch) REFERENCES branch(ifsc));
CREATE TABLE SavingAccount(customerID VARCHAR(200) PRIMARY KEY, AccountNumber INT, Balance INT, FOREIGN KEY(customerID) REFERENCES customerdetails_retail(customerID));
CREATE TABLE loanAccount(customerID VARCHAR(200) PRIMARY KEY, AccountNumber INT, balance INT, FOREIGN KEY(customerID) REFERENCES customerdetails_retail(customerID));
