# Zabbix installation with POstgreSQL

Installation with PostgreSQL + TimescaleDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install Zabbix 5.0 on CentOS8 with PostgreSQL + TimescaleDB follow the steps
below:

- Add PostgreSQL repository to our CentOS8
- Disable actual postgresql module on CentOS8
- Install postgresql12 and postgresql12-server
- Start initdb

First add the repo and disable the old postgresql modules.


- `dnf install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
  dnf -qy module disable postgresql


Now install PostgreSQL 12, start initdb and enable postgresql service:


.. code-block:: bash


  dnf -y install postgresql12 postgresql12-server
  /usr/pgsql-12/bin/postgresql-12-setup initdb
  systemctl enable --now postgresql-12.service

To ensure PostgreSQL work the right way, some changes has to be made under
``/var/lib/pgsql/12/data/pg_hba.conf``. Scroll until the ende and made the
following changes:


.. code-block:: bash

  vim /var/lib/pgsql/12/data/pg_hba.conf

  ....

  # TYPE  DATABASE        USER            ADDRESS                 METHOD

  # "local" is for Unix domain socket connections only
  local   all             all                                     peer
  # IPv4 local connections:
  host    all             all             127.0.0.1/32            md5
  # IPv6 local connections:
  host    all             all             ::1/128                 md5
  # Allow replication connections from localhost, by a user with the
  # replication privilege.
  local   replication     all                                     md5
  host    replication     all             127.0.0.1/32            md5
  host    replication     all             ::1/128                 md5


Add TimescaleDB repository to the CentOS 8, update the system and install
timescale-postgresql-12:


.. code-block:: bash


  tee /etc/yum.repos.d/timescale_timescaledb.repo << EOL
  [timescale_timescaledb]
  name=timescale_timescaledb
  baseurl=https://packagecloud.io/timescale/timescaledb/el/8/\$basearch
  repo_gpgcheck=1
  gpgcheck=0
  enabled=1
  gpgkey=https://packagecloud.io/timescale/timescaledb/gpgkey
  sslverify=1
  sslcacert=/etc/pki/tls/certs/ca-bundle.crt
  metadata_expire=300
  EOL

  ...

  dnf update
  dnf -y install timescaledb-postgresql-12

Optimize PostgreSQL configuration parameters:

.. code-block:: bash

  timescaledb-tune --pg-config=/usr/pgsql-12/bin/pg_config
  systemctl restart postgresql-12.service


Add the Zabbix Repo to the CentOS 8 and install Zabbix 5.0:


.. code-block:: bash


  rpm -Uvh https://repo.zabbix.com/zabbix/5.0/rhel/8/x86_64/zabbix-release-5.0-1.el8.noarch.rpm
  dnf clean all
  dnf install zabbix-server-pgsql zabbix-web-pgsql zabbix-apache-conf zabbix-agent


Create the postgresql initial database:

.. code-block:: bash

  sudo -u postgres createuser --pwprompt zabbix
  sudo -u postgres createdb -O zabbix -E Unicode -T template0 zabbix

Import initial schema and data:

.. code-block:: bash

  zcat /usr/share/doc/zabbix-server-pgsql*/create.sql.gz | sudo -u zabbix psql zabbix

Configure Zabbix-Server to connect with PostgreSQL:

.. code-block:: bash

  vim /etc/zabbix/zabbix_server.conf

  ...

  DBPassword=password


Configure PHP for Zabbix frontend uncommenting and setting the right timezone:

.. code-block:: bash

  vim /etc/php-fpm.d/zabbix.conf

  ...

  ; php_value[date.timezone] = Europe/Riga


Restart and enable all services:


.. code-block:: bash

  systemctl restart zabbix-server zabbix-agent httpd php-fpm postgresql-12.service
  systemctl enable zabbix-server zabbix-agent httpd php-fpm


TimescaleDB:

.. code-block:: bash


  echo "CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;" | sudo -u postgres psql zabbix
  zcat /usr/share/doc/zabbix-server-pgsql/timescaledb.sql.gz | sudo -u zabbix psql zabbix

Zabbix needs to be configured via the web frontend before it can be used.
Navigate to **http://<hostname>/zabbix** and click your way through the setup.

