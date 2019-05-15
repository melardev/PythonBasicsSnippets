"""
**kwargs is used to let the caleld pass a variable number of key/value pairs as argument
You can use any name you want, for example instead of kwargs you can use **some_kwargs.
But you should prepend it with **
"""


def connect(**kwargs):
    user_info = {
        'first_name': kwargs.get('first_name', 'First name not set'),
        'last_name': kwargs.get('last_name', 'Last name not set'),
        'username': kwargs.get('username', 'Username not set'),
    }

    print(user_info)


connect()
connect(first_name='Melar', last_name='Dev', username='Melardev')
connect(first_name='Melar', last_name='Dev')
connect(first_name='Melar', last_name='Dev', middle_name='Not taken into account')
