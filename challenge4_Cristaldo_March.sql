
CREATE SEQUENCE public.genre_genre_id_seq;

CREATE TABLE public.genre (
                genre_id BIGINT NOT NULL DEFAULT nextval('public.genre_genre_id_seq'),
                description_genre VARCHAR(300) NOT NULL,
                genre VARCHAR(100) NOT NULL,
                CONSTRAINT genre_id PRIMARY KEY (genre_id)
);


ALTER SEQUENCE public.genre_genre_id_seq OWNED BY public.genre.genre_id;

CREATE SEQUENCE public.balance_balance_id_seq;

CREATE TABLE public.balance (
                balance_id BIGINT NOT NULL DEFAULT nextval('public.balance_balance_id_seq'),
                amount REAL DEFAULT 0 NOT NULL,
                payment_type VARCHAR(200) NOT NULL,
                CONSTRAINT balance_id PRIMARY KEY (balance_id)
);


ALTER SEQUENCE public.balance_balance_id_seq OWNED BY public.balance.balance_id;

CREATE SEQUENCE public.developer_developer_id_seq_1;

CREATE TABLE public.developer (
                developer_id BIGINT NOT NULL DEFAULT nextval('public.developer_developer_id_seq_1'),
                name VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                star_date DATE NOT NULL,
                CONSTRAINT developer_id PRIMARY KEY (developer_id)
);


ALTER SEQUENCE public.developer_developer_id_seq_1 OWNED BY public.developer.developer_id;

CREATE SEQUENCE public.rarity_rarity_id_seq_1;

CREATE TABLE public.rarity (
                rarity_id BIGINT NOT NULL DEFAULT nextval('public.rarity_rarity_id_seq_1'),
                name VARCHAR(100) NOT NULL,
                scale NUMERIC(5) NOT NULL,
                CONSTRAINT rarity_id PRIMARY KEY (rarity_id)
);


ALTER SEQUENCE public.rarity_rarity_id_seq_1 OWNED BY public.rarity.rarity_id;

CREATE SEQUENCE public.user_1_user_id_seq;

CREATE TABLE public.user_1 (
                user_id BIGINT NOT NULL DEFAULT nextval('public.user_1_user_id_seq'),
                banned BOOLEAN DEFAULT FALSE NOT NULL,
                start_date DATE NOT NULL,
                username VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                balance_id BIGINT NOT NULL,
                CONSTRAINT user_id PRIMARY KEY (user_id)
);


ALTER SEQUENCE public.user_1_user_id_seq OWNED BY public.user_1.user_id;

CREATE SEQUENCE public.user_review_user_review_id_seq;

CREATE TABLE public.user_review (
                user_review_id BIGINT NOT NULL DEFAULT nextval('public.user_review_user_review_id_seq'),
                publish_date DATE NOT NULL,
                title VARCHAR(100) NOT NULL,
                description VARCHAR(300),
                score REAL NOT NULL,
                user_seller_id BIGINT NOT NULL,
                user_reviewer_id BIGINT NOT NULL,
                CONSTRAINT user_review_id PRIMARY KEY (user_review_id)
);


ALTER SEQUENCE public.user_review_user_review_id_seq OWNED BY public.user_review.user_review_id;

CREATE SEQUENCE public.game_game_id_seq;

CREATE TABLE public.game (
                game_id BIGINT NOT NULL DEFAULT nextval('public.game_game_id_seq'),
                description VARCHAR(300),
                name VARCHAR(100) NOT NULL,
                release_date DATE NOT NULL,
                base_price REAL DEFAULT 0 NOT NULL,
                developer_id BIGINT NOT NULL,
                CONSTRAINT game_id PRIMARY KEY (game_id)
);


ALTER SEQUENCE public.game_game_id_seq OWNED BY public.game.game_id;

CREATE TABLE public.genre_game (
                game_id BIGINT NOT NULL,
                genre_id BIGINT NOT NULL,
                CONSTRAINT genre_game_id PRIMARY KEY (game_id, genre_id)
);


