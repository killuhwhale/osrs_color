from collections import defaultdict
from time import sleep, time


'''
TODO
Implement Meal


Meal
- Run multiple recipes for a client
    - each recipe has a should_exit flag,
    when true, meal will call next recipe in the list for that client.




Validators

- Recipe and Stateful 
- setup parsing in base class _v_
- If given, this will return true or fasle to move on to the next step in a recipie


Stateful tasks Class example....

Simple splash bot magic 


'''


class SleepCycle:
    def __init__(self):
        self.start = 0.0
        self.dur = 0.0

    def set(self, start, dur):
        self.start = start
        self.dur = dur

    def is_ready(self) -> bool:
        return time() - self.start >= self.dur

    def remaining(self) -> float:
        return time() - self.start

    def __str__(self):
        return f"Curent duration{time() - self.start}, waiting until: {self.dur}"


class BaseTask:
    def __init__(self, client):
        self.client = client
        self._sleep = SleepCycle()
        self._step = 0
        # parse subclass for all methods if ctype==recipie
        # Strings of each funtion, not in order.
        self.recipie = self._parse_recipies()
        self.sleeps = self._parse_sleep()
        self.valids = self._parse_validators()
        self.should_exit = False  # Lets meal know when to exit

    def is_recipie(self):
        return self.ctype == "RecipieTask"

    def is_stateful(self):
        return self.ctype == "StatefulTask"

    def _run_recipie(self):
        is_running = True
        if self.should_exit:
            print("Should exit set, need to run next recipe in the meal list.")
            return

        if self._step == len(self.recipie):
            self._step = 0

        if self._step > 0:
            # We have at least ran the first step, validate it
            is_valid = self.valids[self._step - 1](self, self.client)
            done_sleeping = self._sleep.is_ready()
            if is_valid is None:
                self.should_exit = True
                return

            if is_valid and done_sleeping:
                print(
                    f"\nRunning ({self._step}): {self.recipie[self._step]}\n")
                # Do the step for the client,
                self.recipie[self._step](self, self.client)

                # Update the sleep time, call lambda function to generate random sleep val
                dur = self.sleeps[self._step](self, is_running)
                self._sleep.set(time(), dur)
                self._step += 1  # Update the clients current step.

            elif done_sleeping and not is_valid:
                print(
                    f"Repeating ({self._step -1}): (current step: {self._step})")
                self.recipie[self._step - 1](self, self.client)

            elif not done_sleeping and is_valid:

                print(
                    f"Sleeping while valid ({self.recipie[self._step - 1]}) Remaining: {self._sleep.remaining()}\n")

            else:
                print(
                    f"Not valid yet and still sleeping: {self.recipie[self._step] - 1}  Remaining: {self._sleep.remaining()}\n")

        elif self._sleep.is_ready() and self.valids[self._step](self, self.client):
            print(f"Running 1st step: {self.recipie[self._step]}\n")
            self.recipie[self._step](self, self.client)
            dur = self.sleeps[self._step](self, is_running)
            self._sleep.set(time(), dur)
            self._step += 1

        print("Task check complete...")

    def check_state(self):
        pass

    def _run_stateful(self):
        self.check_state()

    def run(self):
        # print("Running task")
        if self.is_recipie():
            self._run_recipie()
        elif self.is_stateful():
            self._run_stateful()

    def _parse_class_methods(self, fn_type):
        method_list = []

        for func in dir(self.__class__):
            fn = getattr(self.__class__, func)
            if func.startswith(fn_type):
                method_list.append((fn, fn.__code__.co_firstlineno))

        method_list = sorted(method_list, key=lambda tp: tp[1])
        # Extract just the name of the fn after sorting
        method_list = [tp[0] for tp in method_list]
        return method_list

    def _parse_recipies(self):
        return self._parse_class_methods("_r_")

    def _parse_sleep(self):
        return self._parse_class_methods("_s_")

    def _parse_validators(self):
        return self._parse_class_methods("_v_")

    '''
        This class will provide functionality to run a task.


        run 

        get_queue 


        when I use this as a base class, I want to parse the child class for all methods starting with
        
            - r_ and s_ if its a Recipie Class

        If its a State Class 
            - check_state

        Therefore, If I write a child class and use this as a base class,
        I can write all my recipies its its own class.

        With both Multiple Types of classes, the base class will know how to run "the next step"

        Then, I can just have a list of classes to correspond to each client, just like the cookbook idea.

        So, I can just pass the client in the class.run() method.

        This method will then, depending on the class type, run the correct "next step"



        TODO:
        Move cook book, steps, and sleep functionlity from botloop to this class.

        The Recipie Class will not do it own state keeping per class because:
            - The recipie is determined up a list of functions and there is no need to copy this functionlity in each class.
            - The base class can determine how many steps there are and keep track of which step to run next.


        The State Class will do its own state keeping per class because:
            - Each one will be different and will check its state and do a corresponding action if it needs to.
            - This means there are no steps to keep track of.


        Create  StatefulTask class that extends(BaseTask)
        Create  RecipeTask class that extends(BaseTask)

        Then the base class will know isinstance of Recipie or Stateful Task

        

    '''
