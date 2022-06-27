from . import BaseTask as B


class RecipieTask(B.BaseTask):
    ctype = "RecipieTask"

    def __init__(self, client):
        super().__init__(client)


# if __name__ == "__main__":
#     r = RecipieTask()
#     print(r)
#     r.run()
