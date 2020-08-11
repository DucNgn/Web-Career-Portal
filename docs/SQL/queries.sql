/* 1) Create/Delete/Edit/Display an Employer */

/*Create:*/
insert into user values('3120010', 'Mike', 'Leonard', 'Dr', 'mleonard@hotmail.com', 'mleonardpsw', 'Nobel Prize recipient', 'active', 'gold', '100', '514-830-2341', 'credit card', 'automatic', '1000', '112');

insert into creditCard values('3120010', '112', '4002 9042 6542 2354', 'Mike Leonard', '12 Road', '213', '01/23');

insert into employer values('3120010', 3, '5', '5140009');


/* Delete: */
delete from employer where ID='3120010';

delete from user where ID='3120010'


delete from creditCard where user_ID='3120010'

/*Edit:*/
update employer 
set ID='3120011', posting_count=5, postingLimit='unlimited', company_ID='5140008'
where ID='3120010';


/* Display: */
select *
from employer
where ID='3120011';

/* 2) Create/Delete/Edit/Display a category by an Employer */

/*Create:*/ 

insert into postJobs values('3120000', '4280019');

insert into jobs values('4280019', 'NeuroScience', '99 Alpine', '5140003', 0, 'Researcher', 'description19', 'active', 0, 0, 1, '2020-1-1');

/*Delete:*/

delete from postJobs where employer_ID='3120000' and job_ID='4280000';

delete from jobs where job_ID='4280000';

/*Edit:*/

update jobs
set fields='Health Science'
where fields='NeuroScience';


/*3) Post a new job by an employer*/

update employer 
set posting_count=4
where ID='3120011';

insert into postJobs values('3120011', '4280019');

insert into jobs values('4280019', 'Business', '901 Baker', '5140008', '0', 'Data Scientist', 'description19', 'active', 0, 0, 2, '2020-8-9');

/*4) Provide a job offer for an employee by an employer*/

update apply_to
set status='offering'
where jobSeeker_ID='1230007' and job_ID='4280001';

/*5) Report of a posted job by an employer (Job Title and description, date posted, list of employees applied to the job and status of each application)*/

select j.job_title, j.job_description, j.postedDate, a.jobSeeker_ID, a.status
from post_jobs p, Jobs j, applyTo a
where p.employer_ID='3120009' and p.job_ID='4280018' and p.job_ID=j.job_ID and j.job_ID=a.job_ID;

/*6) Report of posted jobs by an employer during a specific period of time (Job title, date posted, short description of the job up to 50 characters, number of needed employees to the post, number of applied jobs to the post, number of accepted offers).*/

select job_title, postedDate, job_description, vacancy, numOfApplication, numOfAccepted
from post_jobs p, jobs j, applyTo a
where p.employer_ID='3120000' and p.job_ID=j.job_ID and j.job_ID=a.job_ID and postedDate>'2020-1-1' and postedDate<'2020-2-1';


/*7) Create/Delete/Edit/Display an Employee*/
/*Create:*/
insert into user values('1230010', 'Karen', 'White', 'Ms', 'kwhite@yahoo.com', 'kwhitepsw', 'Let me talk to your manager', 'active', 'gold', '100', '514-023-1111', 'credit card', 'automatic', '100', '113');

insert into creditCard values('1230010', '113', '4002 3252 1111 9022', 'Karen White', '12 Towns', '900', '05/22');

insert into jobSeeker values('1230010', 'unlimited', 'resume10', 0);


/*Delete:*/
delete from jobSeeker where ID='1230010';

delete from user where ID='1230010'


delete from creditCard where user_ID='1230010'

/*Edit:*/
update jobSeeker 
set ID='1230011', applyLimit='unlimited', general_resume='resume11', apply_count=0
where ID='1230010';

/*Display:*/
select *
from jobSeeker
where ID='1230011';

/* 8) Search for a job by an employee
// If we are looking for the jobs an employee applied to 
*/
select *
from applyTo
where jobSeeker_ID='1230001' and job_ID='4280000';

