create or replace function getuserhistory(userId bigint) 
returns table(
juego_comprados varchar,
fecha_compra date,
nombre_del_evento varchar,
regalo boolean,
destinatario_regalo varchar,
review int) language plpgsql 
as $$
DECLARE 
    nombre_usuario varchar;
    var_r record;
BEGIN
    SELECT username INTO nombre_usuario FROM user_1 WHERE user_id = userId;
    RAISE NOTICE 'Nombre de usuario: %', nombre_usuario;
    FOR var_r IN (
        SELECT DISTINCT on (ubg.purchase_date)
            g.name,
            ubg.purchase_date,
            CASE WHEN ubg.purchase_date BETWEEN e.start_date AND e.end_date THEN e.name ELSE NULL END AS name_event,
            gi.community_gift_id,
            rg.game_review_id
        FROM
            user_buy_game ubg
            JOIN game g ON ubg.game_id = g.game_id
            LEFT JOIN game_event ge ON ubg.game_id = ge.game_id 
            LEFT JOIN event e ON ge.event_id= e.event_id
            LEFT JOIN gift gi ON ubg.user_id= gi.user_id AND ubg.game_id=gi.game_gift_id
            LEFT JOIN community co ON gi.community_gift_id = co.community_id 
            LEFT JOIN game_review rg ON ubg.game_id = rg.game_id AND  ubg.user_id= rg.user_id 
        WHERE
            ubg.user_id = userId
    ) LOOP
        juego_comprados := var_r.name;
        fecha_compra := var_r.purchase_date;
        nombre_del_evento := var_r.name_event;
        regalo := var_r.community_gift_id IS NOT NULL;
        destinatario_regalo := CASE WHEN var_r.community_gift_id IS NOT NULL THEN var_r.name END;
        review := var_r.game_review_id;
        RETURN NEXT;
    END LOOP;
END;
$$