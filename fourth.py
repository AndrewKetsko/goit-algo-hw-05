contacts={}

def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return 'Give me name and phone please.'
        except KeyError:
            return 'Give me actual name please.'
        except IndexError:
            return 'Give me name please.'
    return inner        

def parse_input(command):
    cmd,*args = command.split()
    cmd=cmd.strip()
    return cmd,args

@input_error
def add_contact(args):
    name,phone=args
    contacts[name]=phone
    return('contact added')

@input_error
def change_contact(args):
    name,phone=args
    contacts[name]=phone
    return('contact changed')

@input_error
def show_phone(args):
    return(f'{args[0]}:{contacts[args[0]]}')

def show_all():
    list=''
    for key, value in contacts.items():
        list+=f'{key}:{value}\n'
    return list

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()
        command,args=parse_input(command)

        match(command):
            case('close'):
                print("Good bye!")
                break  
            case('exit'):
                print("Good bye!")
                break 

            case('hello'):
                print("How can I help you?")

            case('add'):
                print(add_contact(args))

            case('change'):
                print(change_contact(args))

            case('phone'):
                print(show_phone(args))

            case('all'):
                print(show_all())

            case(_):
                print("Invalid command.")


if __name__ == "__main__":
    main()