class Task(object):
    """ A class to generate Task """
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return self.title


class TaskList(object):
    """ A class to list Task """
    #lista_metod = []
    def __init__(self, tasks):
        self.tasks = tasks
