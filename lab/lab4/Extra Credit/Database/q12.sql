/*MySQL 5.6*/
CREATE TABLE Student_registration
    ( `student_name` varchar(20),  `stu_id` int, `course` varchar(20),`status` varchar(3));

INSERT INTO Student_registration
    (`student_name`,`stu_id`, `course`,`status`)
VALUES
('Amy', 60000, 'EE504','C'),
('Amy', 60000, 'EE501', 'C'),
('Amy', 60000, 'EE505','C'), 
('Joe', 70000, 'EE500','C'),
('Joe', 70000, 'EE501', 'IP'),
('Joe', 70000, 'EE504','C'),
('Henry', 80000, 'EE500' , 'C'),
('Henry', 80000, 'EE502' , 'C'),
('Henry', 80000, 'EE503', 'C'),
('Sam', 62000,'EE501' , 'C'),
('Max', 90000, 'EE502', 'IP'),
('Max', 90000, 'EE503', 'C');  

CREATE TABLE Courses
    ( `course` varchar(20),  `units` int);
INSERT INTO Courses
(`course`,`units`)
VALUES
('EE500',3),
('EE501',4),
('EE502',3),
('EE503',7),
('EE504',4),
('EE505',4),
('EE506',3);
