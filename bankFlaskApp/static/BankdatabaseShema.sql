create table User(

    NationalId int not null primary key,
    Name varchar(40) not null,
    Surname varchar(40) not null

);

create table UserBankInfo(
	
  NationalId int not null references User(NationalId),
  BankName varchar(40) not null,
  AccountNumber int not null,
  AccountBalance float not null
	
);

create table Transfer(
	
  NationalId int not null references User(NationalId),
  BankName varchar(40) not null references User(BankName),
  ReceverName varchar(40) not null,
  Amount float not null,
  Fee float not null

);
