# MySQL 5.6

select name, bonus
from Employee join Bonus on Employee.empId = Bonus.empId
where bonus < 1000 or bonus = null