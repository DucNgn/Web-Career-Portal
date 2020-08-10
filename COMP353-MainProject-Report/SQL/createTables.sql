create table user(
ID varchar(7), 
firstName varchar(20), 
lastName varchar(20), 
title varchar(50), 
login_email varchar(50), 
password varchar(20), 
about varchar(50),
account_status varchar(20),
category varchar(20),
monthly_charge decimal(6,2), 
contact_info varchar(50),
method_of_payment varchar(50),
payment_option varchar(20),
balance decimal(8,2),
payment_ID varchar(3)
);

create table creditCard(
user_ID varchar(7),
payment_ID varchar(3),
cardNum varchar(20),
cardName varchar(20),
billingAddress varchar(20),
PIN int(3),
expiredDate varchar(10)
);

create table void(
user_ID varchar(7),
payment_ID varchar(3),
account int(4), 
institutionNum int(4),
transit int(4),
billingAddress varchar(20), 
name varchar(20)
);

create table admin(
ID varchar(7), 
firstname varchar(20), 
lastName varchar(20),
login_email varchar(50),
password varchar(20)
);

create table employer(
ID varchar(7), 
posting_count int(3), 
postingLimit varchar(20),
company_ID varchar(7)
);

create table jobSeeker(
ID varchar(7), 
applyLimit varchar(20), 
general_resume varchar(100), 
apply_count int(3)
);

create table interests(
jobSeekerID varchar(7),
interests varchar(30)
);

create table company(
company_ID varchar(7), 
company_Name varchar(50)
);

create table jobs(
job_ID varchar(7),
fields varchar(50), 
address varchar(50), 
company_ID varchar(7),
view_count int(3),
job_title varchar(50),
job_description varchar(50), 
job_status varchar(30),
numOfApplication int(3),
numOfAccepted int(3),
vacancy int(3),
postedDate date
);


create table postJobs(
employer_ID varchar(7),
job_ID varchar(7)
);

create table applyTo(
jobSeeker_ID varchar(7),
job_ID varchar(7),
appliedDate date, 
status varchar(20),
coverLetter varchar(50),
resume varchar(50)
);

create table reviews(
jobSeeker_ID varchar(7),
company_ID varchar(7),
review varchar(100)
);
