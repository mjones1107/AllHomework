#Megan Jones SQL Homework
use sakila;
# 1a
select first_name, last_name from actor;
#1b
alter table actor
add actor_name varchar(100);
#check this
insert into actor (actor_name) select concat(" ",first_name, " ", last_name) from actor;
select * from actor;
#2a
select actor_id, first_name, last_name from actor where first_name = "Joe"; 
#2b
select * from actor where last_name like '%gen%';
#2c
select last_name, first_name from actor where last_name like '%li%';
#2d
select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China');
#3a
alter table actor add description blob;
select * from actor;
#3b
alter table actor drop description;
select * from actor;
#4a
SELECT last_name, count(last_name) FROM actor GROUP BY last_name;
#4b
SELECT last_name, count(last_name) FROM actor GROUP BY last_name HAVING count(last_name) > 2;
#4c
update actor
set first_name = 'GROUCHO'
where first_name = 'harpo' and last_name = 'williams';
select * from actor where last_name = 'williams';
#4d
update actor
set first_name = 'HARPO'
where first_name = 'groucho' and last_name = 'williams';
select * from actor where last_name = 'williams';
#5a
#6a
SELECT staff.first_name, staff.last_name, address.address
FROM address
INNER JOIN staff ON
staff.address_id=address.address_id;
#6b
SELECT staff.staff_id, staff.first_name, staff.last_name, sum(payment.amount)
FROM payment
JOIN staff ON
staff.staff_id=payment.staff_id
where payment_date like '2005-08-%'
group by staff_id;
#6c
SELECT film.title, count(film_actor.actor_id)
FROM film_actor
JOIN film ON
film.film_id=film_actor.film_id
group by film.title;
#6d
 SELECT COUNT(*)
 FROM inventory
 WHERE film_id IN
 (	SELECT film_id
     FROM film
     WHERE title = 'Hunchback Impossible');
#6e
SELECT customer.customer_id,customer.first_name, customer.last_name, sum(payment.amount)
FROM payment
JOIN customer ON
customer.customer_id=payment.customer_id
group by customer_id
order by first_name asc, last_name asc;
#7a

#7b
 SELECT first_name, last_name
 FROM actor
 WHERE actor_id IN
 (	SELECT actor_id
	FROM film_actor
	WHERE film_id IN
	(	SELECT film_id
		FROM film
		WHERE title = 'Alone Trip'));
#7c
#7d 8 is family
select title, description, rating from film 
where film_id in
(select film_id from film_category where category_id = 8);
#7e

#7f
#7g
#7h
#8a
#8b
#8c