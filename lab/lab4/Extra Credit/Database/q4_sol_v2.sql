# MySQL 5.6

select chef
from ChefSkill
where Dish in (
	select Dish from Menu
)
group by Chef
having count(ChefSkill.Dish) = (select count(Menu.Dish) from Menu);