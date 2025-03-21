--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md53175bce1d3201d16594cebf9d7eb3f9d';






--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.20 (Debian 13.20-1.pgdg120+1)
-- Dumped by pg_dump version 13.20 (Debian 13.20-1.pgdg120+1)

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
-- PostgreSQL database dump complete
--

--
-- Database "oil_reports" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.20 (Debian 13.20-1.pgdg120+1)
-- Dumped by pg_dump version 13.20 (Debian 13.20-1.pgdg120+1)

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
-- Name: oil_reports; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE oil_reports WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE oil_reports OWNER TO postgres;

\connect oil_reports

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: spimex_trading_results; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spimex_trading_results (
    id_ integer NOT NULL,
    exchange_product_id character varying,
    exchange_product_name character varying,
    oil_id character varying,
    delivery_basis_id character varying,
    delivery_basis_name character varying,
    delivery_type_id character varying,
    volume integer,
    total double precision,
    count integer,
    date date,
    created_on date,
    updated_on date
);


ALTER TABLE public.spimex_trading_results OWNER TO postgres;

--
-- Name: spimex_trading_results_id__seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spimex_trading_results_id__seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.spimex_trading_results_id__seq OWNER TO postgres;

--
-- Name: spimex_trading_results_id__seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spimex_trading_results_id__seq OWNED BY public.spimex_trading_results.id_;


--
-- Name: spimex_traiding_results; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spimex_traiding_results (
    id_ integer NOT NULL,
    exchange_product_id character varying,
    exchange_product_name character varying,
    oil_id character varying,
    delivery_basis_id character varying,
    delivery_basis_name character varying,
    delivery_type_id character varying,
    volume integer,
    total double precision,
    count integer,
    date date,
    created_on date,
    updated_on date
);


ALTER TABLE public.spimex_traiding_results OWNER TO postgres;

--
-- Name: spimex_traiding_results_id__seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spimex_traiding_results_id__seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.spimex_traiding_results_id__seq OWNER TO postgres;

--
-- Name: spimex_traiding_results_id__seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spimex_traiding_results_id__seq OWNED BY public.spimex_traiding_results.id_;


--
-- Name: spimex_trading_results id_; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spimex_trading_results ALTER COLUMN id_ SET DEFAULT nextval('public.spimex_trading_results_id__seq'::regclass);


--
-- Name: spimex_traiding_results id_; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spimex_traiding_results ALTER COLUMN id_ SET DEFAULT nextval('public.spimex_traiding_results_id__seq'::regclass);


--
-- Data for Name: spimex_trading_results; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spimex_trading_results (id_, exchange_product_id, exchange_product_name, oil_id, delivery_basis_id, delivery_basis_name, delivery_type_id, volume, total, count, date, created_on, updated_on) FROM stdin;
1	P1	Product 1	OIL1	B1	Basis 1	D1	100	1000.5	10	2024-01-01	2024-01-02	2024-01-03
2	P2	Product 2	OIL2	B2	Basis 2	D2	200	2000.5	20	2024-01-05	2024-01-06	2024-01-07
\.


--
-- Data for Name: spimex_traiding_results; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.spimex_traiding_results (id_, exchange_product_id, exchange_product_name, oil_id, delivery_basis_id, delivery_basis_name, delivery_type_id, volume, total, count, date, created_on, updated_on) FROM stdin;
\.


--
-- Name: spimex_trading_results_id__seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.spimex_trading_results_id__seq', 1, false);


--
-- Name: spimex_traiding_results_id__seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.spimex_traiding_results_id__seq', 46001, true);


--
-- Name: spimex_trading_results spimex_trading_results_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spimex_trading_results
    ADD CONSTRAINT spimex_trading_results_pkey PRIMARY KEY (id_);


--
-- Name: spimex_traiding_results spimex_traiding_results_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spimex_traiding_results
    ADD CONSTRAINT spimex_traiding_results_pkey PRIMARY KEY (id_);


--
-- PostgreSQL database dump complete
--

--
-- Database "oil_reports_test" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.20 (Debian 13.20-1.pgdg120+1)
-- Dumped by pg_dump version 13.20 (Debian 13.20-1.pgdg120+1)

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
-- Name: oil_reports_test; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE oil_reports_test WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE oil_reports_test OWNER TO postgres;

\connect oil_reports_test

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
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.20 (Debian 13.20-1.pgdg120+1)
-- Dumped by pg_dump version 13.20 (Debian 13.20-1.pgdg120+1)

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
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

