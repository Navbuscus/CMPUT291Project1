/*
 *  Create/refreshes the database schema for Assignment 2
 *  CMPUT291, Winter Term, 2015.
 *  Author: Li-Yan Yuan
 *  University of Alberta
 */
DROP TABLE owner;
DROP TABLE auto_sale;
DROP TABLE restriction;
DROP TABLE driving_condition;
DROP TABLE ticket;
DROP TABLE ticket_type;
DROP TABLE vehicle;
DROP TABLE vehicle_type;
DROP TABLE drive_licence;
DROP TABLE people;

/*
 *  Table containing all the info for each person
 */
CREATE TABLE  people (
  sin           CHAR(15),  
  name          VARCHAR(40),
  height        number(5,2),
  weight        number(5,2),
  eyecolor      VARCHAR (10),
  haircolor     VARCHAR(10),
  addr          VARCHAR2(50),
  gender        CHAR,
  birthday      DATE,
  PRIMARY KEY (sin),
  CHECK ( gender IN ('m', 'f') )
);

/*
 *  Table containing drive_licence info
 */
CREATE TABLE drive_licence (
  licence_no      CHAR(15),
  sin             char(15),
  class           VARCHAR(10),
  photo           BLOB,
  issuing_date    DATE,
  expiring_date   DATE,
  PRIMARY KEY (licence_no),
  UNIQUE (sin),
  FOREIGN KEY (sin) REFERENCES people
        ON DELETE CASCADE
);

/*
 *  The driving conditions
 */
CREATE TABLE driving_condition (
  c_id        INTEGER,
  description VARCHAR(1024),
  PRIMARY KEY (c_id)
);

/*
 *   to indicate the driving conditions for each drive licence
 */
CREATE TABLE restriction(
  licence_no   CHAR(15),
  r_id         INTEGER,
  PRIMARY KEY (licence_no, r_id),
  FOREIGN KEY (licence_no) REFERENCES drive_licence,
  FOREIGN KEY (r_id) REFERENCES driving_condition
);

/*
 *  to store all the typles of vehicles
 */
CREATE TABLE vehicle_type (
  type_id       integer,
  type          CHAR(10),
  PRIMARY KEY (type_id)
);

/*
 *   Vehicle information
 */
CREATE TABLE vehicle (
  serial_no    CHAR(15),
  maker        VARCHAR(20),	
  model        VARCHAR(20),
  year         number(4,0),
  color        VARCHAR(10),
  type_id      integer,
  PRIMARY KEY (serial_no),
  FOREIGN KEY (type_id) REFERENCES vehicle_type
);

/*
 *   The ownership of each vehicle
 */
CREATE TABLE owner (
  owner_id          CHAR(15),
  vehicle_id        CHAR(15),
  is_primary_owner  CHAR(1),
  PRIMARY KEY (owner_id, vehicle_id),
  FOREIGN KEY (owner_id) REFERENCES people,
  FOREIGN KEY (vehicle_id) REFERENCES vehicle,
  CHECK ( is_primary_owner IN ('y', 'n'))
);

/*
 *  To record auto sales
 */
CREATE TABLE auto_sale (
  transaction_id  int,
  seller_id   CHAR(15),
  buyer_id    CHAR(15),
  vehicle_id  CHAR(15),
  s_date      date,
  price       numeric(9,2),
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (seller_id) REFERENCES people,
  FOREIGN KEY (buyer_id) REFERENCES people,
  FOREIGN KEY (vehicle_id) REFERENCES vehicle
);

/*
 *  all the ticket types
 */
CREATE TABLE ticket_type (
  vtype     CHAR(10),
  fine      number(5,2),
  PRIMARY KEY (vtype)
);

/*
 *  Ticket records
 */
CREATE TABLE ticket (
  ticket_no     int,
  violator_no   CHAR(15),  
  vehicle_id    CHAR(15),
  office_no     CHAR(15),
  vtype        char(10),
  vdate        date,
  place        varchar(20),
  descriptions varchar(1024),
  PRIMARY KEY (ticket_no),
  FOREIGN KEY (vtype) REFERENCES ticket_type,
  FOREIGN KEY (violator_no) REFERENCES people ON DELETE CASCADE,
  FOREIGN KEY (vehicle_id)  REFERENCES vehicle,
  FOREIGN KEY (office_no) REFERENCES people ON DELETE CASCADE
);

