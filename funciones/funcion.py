def server_sol(nombre, estado):
	servers[nombre]['libre'] = estado;

def client_res():
	for ser in servers:
		if(servers[ser]['libre']):
			return servers[ser]['host']

servers =	{
  "ser1": {"host": '196.203.201:3000', "libre": True  },
  "ser2": {"host": '196.203.201:4000', "libre": True  },
}
server_sol('ser1', False)

x = client_res()
print x
for ser in servers:
	print(servers[ser]);










