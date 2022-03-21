import sys

clients = ['Julio','David']


def create_clients(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    for index, client in enumerate(clients):
        print('{}: {}'.format(index, client))


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = client_name
    else:
        print('Client is not in clients list')

def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in clients list')

def search_client(client_name):
    global clients

    for client in client:
        if client != client_name:
            continue
        else:
            return True

def _get_cliente_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')
    
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


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
        client_name = _get_cliente_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_cliente_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_cliente_name()
        update_client_name = input("What is the updated cliend name? ")
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_cliente_name()
        find = search_client(client_name)
        
        if find:
            print('The client is in the clients list')
        else:
            print('The client: {} is not in our clients list'.format(client_name))

    else:
        print('Invalid command')