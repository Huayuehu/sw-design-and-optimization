# MySQL 5.6

select student_name as Name, sum(units) as Units_complete
from Student_registration join Courses on Student_registration.course = Courses.course
where student_name not in (
  select student_name from Student_registration
  where status = "IP"
)
group by student_name
having Units_complete > 10;