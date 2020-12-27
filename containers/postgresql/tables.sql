-- Table: public.player

-- DROP TABLE public.player;

CREATE TABLE IF NOT EXISTS public.player
(
    url text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default",
    id text COLLATE pg_catalog."default",
    "Date of Birth" text COLLATE pg_catalog."default",
    "Position" text COLLATE pg_catalog."default",
    "Age" text COLLATE pg_catalog."default",
    "Height" text COLLATE pg_catalog."default",
    "Place of Birth" text COLLATE pg_catalog."default",
    "Weight" text COLLATE pg_catalog."default",
    "Nation" text COLLATE pg_catalog."default",
    "Shoots" text COLLATE pg_catalog."default",
    "Youth Team" text COLLATE pg_catalog."default",
    "Contract" text COLLATE pg_catalog."default",
    "Cap Hit" text COLLATE pg_catalog."default",
    "NHL Rights" text COLLATE pg_catalog."default",
    "Drafted" text COLLATE pg_catalog."default",
    "Agency" text COLLATE pg_catalog."default",
    "Highlights" text COLLATE pg_catalog."default",
    "Status" text COLLATE pg_catalog."default",
    "NHL Draft" text COLLATE pg_catalog."default",
    "Rankings" text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.player
    OWNER to postgres;

-- Table: public.player_season

-- DROP TABLE public.player_season;

CREATE TABLE IF NOT EXISTS public.player_season
(
    "S" text COLLATE pg_catalog."default",
    "Team" text COLLATE pg_catalog."default",
    "League" text COLLATE pg_catalog."default",
    "GP" text COLLATE pg_catalog."default",
    "G" text COLLATE pg_catalog."default",
    "A" text COLLATE pg_catalog."default",
    "TP" text COLLATE pg_catalog."default",
    "PIM" text COLLATE pg_catalog."default",
    "+/-" text COLLATE pg_catalog."default",
    "Unnamed: 9" text COLLATE pg_catalog."default",
    "POST" text COLLATE pg_catalog."default",
    "GP.1" text COLLATE pg_catalog."default",
    "G.1" text COLLATE pg_catalog."default",
    "A.1" text COLLATE pg_catalog."default",
    "TP.1" text COLLATE pg_catalog."default",
    "PIM.1" text COLLATE pg_catalog."default",
    "+/-.1" text COLLATE pg_catalog."default",
    player_id text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.player_season
    OWNER to postgres;