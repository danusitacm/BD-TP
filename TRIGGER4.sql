CREATE FUNCTION calculo_precio_compra RETURNS trigger AS 
$$
	DECLARE
		discount DECIMAL(10,2);
   	    base_price DECIMAL(10,2);
   	 	total DECIMAL(10,2);
    BEGIN
	total :=0;
	SELECT g.base_price, COALESCE(ge.discount, 0) INTO base_price, discount
	FROM game g
    JOIN game_event ge ON ge.game_id = g.game_id
    JOIN event e ON e.event_id = ge.event_id
    WHERE g.game_id = NEW.game_id
      AND NEW.purchase_date BETWEEN e.start_date AND e.end_date;

    -- Calcular el precio total
	SELECT base_price * (1 - discount) INTO total;
	-- Actualizar el campo total_price en la tabla ubg
    IF TG_OP = 'INSERT' THEN
        NEW.total_price := total;
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        IF total <> NEW.total_price THEN
            NEW.total_price := total;
            RETURN NEW;
            END IF;
        END IF;
  	RETURN NEW;
    END;

LANGUAGE plpgsql;
CREATE TRIGGER calculo_precio_compra
    AFTER INSERT OR UPDATE ON user_buy_game
    FOR EACH ROW 
    EXECUTE PROCEDURE calculo_precio_compra()