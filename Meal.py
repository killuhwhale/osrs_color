from tasks import BaseTask as B
from typing import List


class Meal:
    ''' Manages Mutliple Tasks.

    To be used in the cookbook, meal.run() -> currentRecipie.currentTask.run()

    '''

    def __init__(self, tasks: List[B.BaseTask]):
        self.tasks = tasks
        self.current_task = 0

    def run(self):
        task = self.tasks[self.current_task]
        if task.should_exit:
            self.current_task += 1
            self.current_task %= len(self.tasks)
            task.should_exit = False
            task = self.tasks[self.current_task]

        task.run()
