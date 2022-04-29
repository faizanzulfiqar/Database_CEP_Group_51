create schema hospitalmng; 
use hospitalmng; 
create table patient( 
					patient_id numeric(5) primary key,
                    F_name varchar(20),
                    L_name varchar(20),
                    gender char(1),
                    address varchar(30)
                    );
                    
create table staff( 
					staff_id numeric(10) primary key,
					fname varchar(20),
                    lname varchar(20),
                    gender varchar(2),
                    phone_no numeric(20),
                    address varchar(30) 
                    ); 
                    
                    
create table diagnosis( 
					diagnosis_id varchar(10) primary key,
                    patient_id numeric(5)
                    ); 


create table medicine( 
					date_end datetime ,
                    date_start datetime,
                    price numeric,
                    quantity numeric,
                    medicine_id numeric(20) primary key
                    ); 
                    
create table given( 
					medicine_id numeric(20),
                    patient_id numeric(5)
                    ); 
                    
                    
create table Bill( 
					bill_id numeric primary key,
                    patient_id numeric(5),
                    doctor_charges numeric,
                    room_charges numeric,
                    medicine_charges numeric
                    ); 
                    

                    
create table doctor( 
					doctor_id numeric(5) primary key,
                    field varchar(20)
                    ); 
				
                    
create table nurse( 
					nurse_id numeric(5) primary key
                    ); 
                    
                    
create table room( 
					room_id varchar(10) primary key,
                    r_type varchar(20),
                    patient_id numeric(5),
                    nurse_id numeric(5)
                    ); 
                    
                    
create table treatment( 
                    patient_id numeric(5),
                    doctor_id numeric(5)
                    ); 
                    
                    
create table records( 
					date_admission datetime,
                    date_discharge datetime,
                    record_id varchar(20) primary key,
                    treatment varchar(30),
                    future_date datetime,
                    patient_id numeric(5),
                    doctor_id numeric(5)
                    ); 