import datetime

def log_path(file):
    def get_logo(old_function):
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            resalt = old_function(*args, **kwargs)
            with open(file, 'a', encoding='utf-8') as f:
                f.write(f'{start}  {old_function.__name__} {resalt}\n')
            return resalt
        return new_function
    return get_logo