/* If we are looking for a job an employee can apply to */
select *
from jobs;

/*9) Apply for a job by an employee*/

insert into applyTo values('1230001', '4280015', '2020-05-06', 'interviewing', 'interviewing', 'coverLetter1', 'resume1');


update jobs
set numOfApplication=2
where job_ID='4280015';

/*10) Accept/Deny a job offer by an employee*/

/*Accept: */
update applyTo
set status='accepted'
where job_ID='4280015' and jobSeeker_ID='1230001';

update jobs
set numOfAccepted=1
where job_ID='4280015' and jobSeeker_ID='1230001';

/*Deny: */
update applyTo
set status='rejected'
where job_ID='4280015' and jobSeeker_ID='1230001';

/* 11) Withdraw from an applied job by an employee */

update applyTo
set status='withdrawn'
where job_ID='4280015' and jobSeeker_ID='1230001';

/*12) Delete a profile by an employee*/
delete from jobSeeker where ID='1230010';

/*13) Report of applied jobs by an employee during a specific period of time (Job title, date applied, short description of the job up to 50 characters, status of the application) */

select j.job_title, j.appliedDate, j.job_description, a.status
from job j, applyTo a 
where a.jobSeeker_ID='1230001' and a.appliedDate>'2020-5-1' and a.appliedDate<'2020-8-1';

/*14) Add/Delete/Edit a method of payment by a user*/

/*Add (credit card):*/
insert into creditCard values('1230001', '112', '4002 1233 1231 1233', 'Greg Oden', '125 Oak', '459', '11/22');

/*Add (void): */
insert into void values('1230001', '212', '2131', '0930', '0921', '125 Oak', 'Greg Oden');

/*Delete (credit card):*/
delete from creditCard
where user_ID='1230001' and payment_ID='112';

/*Delete (void): */
delete from creditCard
where user_ID='1230001' and payment_ID='212';

/*Edit (credit card):*/
update creditCard
set user_ID='1230002', payment_ID='113', cardNum='4002 1111 2222 3333', cardName='Jack Frost', billingAddress='1 North Pole', PIN='111', expiredDate='12/25'
where user_ID='1230001' and payment_ID='112';

/*Edit (void): */
update creditCard
set user_ID='1230002', payment_ID='213', account='1212', institutionNum='1341', transit='1225', billingAddress='101 Chimney', name='Santa Clause'
where user_ID='1230001' and payment_ID='212';

/*15) Add/Delete/Edit an automatic payment by a user

//Not sure how add and edit are different. Assuming add means add a new user with automatic payment set up.
Add:
*/
insert into user values(‘1230010', ‘Jackson', ‘Martin', ‘Mr', ‘jmartin@yahoo.com', ‘jmartinpsw', ‘SoundCloud Rapper', ‘active', ‘prime', ‘10', ‘514-902-9332', ‘credit card', ‘automatic', ‘300', ‘113');

insert into creditCard values(‘1230010', ‘113', ‘4002 4334 3456 7665', ‘Jackson Martin', ‘54 Pine', ‘675', ‘11/23');

update user
set payment_option='automatic'
where ID='1230010';

/*Delete
//Assuming we want to delete the user as well 
*/
delete from user where ID='1230010' and payment_option='automatic';

delete from creditCard where user_ID='1230010' and payment_ID='113';


/*//Assuming we delete the previous payment option and setting it to null, causing the category to change to basic*/

update user
set payment_option=null, category='basic'
where ID='1230010';

/*Edit: */
update user
set payment_option='manual'
Where ID='1230010';


/*16) Make a manual payment by a user

//Assuming we have a jobSeeker with a prime account, making a manual payment of 10.
*/

update user
set balance=balance-10
where ID='1230010';


/*17) Report of all users by the administrator for employers or employees (Name, email, category, status, balance)*/

select firstName, lastName, category, account_status, balance
from user;

/*18) Report of all outstanding balance accounts (User name, email, balance, since when the account is suffering)
*/

select concat(firstName, ' ', lastName) as userName, login_email, balance
from user
where balance<0;


