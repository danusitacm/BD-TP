CREATE FUNCTION antisolapamiento_de_eventos() RETURNS trigger AS 
$$
	BEGIN
		IF (select end_date from event where NEW.star_date <= end_date order by end_date desc LIMIT 1) is not null THEN 
			RAISE EXCEPTION 'Ya existe un evento, no autorizo';
		END IF; 
		RETURN NEW;
	END;
$$
LANGUAGE plpgsql;
CREATE TRIGGER antisolapamiento_de_eventos 
	BEFORE INSERT OR UPDATE ON event
	FOR EACH ROW 
	EXECUTE PROCEDURE antisolapamiento_de_eventos()