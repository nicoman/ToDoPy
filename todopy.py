class Task(object):
    """ A class to generate Task """
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return self.title


class TaskList(object):
    """ A class to list Task """

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.tasks)

    def add(self, x):
        self.tasks.append(x)
