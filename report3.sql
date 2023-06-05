create or replace function getuserhistory(userId bigint) 
returns table(
juego_comprados varchar,
fecha_compra date,
nombre_del_evento varchar,
regalo boolean,
destinatario_regalo varchar,
review varchar) language plpgsql 
as $$
declare 
nombre_usuario varchar;
var_r record;
begin
    select username from user_1 into nombre_usuario where user_id=userId;
    raise notice 'Nombre de usuario: %', nombre_usuario;
    for var_r in(
		select distinct on ( u.user_id, g.name, ubg.purchase_date) u.user_id, g.name, ubg.purchase_date, 
		case when ubg.purchase_date between e.star_date and e.end_date then e.name
			else null
			end as name_event,
		case when gi.game_gift_id=ubg.game_id then true 
			else false
			end as setgift,
		case when gi.game_gift_id=ubg.game_id then co.name
			else null
			end as setgift2
		from user_1 u
		JOIN user_buy_game ubg on ubg.user_id=u.user_id
		JOIN game g on g.game_id=ubg.game_id
		JOIN game_event ge on ge.game_id=ubg.game_id
		JOIN event e on e.event_id=ge.event_id
		JOIN gift gi on gi.user_id=u.user_id
		join community co on co.community_id=gi.community_gift_id
		where u.user_id=userId)
    loop
        juego_comprados := (var_r.name); 
        fecha_compra := (var_r.purchase_date);
    return next;
    end loop;
end;
$$