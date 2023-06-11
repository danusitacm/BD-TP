create or replace function getActiveUserFromCommunity(idCommunity bigint, review int)
   returns table(nombre_del_usuario varchar , cantidad_de_reviews int)language plpgsql as $$
   declare
   var record;
begin
	for var in (
	select distinct on (u.username)u.username , count(gr.game_review_id) as cant_review 
	from user_1 u 
	inner join comunnity_user cu on u.user_id=cu.user_community_id 
	inner join game_review gr on cu.user_community_id=gr.user_id 
	where community_id=idCommunity group by u.user_id having count(gr.game_review_id) > review)
	loop
	nombre_del_usuario :=(var.username);
	cantidad_de_reviews :=(var.cant_review);
	return next;
	end loop;
end;
$$