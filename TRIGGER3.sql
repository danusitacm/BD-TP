CREATE FUNCTION user_no_review_si_no_compro() RETURNS trigger AS 
$$
	BEGIN
		if NOT EXISTS (
		SELECT 1
		FROM  user_buy_game
		WHERE NEW.user_id = user_id
		AND game_id = NEW.game_id
	) THEN 
		RAISE EXCEPTION 'El usuario debe comprar el juego antes de dejar una reseña';
	END IF; 
	RETURN NEW;
		IF NOT EXISTS (SELECT 1 FROM user_buy_game WHERE NEW.user_id = user_id AND  game_id = NEW.game_id) THEN 
			RAISE EXCEPTION 'No podes dejar review si no compras kp, no autorizo';
		END IF; 
		RETURN NEW;
	END;
$$
LANGUAGE plpgsql;
CREATE TRIGGER user_no_review_si_no_compro 
	BEFORE INSERT OR UPDATE ON user_review
	FOR EACH ROW 
	EXECUTE PROCEDURE uuser_no_review_si_no_compro();
