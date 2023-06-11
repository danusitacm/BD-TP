create or replace function getGamesFromEvent(id bigint)
   returns table(nameGame varchar) language plpgsql as $$
   declare 
  		startDate date;
		endDate	date;
		gameID bigint;
		var record;
begin
	select start_date into startDate from event where event_id=id;
	select end_date into endDate from event where event_id=id;
	for var in (
		select g.name,ubg.game_id from game g JOIN user_buy_game ubg ON g.game_id=ubg.game_id
		WHERE ubg.purchase_date>=startDate and ubg.purchase_date<=endDate  
	) loop 
	nameGame := (var.name);
	return next;
	end loop;
end;
$$
