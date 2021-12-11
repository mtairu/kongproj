CREATE USER fastapi IDENTIFIED WITH mysql_native_password BY 'x2VUdt0N';
GRANT ALL PRIVILEGES ON sample_bls_db.* to fastapi;
FLUSH PRIVILEGES;

