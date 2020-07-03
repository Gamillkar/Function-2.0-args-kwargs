class Contact():
    def __init__(self, name, surname, numbers, favorite_contact=False, *args, **kwargs):
        self.name = name
        self.surname= surname
        self.numbers = numbers
        self.args = args
        self.kwargs = kwargs
        self.favorite_contact = favorite_contact
        if favorite_contact is False:
            self.favorite_contact = 'нет'
        self.data = f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон:{self.numbers}\n' \
                    f'В избранных: {self.favorite_contact}\nДополнительная информация:\n\t{self.kwarg_converting()}\n\t{self.args_converting()}\n'

    def kwarg_converting(self):
        list_kwargs = []
        for webcity, email in self.kwargs.items():
            local_data = f'{webcity} : {email}'
            list_kwargs.append(local_data)
        property_string_kwargs = '\n\t'.join(list_kwargs)
        return property_string_kwargs

    def args_converting(self):
        list_args = self.args
        str_args = '\n\t'.join(list_args)
        return str_args


    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data


class PhoneBook(Contact):

    def __init__(self, name_phonebook):
        self.name_phonebook = name_phonebook
        self.list_contact = []

    def print_contact(self):
        '''Вывод контактов из телефонной книги'''
        for contact in self.list_contact:
            print(f'{contact}\n')

    def add_contact(self, name):
        '''Добавление нового контакта'''
        self.list_contact.append(name)

    def del_contact(self, number_telephon):
        '''Удаление контакта по номеру телефона'''
        for user in self.list_contact:
            if number_telephon in user.data:
                self.list_contact.remove(user)

    def search_contact_number(self):
        '''Поиск всех избранных номеров'''
        for user in self.list_contact:
            if 'нет' not in user.favorite_contact :
                print(f'В избранных телефонной книги: {user.favorite_contact}')

    def search_contact_name(self, name, surname):
        '''Поиск контакта по имени и фамилии'''
        for user in self.list_contact:
            if name and surname in user.data:
                print(user.data)



if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    semion = Contact('Semion', 'Georgievich', '+77777777', 'jhon', '+4141141', 'Заметка-позвонить Коле', telegram='@sema')
    my_phone_book = PhoneBook('my_tel_book')
    my_phone_book.add_contact(jhon)
    my_phone_book.add_contact(semion)
    # my_phone_book.del_contact('+71234567809')
    # my_phone_book.print_contact()
    my_phone_book.search_contact_name('Jhon','Smith')






