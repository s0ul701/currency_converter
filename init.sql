CREATE DATABASE postgres_db;
CREATE USER postgres_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE "postgres_db" to postgres_user;