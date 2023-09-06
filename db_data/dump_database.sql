--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.4 (Debian 15.4-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: types_movement; Type: TYPE; Schema: public; Owner: banza
--

CREATE TYPE public.types_movement AS ENUM (
    'ingreso',
    'egreso'
);


ALTER TYPE public.types_movement OWNER TO banza;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Categoria; Type: TABLE; Schema: public; Owner: banza
--

CREATE TABLE public."Categoria" (
    id integer NOT NULL,
    nombre character varying
);


ALTER TABLE public."Categoria" OWNER TO banza;

--
-- Name: Categoria_Cliente; Type: TABLE; Schema: public; Owner: banza
--

CREATE TABLE public."Categoria_Cliente" (
    id_categoria integer NOT NULL,
    id_cliente integer NOT NULL
);


ALTER TABLE public."Categoria_Cliente" OWNER TO banza;

--
-- Name: Categoria_id_seq; Type: SEQUENCE; Schema: public; Owner: banza
--

CREATE SEQUENCE public."Categoria_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Categoria_id_seq" OWNER TO banza;

--
-- Name: Categoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: banza
--

ALTER SEQUENCE public."Categoria_id_seq" OWNED BY public."Categoria".id;


--
-- Name: Cliente; Type: TABLE; Schema: public; Owner: banza
--

CREATE TABLE public."Cliente" (
    id integer NOT NULL,
    nombre character varying
);


ALTER TABLE public."Cliente" OWNER TO banza;

--
-- Name: Cliente_id_seq; Type: SEQUENCE; Schema: public; Owner: banza
--

CREATE SEQUENCE public."Cliente_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Cliente_id_seq" OWNER TO banza;

--
-- Name: Cliente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: banza
--

ALTER SEQUENCE public."Cliente_id_seq" OWNED BY public."Cliente".id;


--
-- Name: Cuenta; Type: TABLE; Schema: public; Owner: banza
--

CREATE TABLE public."Cuenta" (
    id integer NOT NULL,
    id_cliente integer
);


ALTER TABLE public."Cuenta" OWNER TO banza;

--
-- Name: Cuenta_id_seq; Type: SEQUENCE; Schema: public; Owner: banza
--

CREATE SEQUENCE public."Cuenta_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Cuenta_id_seq" OWNER TO banza;

--
-- Name: Cuenta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: banza
--

ALTER SEQUENCE public."Cuenta_id_seq" OWNED BY public."Cuenta".id;


--
-- Name: Movimiento; Type: TABLE; Schema: public; Owner: banza
--

CREATE TABLE public."Movimiento" (
    id integer NOT NULL,
    id_cuenta integer,
    tipo public.types_movement,
    importe numeric(10,2),
    fecha timestamp without time zone
);


ALTER TABLE public."Movimiento" OWNER TO banza;

--
-- Name: Movimiento_id_seq; Type: SEQUENCE; Schema: public; Owner: banza
--

CREATE SEQUENCE public."Movimiento_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movimiento_id_seq" OWNER TO banza;

--
-- Name: Movimiento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: banza
--

ALTER SEQUENCE public."Movimiento_id_seq" OWNED BY public."Movimiento".id;


--
-- Name: Categoria id; Type: DEFAULT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Categoria" ALTER COLUMN id SET DEFAULT nextval('public."Categoria_id_seq"'::regclass);


--
-- Name: Cliente id; Type: DEFAULT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Cliente" ALTER COLUMN id SET DEFAULT nextval('public."Cliente_id_seq"'::regclass);


--
-- Name: Cuenta id; Type: DEFAULT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Cuenta" ALTER COLUMN id SET DEFAULT nextval('public."Cuenta_id_seq"'::regclass);


--
-- Name: Movimiento id; Type: DEFAULT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Movimiento" ALTER COLUMN id SET DEFAULT nextval('public."Movimiento_id_seq"'::regclass);


--
-- Data for Name: Categoria; Type: TABLE DATA; Schema: public; Owner: banza
--

COPY public."Categoria" (id, nombre) FROM stdin;
1	Persona Fisica
2	Empresa
\.


--
-- Data for Name: Categoria_Cliente; Type: TABLE DATA; Schema: public; Owner: banza
--

COPY public."Categoria_Cliente" (id_categoria, id_cliente) FROM stdin;
1	1
\.


--
-- Data for Name: Cliente; Type: TABLE DATA; Schema: public; Owner: banza
--

COPY public."Cliente" (id, nombre) FROM stdin;
1	Julio Sejas
\.


--
-- Data for Name: Cuenta; Type: TABLE DATA; Schema: public; Owner: banza
--

COPY public."Cuenta" (id, id_cliente) FROM stdin;
1	1
2	1
\.


--
-- Data for Name: Movimiento; Type: TABLE DATA; Schema: public; Owner: banza
--

COPY public."Movimiento" (id, id_cuenta, tipo, importe, fecha) FROM stdin;
1	1	ingreso	20000.00	2023-09-06 12:12:09.062634
2	1	ingreso	5000.00	2023-09-06 12:12:09.062634
3	1	egreso	1000.00	2023-09-06 12:12:09.062634
4	2	ingreso	2500.00	2023-09-06 12:12:09.062634
5	2	ingreso	500.00	2023-09-06 12:12:09.062634
6	2	ingreso	550.00	2023-09-06 12:12:09.062634
\.


--
-- Name: Categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: banza
--

SELECT pg_catalog.setval('public."Categoria_id_seq"', 2, true);


--
-- Name: Cliente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: banza
--

SELECT pg_catalog.setval('public."Cliente_id_seq"', 1, true);


--
-- Name: Cuenta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: banza
--

SELECT pg_catalog.setval('public."Cuenta_id_seq"', 2, true);


--
-- Name: Movimiento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: banza
--

SELECT pg_catalog.setval('public."Movimiento_id_seq"', 6, true);


--
-- Name: Categoria_Cliente Categoria_Cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Categoria_Cliente"
    ADD CONSTRAINT "Categoria_Cliente_pkey" PRIMARY KEY (id_categoria, id_cliente);


--
-- Name: Categoria Categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Categoria"
    ADD CONSTRAINT "Categoria_pkey" PRIMARY KEY (id);


--
-- Name: Cliente Cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_pkey" PRIMARY KEY (id);


--
-- Name: Cuenta Cuenta_pkey; Type: CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Cuenta"
    ADD CONSTRAINT "Cuenta_pkey" PRIMARY KEY (id);


--
-- Name: Movimiento Movimiento_pkey; Type: CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Movimiento"
    ADD CONSTRAINT "Movimiento_pkey" PRIMARY KEY (id);


--
-- Name: ix_Categoria_id; Type: INDEX; Schema: public; Owner: banza
--

CREATE INDEX "ix_Categoria_id" ON public."Categoria" USING btree (id);


--
-- Name: ix_Cliente_id; Type: INDEX; Schema: public; Owner: banza
--

CREATE INDEX "ix_Cliente_id" ON public."Cliente" USING btree (id);


--
-- Name: ix_Cuenta_id; Type: INDEX; Schema: public; Owner: banza
--

CREATE INDEX "ix_Cuenta_id" ON public."Cuenta" USING btree (id);


--
-- Name: ix_Movimiento_id; Type: INDEX; Schema: public; Owner: banza
--

CREATE INDEX "ix_Movimiento_id" ON public."Movimiento" USING btree (id);


--
-- Name: Categoria_Cliente Categoria_Cliente_id_categoria_fkey; Type: FK CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Categoria_Cliente"
    ADD CONSTRAINT "Categoria_Cliente_id_categoria_fkey" FOREIGN KEY (id_categoria) REFERENCES public."Categoria"(id);


--
-- Name: Categoria_Cliente Categoria_Cliente_id_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Categoria_Cliente"
    ADD CONSTRAINT "Categoria_Cliente_id_cliente_fkey" FOREIGN KEY (id_cliente) REFERENCES public."Cliente"(id);


--
-- Name: Cuenta Cuenta_id_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Cuenta"
    ADD CONSTRAINT "Cuenta_id_cliente_fkey" FOREIGN KEY (id_cliente) REFERENCES public."Cliente"(id);


--
-- Name: Movimiento Movimiento_id_cuenta_fkey; Type: FK CONSTRAINT; Schema: public; Owner: banza
--

ALTER TABLE ONLY public."Movimiento"
    ADD CONSTRAINT "Movimiento_id_cuenta_fkey" FOREIGN KEY (id_cuenta) REFERENCES public."Cuenta"(id);


--
-- PostgreSQL database dump complete
--

