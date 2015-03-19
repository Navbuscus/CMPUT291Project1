CMPUT 291 Introduction to File and Database Management

Winter 2015
Mini-Project 1
Due time:  18:00 on  March 27, 2015.
Clarifications and notifications:

    No clarification so far.

Introduction
=======

In this project, you are going to design and implement a database application system for an auto registration system, based on your previous work in the first two assignments.

This is a simple client-server application in which the data will be stored in the Oracle Server in the lab, and all the application programs shall be developed using (1) Java and JDBC, or (2) Python.  (You may develop your application programs using C and ODBC or Embedded C, or any other technologies  if you really dislike Java and Python, but do not expect any help from the lab.)  You are free to implement a GUI interface or a web-based three-tier system instead, but there will be neither support nor bonus for doing that.

This is a group project, with two or three students in each group, and of course, all students in a group will receive the same mark for the project. Send an email to  TA  Kriti Khare with the list of students in your group before March 10. (Our on-line group registration program apparently not working properly).

Database Specification

Consider an auto registration system, as outlined in Assignment 1,  with the following tables:

    people( sin, name, height,weight,eyecolor, haircolor,addr,gender,birthday )
    drive_licence( licence_no,sin,class,photo,issuing_date,expiring_date)
    driving_condition( c_id, description )
    restriction( licence_no, r_id )
    vehicle_type( type_id, type )
    vehicle( serial_no, maker, model, year, color, type_id )
    owner(owner_id, vehicle_id, is_primary_owner)
    auto_sale( transaction_id,seller_id, buyer_id, vehicle_id, s_date, price )
    ticket_type( vtype, fine )
    ticket( ticket_no, violator_no,vehicle_no,office_no,vtype,vdate,place,descriptions )

Note that this is the same as one given in Assignment 2.

Use the provided SQL statements to create the database and then populate the initial database using your own data set. Do not make any change to the schema as it will be used to test your project.

Application Programs

The system consists of the following five (5) application programs.

New Vehicle Registration

This component is used to register a new vehicle by an auto registration officer. By a new vehicle, we mean a vehicle that has not been registered in the database. The component shall allow an officer to enter the detailed information about the vehicle and personal information about its new owners, if it is not in the database. You may assume that all the information about vehicle types has been loaded in the initial database.

Auto Transaction

This component is used to complete an auto transaction. Your program shall allow the officer to enter all necessary information to complete this task, including, but not limiting to, the details about the seller, the buyer, the date, and the price. The component shall also remove the relevant information of the previous ownership.

Driver Licence Registration

This component is used to record the information needed to issuing a drive licence, including the personal information and a picture for the driver. You may assume that all the image files are stored in a local disk system.

Violation Record

This component is used by a police officer to issue a traffic ticket and record the violation. You may assume that all the information about ticket_type has been loaded in the initial database.

Search Engine

This component is used to perform the following searches.

1. List the name, licence_no, addr, birthday, driving class, driving_condition, and the expiring_data of a driver by entering either a licence_no or a given name. It shall display all the entries if a duplicate name is given.
   
2. List all violation records received by a person if  the drive licence_no or sin of a person  is entered.

3. Print out the vehicle_history, including the number of times that a vehicle has been changed hand, the average price, and the number of violations it has been involved by entering the vehicle's serial number.

Requirements

1. Your system must start with a main menu for a user to use any of the five application programs, and the system terminates only if the user explicitly choose to do so.

2. Your programs shall display proper information to guide users to perform their work and correct any mistake.

3. You are required to submit a typed design report. The design report should include a brief description of the overall design of your application system. The description should focus mostly on the classes required to deliver the major functions of your application, not on secondary or utility classes. You shall clearly describe the responsibility and interface of each class and relationships among them. As an example, you may take a look at the document for the Berkeley DB.

4. You are required to demonstrate your application system in the lab against the database populated with our own test data in a TA account. The demo will be run using the source code submitted and nothing else. Make sure your submission includes every file that is needed. The code will be executed under a TA account. Do not hard-code username, password or table prefixes (such as username or group name) in your code. If you cannot set up your application within 3 minutes under a TA account, the TA will be moving to the next demo. At demo time, all group members must be present. The TA will be using a script to create and populate the initial database. You will be then asked to perform various tasks and show how your application is handling each task. A mark will be assigned to your demo on the spot after the testing.

Notes

1. Please use case insensitive comparison in your SQL, Python, or Java programs. For SQL statements, one may use "LOWER" or "UPPER" functions to archive case insensitive comparison.

2. This is a  sample Java program  ( a sample Python program )  for inserting a local file into a table as a Blob/LONG RAW.

3. A list of all possible test scenarios will be posted hear one week before the due date.

Instructions for Submissions

You must submit (1) the design report, and (2) the source code of your application programs and related files.

1. Submit your design report in hard copy, at the designated drop box for CMPUT291 located on the first floor of CSC building, across from Room 1-43. There is no guarantee to get your report marked and/or returned to you if it is dropped in a wrong box!

2. Create a single gzipped tar file with all your source code and additional files you may need for your demo using
                     tar -c file1, file2, ..., fileN | gzip -c > project.tgz; 

3. Submit project.tgz at the bottom of this page.
