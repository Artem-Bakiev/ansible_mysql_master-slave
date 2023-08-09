# ansible_mysql

Installs and configures MySQL server on Ubuntu servers. Also this role can configure the databases for master-slave replication

# Requirements

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes

# Role variables

Available variables are listed in vars/main.yml file, and for master-slave configuration you have master_server_ip variable in defaults/main.yml
Also you can use -e(--extra-vars) flag to create databases, create users in the database and set the password for this user(only for main database)

# Usage

1. Generate inventory file from config.toml: Run python3 generate_inventory.py
2. For mysql server installation run: ansible-playbook mysql.yml -i inventory
3. If you want to create new database, users and set password for this user run: ansible-playbook mysql.yml -i inventory -e "db_name=dev db_user=dev db_pass=passs"
4. If you want to configure master-slave replication you need to run: ansible-playbook mysql.yml -i inventory -e "master_slave_install=true"
