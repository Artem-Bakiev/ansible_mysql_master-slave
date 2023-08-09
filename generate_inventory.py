from jinja2 import Template
import toml

# Load data from config.toml
with open('config.toml', 'r') as f:
    config_data = toml.load(f)

# Jinja2 template for inventory
inventory_template = Template(
'''[{{ server_group }}-1_srv_main]
{{ server_group }}-1  ansible_ssh_host=root@{{ server_ip }} 

{% if slaves %}
[{{ server_group }}-1_srv_slave]
{% for index, slave in slaves.items() %}
{{ server_group }}-1-slave-{{ index +1 }} server_id={{ index +2 }} ansible_ssh_host=root@{{ slave }}
{% endfor %}
{% endif %}
''')

# Render the template with the config data
inventory_content = inventory_template.render(
        server_group=config_data['sites']['testpartner']['server_group'],
        server_ip=config_data['sites']['testpartner']['db']['host'],
        slaves=dict(enumerate(config_data['sites']['testpartner']['db']['slaves'])),
        mysql_user=config_data['sites']['testpartner']['db']['user'],
        mysql_password=config_data['sites']['testpartner']['db']['password'],
        mysql_base=config_data['sites']['testpartner']['db']['base'],
        )

# Write the inventory content to a file
with open('inventory', 'w') as f:
    f.write(inventory_content)
