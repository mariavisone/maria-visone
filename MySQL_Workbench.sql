/*Scrivete una query SQL che restituisca solo i record dalla tabella 
"products"con un prezzo superiore a 50.*/

/*select * from products 
where buyPrice > 50
order by buyPrice */

/*Scrivete una query SQL che elimini tutti gli ordini nella tabella
 "orders" con lo stato "Cancelled".*/
 
use classicmodels;
select orderNumber from orders where status = "Cancelled";

-- cancello prima questi dalla tabella gli ordini collegati alla tabella orders
-- orderNumber è la chiave condivisa, quindi uso questa per riferirmi ai prodotti presenti in entrambe le tabelle 

delete from orderdetails
where orderNumber IN (
select orderNumber from orders where status = "Cancelled"
);

-- eliminazione della tabella dove ce la chiave primaria
delete from orders
where status = "Cancelled";



