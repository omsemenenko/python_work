def cars(name, title, **kwargs):
    kwargs['factory'] = name
    kwargs['model'] = title
    return kwargs

make_car = cars('mitsubish', 'outlander', color='grey', tow_package=True)
print(make_car)