CREATE SEQUENCE public.user_buy_game_user_buy_game_seq;

CREATE TABLE public.user_buy_game (
                user_buy_game BIGINT NOT NULL DEFAULT nextval('public.user_buy_game_user_buy_game_seq'),
                total_price REAL NOT NULL,
                purchase_date DATE NOT NULL,
                game_id BIGINT NOT NULL,
                user_id BIGINT NOT NULL,
                CONSTRAINT user_buy_game_id PRIMARY KEY (user_buy_game)
);


ALTER SEQUENCE public.user_buy_game_user_buy_game_seq OWNED BY public.user_buy_game.user_buy_game;

CREATE SEQUENCE public.game_review_game_review_id_seq;

CREATE TABLE public.game_review (
                game_review_id BIGINT NOT NULL DEFAULT nextval('public.game_review_game_review_id_seq'),
                description VARCHAR(300),
                publish_date DATE NOT NULL,
                score REAL NOT NULL,
                title VARCHAR(100) NOT NULL,
                game_id BIGINT NOT NULL,
                user_id BIGINT NOT NULL,
                CONSTRAINT game_review_id PRIMARY KEY (game_review_id)
);


ALTER SEQUENCE public.game_review_game_review_id_seq OWNED BY public.game_review.game_review_id;

CREATE SEQUENCE public.item_item_id_seq;

CREATE TABLE public.item (
                item_id BIGINT NOT NULL DEFAULT nextval('public.item_item_id_seq'),
                name VARCHAR(100) NOT NULL,
                price REAL NOT NULL,
                description VARCHAR(300),
                game_id BIGINT NOT NULL,
                rarity_id BIGINT NOT NULL,
                CONSTRAINT item_id PRIMARY KEY (item_id)
);


ALTER SEQUENCE public.item_item_id_seq OWNED BY public.item.item_id;

CREATE SEQUENCE public.user_got_item_user_got_item_id_seq_1;

CREATE TABLE public.user_got_item (
                user_got_item_id BIGINT NOT NULL DEFAULT nextval('public.user_got_item_user_got_item_id_seq_1'),
                drop_date DATE NOT NULL,
                user_id BIGINT NOT NULL,
                item_id BIGINT NOT NULL,
                status VARCHAR(100) NOT NULL,
                CONSTRAINT user_got_item_id PRIMARY KEY (user_got_item_id)
);


ALTER SEQUENCE public.user_got_item_user_got_item_id_seq_1 OWNED BY public.user_got_item.user_got_item_id;

CREATE SEQUENCE public.market_market_id_seq;

CREATE TABLE public.market (
                market_id VARCHAR NOT NULL DEFAULT nextval('public.market_market_id_seq'),
                user_id BIGINT NOT NULL,
                user_got_item_id BIGINT NOT NULL,
                price REAL NOT NULL,
                CONSTRAINT market_id PRIMARY KEY (market_id)
);


ALTER SEQUENCE public.market_market_id_seq OWNED BY public.market.market_id;

CREATE SEQUENCE public.user_buy_item_user_buy_item_id_seq;

CREATE TABLE public.user_buy_item (
                user_buy_item_id BIGINT NOT NULL DEFAULT nextval('public.user_buy_item_user_buy_item_id_seq'),
                purchase_date DATE NOT NULL,
                user_buyer_id BIGINT NOT NULL,
                market_id VARCHAR NOT NULL,
                CONSTRAINT user_buy_item_id PRIMARY KEY (user_buy_item_id)
);


ALTER SEQUENCE public.user_buy_item_user_buy_item_id_seq OWNED BY public.user_buy_item.user_buy_item_id;

CREATE SEQUENCE public.event_event_id_seq;

CREATE TABLE public.event (
                event_id BIGINT NOT NULL DEFAULT nextval('public.event_event_id_seq'),
                name VARCHAR(100) NOT NULL,
                description VARCHAR(300),
                star_date DATE NOT NULL,
                end_date DATE NOT NULL,
                CONSTRAINT event_id PRIMARY KEY (event_id)
);


