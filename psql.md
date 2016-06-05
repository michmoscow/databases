# installing

apt-get install postgresql

```
Creating new cluster 9.3/main ...
  config /etc/postgresql/9.3/main
  data   /var/lib/postgresql/9.3/main
  locale en_US.UTF-8
  port   5432
```

https://help.ubuntu.com/community/PostgreSQL








## Not needed?

sudo -u postgres psql postgres   - connecting to postgres db as postgres user

\password postgres              - setting pwd for postgres db

sudo -u postgres createdb mydb


## Alternative Server Setup!!!
```
sudo -u postgres createuser --superuser $USER            (leonid). making leonid superuser
sudo -u postgres psql
\password leonid
12345
sudo -u postgres createdb $USER    - connecting to leonid should be without pwd
then psql - connecting to leonid database
```

* uncommented line in /etc/hosts with localhost
## PSQL

* \q exit
* \l список бд
* \dt - список всех таблиц
* \d table - структура таблицы table
* \dt+ - список всех таблиц с описанием
* \? - help по psql




