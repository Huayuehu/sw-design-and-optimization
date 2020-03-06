# MySQL 5.6

select distinct Chef 
from Chefskill A 
where not exists
(
  select Dish 
  from Menu B 
  where not exists
  (
    select * 
    from ChefSkill C 
    where C.Dish = B.Dish and C.Chef = A.Chef
  )
);