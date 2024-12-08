select supplier_id, max(unit_price) as max_price from products
where supplier_id in (1, 3, 5)
group by supplier_id 
order by supplier_id 
