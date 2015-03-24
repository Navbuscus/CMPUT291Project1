CMPUT 291 Project 1 Testing Scenarios
=======

Winter 2015
Mini-Project 1
Due time:  18:00 on  March 27, 2015.
Clarifications and notifications:

    No clarification so far.

**Part 1: Vehicle Registration** 

1. Register a new vehicle, its primary owner and its secondary owner. Both owners
are already present in the database.
2. Register a vehicle whose serial number already exists in the database – an
appropriate error message should be shown.
3. Register a new vehicle whose owner is not present in database. Add this person to
the database.

**Part 2: Auto transaction**

1. Add a sale record where buyer does not exist in the database: a new person should
be added after asking appropriate information.
2. Add a sale record where seller is not an owner of the vehicle – an appropriate error
message should be shown.
3. Add a sale record where vehicle does not exist in the database – an appropriate
message should be displayed.

**Part 3: Driver License Registration**

1. Register a new driver license (with photo) where the person does not exist in the
database. – New person should be added.
2. Add driver license for an existing person in database.
3. Add driver license of a person who already has a license. – An error message
should be shown.

**Part 4: Violation Record**

1. Register a violation record where violator/vehicle that does not exist. – An
appropriate message should be shown.
2. Register a violation record for primary owner of a given vehicle.
3. Register a violation record for a given driver and a given vehicle.

**Part 5: Search Engine**

1. Display all information for persons with given name is given that 2 people have.
Eg if name is “Bob” and there are 2 people in the database that have this name,
both their information should be shown.
2. Retrieve all violation records for an invalid license number. An appropriate error
message should be shown.