/*
 *  Populate the database schema for Assignment 2
 *  CMPUT291, Winter Term, 2015.
 *  Author: Anthony W
 *  University of Alberta
 */

/*PEOPLE*/
INSERT INTO people (SIN,NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
VALUES ('123456789','Sarah',123.45,123.45,'blue','black','1 street','f',TO_DATE('20000101', 'YYYYMMDD'));

INSERT INTO people (SIN,NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
VALUES ('223456789','Peter',223.45,123.45,'brown','black','2 street','m',TO_DATE('20000101', 'YYYYMMDD'));

INSERT INTO people (SIN,NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
VALUES ('323456789','Jack',323.45,123.45,'brown','black','3 street','m',TO_DATE('20000101', 'YYYYMMDD'));

INSERT INTO people (SIN,NAME, HEIGHT,  WEIGHT, EYECOLOR, HAIRCOLOR, ADDR, GENDER, BIRTHDAY)
VALUES ('423456789','Lucy',323.45,123.45,'brown','black','4 street','f',TO_DATE('20000101', 'YYYYMMDD'));

/*DRIVE_LICENCE*/
INSERT INTO drive_licence (LICENCE_NO , SIN , CLASS , PHOTO , ISSUING_DATE , EXPIRING_DATE )
VALUES ('12345','123456789','driving',NULL,TO_DATE('20000101', 'YYYYMMDD'),TO_DATE('20000101', 'YYYYMMDD'));

INSERT INTO drive_licence (LICENCE_NO , SIN , CLASS , PHOTO , ISSUING_DATE , EXPIRING_DATE )
VALUES ('22345','223456789','nondriving',NULL,TO_DATE('20000101', 'YYYYMMDD'),TO_DATE('20000101', 'YYYYMMDD'));

INSERT INTO drive_licence (LICENCE_NO , SIN , CLASS , PHOTO , ISSUING_DATE , EXPIRING_DATE )
VALUES ('32345','323456789','nondriving',NULL,TO_DATE('20000101', 'YYYYMMDD'),TO_DATE('20000101', 'YYYYMMDD'));

INSERT INTO drive_licence (LICENCE_NO , SIN , CLASS , PHOTO , ISSUING_DATE , EXPIRING_DATE )
VALUES ('42345','423456789','nondriving',NULL,TO_DATE('20000101', 'YYYYMMDD'),TO_DATE('20000101', 'YYYYMMDD'));

/*DRIVING_CONDITION*/
INSERT INTO driving_condition (C_ID , DESCRIPTION)
VALUES (11,'hitthecurb');

INSERT INTO driving_condition (C_ID , DESCRIPTION)
VALUES (12,'hitthecar');

INSERT INTO driving_condition (C_ID , DESCRIPTION)
VALUES (13,'hittheditch');

/*RESTRICTION*/
INSERT INTO restriction (LICENCE_NO , R_ID )
VALUES ('12345',11);

INSERT INTO restriction (LICENCE_NO , R_ID )
VALUES ('12345',12);

INSERT INTO restriction (LICENCE_NO , R_ID )
VALUES ('12345',13);

/*VEHICLE_TYPE*/
INSERT INTO vehicle_type (TYPE_ID , TYPE)
VALUES (10,'sedan');

INSERT INTO vehicle_type (TYPE_ID , TYPE)
VALUES (11,'truck');

INSERT INTO vehicle_type (TYPE_ID , TYPE)
VALUES (12,'trailer');

INSERT INTO vehicle_type (TYPE_ID , TYPE)
VALUES (13,'SUV');

/*VEHICLE*/
INSERT INTO vehicle (SERIAL_NO , MAKER , MODEL , YEAR , COLOR , TYPE_ID)
VALUES ('1000000','Kia','sorento','2015','blue',10);

INSERT INTO vehicle (SERIAL_NO , MAKER , MODEL , YEAR , COLOR , TYPE_ID)
VALUES ('2000000','Kia','sorento','2015','blue',11);

INSERT INTO vehicle (SERIAL_NO , MAKER , MODEL , YEAR , COLOR , TYPE_ID)
VALUES ('3000000','Kia','sorento','2015','blue',12);

INSERT INTO vehicle (SERIAL_NO , MAKER , MODEL , YEAR , COLOR , TYPE_ID)
VALUES ('4000000','Nissan','Rogue','2015','red',13);

INSERT INTO vehicle (SERIAL_NO , MAKER , MODEL , YEAR , COLOR , TYPE_ID)
VALUES ('5000000','Nissan','Rogue','2015','red',13);

INSERT INTO vehicle (SERIAL_NO , MAKER , MODEL , YEAR , COLOR , TYPE_ID)
VALUES ('6000000','Nissan','Rogue','2015','red',13);

/*OWNER*/
INSERT INTO owner (OWNER_ID , VEHICLE_ID , IS_PRIMARY_OWNER)
VALUES ('123456789','1000000','y');

INSERT INTO owner (OWNER_ID , VEHICLE_ID , IS_PRIMARY_OWNER)
VALUES ('223456789','2000000','y');

INSERT INTO owner (OWNER_ID , VEHICLE_ID , IS_PRIMARY_OWNER)
VALUES ('323456789','3000000','n');

INSERT INTO owner (OWNER_ID , VEHICLE_ID , IS_PRIMARY_OWNER)
VALUES ('423456789','4000000','y');

INSERT INTO owner (OWNER_ID , VEHICLE_ID , IS_PRIMARY_OWNER)
VALUES ('423456789','5000000','y');

INSERT INTO owner (OWNER_ID , VEHICLE_ID , IS_PRIMARY_OWNER)
VALUES ('423456789','6000000','y');

/*AUTO_SALE*/
INSERT INTO auto_sale (TRANSACTION_ID , SELLER_ID , BUYER_ID , VEHICLE_ID , S_DATE , PRICE )
VALUES (100,'123456789','223456789','2000000',TO_DATE('20000101', 'YYYYMMDD'),20000.00);

INSERT INTO auto_sale (TRANSACTION_ID , SELLER_ID , BUYER_ID , VEHICLE_ID , S_DATE , PRICE )
VALUES (101,'123456789','323456789','3000000',TO_DATE('20000101', 'YYYYMMDD'),40000.00);

INSERT INTO auto_sale (TRANSACTION_ID , SELLER_ID , BUYER_ID , VEHICLE_ID , S_DATE , PRICE )
VALUES (102,'323456789','123456789','1000000',TO_DATE('20000101', 'YYYYMMDD'),20000.00);

/*TICKET_TYPE*/
INSERT INTO ticket_type (VTYPE,FINE) 
VALUES ('parking',300.00);

INSERT INTO ticket_type (VTYPE,FINE) 
VALUES ('alcohol',300.00);

INSERT INTO ticket_type (VTYPE,FINE) 
VALUES ('hitandrun',300.00);

/*TICKET*/  
INSERT INTO ticket (TICKET_NO , VIOLATOR_NO , VEHICLE_ID , OFFICE_NO , VTYPE , VDATE , PLACE , DESCRIPTIONS) 
VALUES (1000, '123456789', '1000000','123456789','parking',TO_DATE('20141201', 'YYYYMMDD'),'traffic','schoolzone');

INSERT INTO ticket (TICKET_NO , VIOLATOR_NO , VEHICLE_ID , OFFICE_NO , VTYPE , VDATE , PLACE , DESCRIPTIONS) 
VALUES (2000, '123456789', '1000000','123456789','parking',TO_DATE('20141201', 'YYYYMMDD'),'traffic','schoolzone');

INSERT INTO ticket (TICKET_NO , VIOLATOR_NO , VEHICLE_ID , OFFICE_NO , VTYPE , VDATE , PLACE , DESCRIPTIONS) 
VALUES (4000, '123456789', '1000000','123456789','parking',TO_DATE('20141201', 'YYYYMMDD'),'traffic','schoolzone');

INSERT INTO ticket (TICKET_NO , VIOLATOR_NO , VEHICLE_ID , OFFICE_NO , VTYPE , VDATE , PLACE , DESCRIPTIONS) 
VALUES (3000, '123456789', '1000000','123456789','hitandrun',TO_DATE('20000101', 'YYYYMMDD'),'traffic light','schoolzone');

