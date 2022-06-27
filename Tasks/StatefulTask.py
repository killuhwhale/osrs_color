from . import BaseTask as B


class StatefulTask(B.BaseTask):
    ctype = "StatefulTask"

    def __init__(self, client):
        super().__init__(client)


# if __name__ == "__main__":
#     r = RecipieTask()
#     print(r)
#     r.run()
