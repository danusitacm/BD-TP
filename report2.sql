create or replace function getActiveUserFromCommunity(idCommunity bigint, review int)
   returns table(nombre_del_usuario varchar , cantidad_de_reviews int)language plpgsql as $$
   declare
   var record;
	begin
	for var in (
	select username, count(gr.game_review_id) as cant_review
	from user_1 u
	join comunnity_user cu on cu.user_community_id=u.user_id and cu.community_id=idCommunity
	left join game_review gr on gr.user_id = cu.user_community_id
	group by u.user_id having count(gr.game_review_id) >= review)
	loop
	nombre_del_usuario :=(var.username);
	cantidad_de_reviews :=(var.cant_review);
	return next;
	end loop;
end;
