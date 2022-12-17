def read_saves(list, file_path):
    """
    Read saves from file
    :param list: list which contains saves
    :param file_path: path to file in which saves are contained
    :return: list
    """
    f = open(file_path, "r+")
    list.clear()
    for i in range(9):
        list.append(f.readline().replace('\n',''))

class key:
    def __init__(self, key, previous_action: int, current_action: int):
        """
        Create an object
        :param key: Key bind
        :param previous_action: 1 if in previous cycle key was pressed, else 0
        :param current_action: 1 if in current cycle key was pressed, else 0
        """
        self.key = key
        self.previous_action = previous_action
        self.current_action = current_action

    def on_press(self):
        """
        Checks if key was pressed
        :return: bool
        """
        if self.previous_action == 0 and self.current_action == 1:
            return True
        else:
            return False

    def on_release(self):
        """
        Checks if key was released
        :return: bool
        """
        if self.previous_action == 1 and self.current_action == 0:
            return True
        else:
            return False

