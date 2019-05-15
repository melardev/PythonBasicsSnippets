def func(name=None):
    if name is None or name == "":
        print("Your name is unknown")
        return
    print("Your name is ", name)


func()
func('Melardev')
func(name='Melardev')