ALTER SEQUENCE public.event_event_id_seq OWNED BY public.event.event_id;

CREATE TABLE public.game_event (
                event_id BIGINT NOT NULL,
                game_id BIGINT NOT NULL,
                discount REAL NOT NULL,
                CONSTRAINT game_event_id PRIMARY KEY (event_id, game_id)
);


CREATE SEQUENCE public.community_community_id_seq;

CREATE TABLE public.community (
                community_id BIGINT NOT NULL DEFAULT nextval('public.community_community_id_seq'),
                name VARCHAR(100) NOT NULL,
                description VARCHAR(300),
                CONSTRAINT community_id PRIMARY KEY (community_id)
);


ALTER SEQUENCE public.community_community_id_seq OWNED BY public.community.community_id;

CREATE TABLE public.comunnity_user (
                community_id BIGINT NOT NULL,
                user_id BIGINT NOT NULL,
                CONSTRAINT comunnity_user_id PRIMARY KEY (community_id, user_id)
);


ALTER TABLE public.genre_game ADD CONSTRAINT genre_genre_game_fk
FOREIGN KEY (genre_id)
REFERENCES public.genre (genre_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_1 ADD CONSTRAINT wallet_user_fk
FOREIGN KEY (balance_id)
REFERENCES public.balance (balance_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.game ADD CONSTRAINT developer_game_fk
FOREIGN KEY (developer_id)
REFERENCES public.developer (developer_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.item ADD CONSTRAINT rarity_item_fk
FOREIGN KEY (rarity_id)
REFERENCES public.rarity (rarity_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.game_review ADD CONSTRAINT user_game_review_fk
FOREIGN KEY (user_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_review ADD CONSTRAINT user_user_review_fk
FOREIGN KEY (user_seller_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_review ADD CONSTRAINT user_user_review_fk1
FOREIGN KEY (user_reviewer_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_buy_game ADD CONSTRAINT user_user_buy_game_fk
FOREIGN KEY (user_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_buy_item ADD CONSTRAINT user_user_buy_item_fk1
FOREIGN KEY (user_buyer_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_got_item ADD CONSTRAINT user_user_got_item_fk
FOREIGN KEY (user_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.market ADD CONSTRAINT user_market_fk
FOREIGN KEY (user_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.comunnity_user ADD CONSTRAINT user_1_comunnity_user_fk
FOREIGN KEY (user_id)
REFERENCES public.user_1 (user_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.item ADD CONSTRAINT game_item_fk
FOREIGN KEY (game_id)
REFERENCES public.game (game_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.game_event ADD CONSTRAINT game_game_event_fk
FOREIGN KEY (game_id)
REFERENCES public.game (game_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.game_review ADD CONSTRAINT game_game_review_fk
FOREIGN KEY (game_id)
REFERENCES public.game (game_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_buy_game ADD CONSTRAINT game_user_buy_game_fk
FOREIGN KEY (game_id)
REFERENCES public.game (game_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.genre_game ADD CONSTRAINT game_genre_game_fk
FOREIGN KEY (game_id)
REFERENCES public.game (game_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_got_item ADD CONSTRAINT item_user_got_item_fk
FOREIGN KEY (item_id)
REFERENCES public.item (item_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.market ADD CONSTRAINT user_got_item_market_fk
FOREIGN KEY (user_got_item_id)
REFERENCES public.user_got_item (user_got_item_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.user_buy_item ADD CONSTRAINT market_user_buy_item_fk
FOREIGN KEY (market_id)
REFERENCES public.market (market_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.game_event ADD CONSTRAINT event_game_event_fk
FOREIGN KEY (event_id)
REFERENCES public.event (event_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.comunnity_user ADD CONSTRAINT community_comunnity_user_fk
FOREIGN KEY (community_id)
REFERENCES public.community (community_id)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
