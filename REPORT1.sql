CREATE OR REPLACE FUNCTION getGamesFromEvent(id bigint)
   RETURNS TABLE (nombre_del_juego varchar)
   LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT g.name
    FROM game g
    JOIN user_buy_game ubg ON g.game_id = ubg.game_id
    JOIN event e ON e.event_id = id
    WHERE ubg.purchase_date >= e.start_date AND ubg.purchase_date <= e.end_date;
END;
$$;