# CMPUT 291: Project 1 Makefile 
# Author: Anthony 

# Description: while connected to lab machine & working in git directory ...
# i.   enable sqlplus in ssh remote host 
# ii.  populate DB with sql statements using "project1-data.sql" script
# iii. test our python script 


PATH= source /oracle/oraenv
CC= python3

all:
	set pop test

# i.   enables sqlplus in ssh remote host
set:
	$(PATH) 

# ii.  populates DB with sql statements using "project1-data.sql" script
pop:
	sqlplus ajwu @project1-data.sql

# iii. test python script 
test: mainMenu.py
	python3 mainMenu.py
