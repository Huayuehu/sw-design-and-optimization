# MySQL 5.6

select student_name as name, stu_id from Student_registration
where student_name not in (
  select student_name from Student_registration
  where status = "IP"
)
group by student_name
order by stu_id asc;