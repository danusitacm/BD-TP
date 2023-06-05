CREATE FUNCTION user_no_compra_a_si_mismo() RETURNS trigger AS 
$$
	BEGIN
<<<<<<< HEAD
		IF EXISTS (
		SELECT 1
		FROM item_transacction
		WHERE NEW.user_buyer_id = user_seller_id
		ORDER BY user_seller_id DESC
		LIMIT 1
	) THEN 
		RAISE EXCEPTION 'No se puede insertar o actualizar la transaccion debido a que un usuario no puede comprar su mismo item';
	END IF; 
	RETURN NEW;
=======
		IF EXISTS (SELECT 1 FROM item_transacction WHERE NEW.user_buyer_id = user_seller_id ORDER BY user_seller_id DESC LIMIT 1) THEN 
			RAISE EXCEPTION 'No podes comprarte a ti mismo, no autorizo';
		END IF; 
		RETURN NEW;
>>>>>>> mercado
	END;
$$
LANGUAGE plpgsql;
CREATE TRIGGER user_no_compra_a_si_mismo 
	BEFORE INSERT OR UPDATE ON item_transacction
	FOR EACH ROW 
	EXECUTE PROCEDURE user_no_compra_a_si_mismo()
