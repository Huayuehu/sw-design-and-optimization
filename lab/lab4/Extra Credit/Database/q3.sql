/*MySQL 5.6*/ 
CREATE TABLE Employee
    (`empId` int, `name` varchar(6), `supervisor` varchar(4), `salary` int, PRIMARY KEY(empId));
    
INSERT INTO Employee
    (`empId`, `name`, `supervisor`, `salary`)
VALUES
    (1, 'John', '3', 1000),
    (2, 'Dan', '3', 2000),
    (3, 'Brad', NULL, 4000),
    (4, 'Thomas', '3', 4000);

CREATE TABLE Bonus
    (`empId` int, `bonus` int, PRIMARY KEY(empId));
    
INSERT INTO Bonus
    (`empId`, `bonus`)
VALUES
    (2, 500),
    (4, 2000);
