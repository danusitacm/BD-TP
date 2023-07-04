CREATE OR REPLACE FUNCTION getGamesFromEvent(id bigint)
   RETURNS TABLE (nombre_del_juego varchar)
   LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT g.name
    FROM game_event ge
	JOIN game g on ge.game_id=g.game_id
    JOIN user_buy_game ubg ON ge.game_id = ubg.game_id
    JOIN event e ON e.event_id = ge.event_id
    WHERE ubg.purchase_date >= e.start_date AND ubg.purchase_date <= e.end_date
	AND ge.event_id=id;
END;
$$;