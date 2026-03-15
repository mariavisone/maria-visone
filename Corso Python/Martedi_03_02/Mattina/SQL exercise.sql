-- Estrai i nomi (first_name) e i cognomi (last_name) di tutti gli attori presenti nella tabella actor. Rinomina le colonne come "Nome" e "Cognome" per rendere il report più leggibile.

select first_name as Nome, last_name as Cognome from actor;

-- Trova tutti i titoli dei film che hanno un rating uguale a 'G' (General Audiences)
select * from film 
where rating = 'G';

-- Trova tutti i clienti nella tabella customer il cui nome inizia con la lettera "A" e il cognome finisce con la lettera "S".

select * from customer 
where first_name like 'A%'
and last_name like '%S';

-- Seleziona i film che hanno una durata (length) superiore a 150 minuti E un costo di noleggio (rental_rate) inferiore a 1.00$.

select * from film
where length > 150 and rental_rate < 1.00 order by length;

