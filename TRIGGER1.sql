CREATE FUNCTION antisolapamiento_de_eventos() RETURNS trigger AS 
$$
	BEGIN
		IF EXISTS (
		SELECT 1
		FROM event
		WHERE NEW.start_date <= end_date
		ORDER BY end_date DESC
		LIMIT 1
	) THEN 
		RAISE EXCEPTION 'No se puede insertar o actualizar el evento debido a que ya existe un evento en esas fechas';
	END IF; 
	RETURN NEW;
	END;
$$
LANGUAGE plpgsql;
CREATE TRIGGER antisolapamiento_de_eventos 
	BEFORE INSERT OR UPDATE ON event
	FOR EACH ROW 
	EXECUTE PROCEDURE antisolapamiento_de_eventos()