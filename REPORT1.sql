CREATE OR REPLACE FUNCTION getGamesFromEvent(id bigint)
   RETURNS TABLE (nameGame varchar)
   LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT g.name
    FROM game g
    JOIN user_buy_game ubg ON g.game_id = ubg.game_id
    WHERE ubg.purchase_date BETWEEN (SELECT start_date FROM event WHERE event_id = id)
    AND (SELECT end_date FROM event WHERE event_id = id);
    RETURN;
END;
$$;