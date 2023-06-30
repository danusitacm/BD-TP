CREATE FUNCTION calculo_precio_compra() RETURNS trigger AS 
$$
	DECLARE
		discount DECIMAL(10,2);
   	    b_price DECIMAL(10,2);
   	 	total DECIMAL(10,2);
    BEGIN
	total :=0;
	discount :=0;
	--Obtener el descuento--
	SELECT COALESCE(
    (SELECT ge.discount
    FROM game g
    JOIN game_event ge ON ge.game_id = g.game_id
    JOIN event e ON e.event_id = ge.event_id
    WHERE g.game_id = NEW.game_id
    AND NEW.purchase_date BETWEEN e.start_date AND e.end_date),
    0
	) INTO discount;
	--Calcular el precio total--
	SELECT g.base_price * (1 - discount) INTO total
	FROM game g
	WHERE g.game_id = NEW.game_id;
	-- Actualizar el campo total_price en la tabla ubg
	NEW.total_price := total;
  	RETURN NEW;
    END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER calculo_precio_compra
    BEFORE INSERT OR UPDATE ON user_buy_game
    FOR EACH ROW 
    EXECUTE PROCEDURE calculo_precio_compra()