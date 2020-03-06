# MySQL 5.6

select chef
from ChefSkill join Menu on ChefSkill.Dish = Menu.Dish
group by Chef
having count(ChefSkill.Dish) = (select count(Menu.Dish) from Menu);