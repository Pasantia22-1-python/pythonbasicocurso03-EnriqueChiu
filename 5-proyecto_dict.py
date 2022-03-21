from pydoc import cli
import sys

clients = [
    {
        'name': 'Julio',
        'company': 'Google',
        'email': 'enriquechiu12@google.com',
        'position': 'software enginner',
    },
    {
        'name': 'David',
        'company': 'Facebook',
        'email': 'david@facebook.com',
        'position': 'data enginner',
    }
]


def create_clients(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    for index, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = index,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'],
        ))


def update_client(client_name, update_client):
    global clients

    flag = False

    for index, client in enumerate(clients):
        if client['name'] == client_name:
            clients[index] = update_client
            flag = True

    if (not flag):
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    flag = False

    for index, client in enumerate(clients):
        if client['name'] == client_name:
            del clients[index]
            flag = True
        
    if not flag:
        print('Client is not in clients list')

def search_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

    if not client_name:
        sys.exit()

    return client_name

def _get_cliente_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}? '.format(field_name))

        if field == 'exit':
            field = None
            break

    if not field:
        sys.exit()
    
    return field

def _print_welcome():
    print('WELCOME TO CIANCODERS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')



if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_cliente_field('name'),
            'company': _get_cliente_field('company'),
            'email': _get_cliente_field('email'),
            'position': _get_cliente_field('position'),
        }
        create_clients(client)
        list_clients()
    elif command == 'D':
        client_name= _get_cliente_field('name')
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name= _get_cliente_field('name')
        client = {
            'name': _get_cliente_field('new name'),
            'company': _get_cliente_field('new company'),
            'email': _get_cliente_field('new email'),
            'position': _get_cliente_field('new position'),
        }
        update_client(client_name, client)
        list_clients()
    elif command == 'S':
        client_name = _get_cliente_field('name')
        find = search_client(client_name)
        
        if find:
            print('The client is in the clients list')
        else:
            print('The client: {} is not in our clients list'.format(client_name))

    else:
        print('Invalid command')