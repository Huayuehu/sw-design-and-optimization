/*MySQL 5.6*/
CREATE TABLE ChefSkill
    (Chef varchar(5) NOT NULL, 
     Dish varchar(30) NOT NULL,
     PRIMARY KEY (Chef, Dish)
    );

INSERT INTO ChefSkill
    (Chef, Dish)
VALUES
    ('A', 'Mint chocolate brownie'),
    ('B', 'Upside down pineapple cake'),
    ('B', 'Creme brulee'),
    ('B', 'Mint chocolate brownie'),
    ('C', 'Upside down pineapple cake'),
    ('C', 'Creme brulee'),
    ('D', 'Apple pie'),
    ('D', 'Upside down pineapple cake'),
    ('D', 'Creme brulee'),
    ('E', 'Apple pie'),
    ('E', 'Upside down pineapple cake'),
    ('E', 'Creme brulee'),
    ('E', 'Bananas Foster');

CREATE TABLE Menu
    (Dish varchar(30) NOT NULL PRIMARY KEY);

INSERT INTO Menu
    (Dish)
VALUES
    ('Apple pie'),
    ('Upside down pineapple cake'),
    ('Creme brulee');
