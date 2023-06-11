CREATE FUNCTION calculo_precio_compra() RETURNS trigger AS
$$
	DECLARE
		discount DECIMAL(10,2);
   	    base_price DECIMAL(10,2);
   	 	total_price DECIMAL(10,2);
    BEGIN
	SELECT g.base_price, ge.discount INTO base_price, discount
    FROM game g
    JOIN game_event ge ON ge.game_id = g.game_id
    JOIN event e ON e.event_id = ge.event_id
    WHERE g.game_id = NEW.game_id
      AND NEW.purchase_date BETWEEN e.start_date AND e.end_date;

    -- Calcular el precio total
	select base_price - (base_price * discount) into total_price;
   
    -- Actualizar el campo total_price en la tabla ubg
    UPDATE user_buy_game SET total_price = total_price WHERE user_id = NEW.user_id AND purchase_id = NEW.purchase_id;
  	RETURN NEW;
    END;
$$
LANGUAGE plpgsql;
CREATE TRIGGER calculo_precio_compra
    AFTER INSERT OR UPDATE ON user_buy_game
    FOR EACH ROW 
    EXECUTE PROCEDURE calculo_precio_compra()