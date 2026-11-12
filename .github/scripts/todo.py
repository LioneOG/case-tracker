class CaseTask:
    """One investigation task on the case board."""

    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status
        self.completed = False

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"CaseTask({self.title!r}, {self.status!r})"

    def __str__(self):
        marker = "x" if self.completed else " "
        return f"[{marker}] {self.title}"


class CaseBoard:
    """Holds every task for the case and filters them by status."""

    SAMPLE_TASKS = [
        ("Secure the crime scene", True),
        ("Collect CCTV footage", True),
        ("Interview the first witness", True),
        ("Image the suspect's laptop", True),
        ("Analyse phone records", True),
        ("Write the forensic report", False),
    ]

    def __init__(self):
        self.tasks = []

    def populate(self):
        for title, done in self.SAMPLE_TASKS:
            task = CaseTask(title)
            if done:
                task.mark_completed()
            self.add_task(task)

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    board = CaseBoard()
    board.populate()

    print("Open tasks:")
    for task in board.get_open_tasks():
        print(f"  {task}")

    print("\nClosed tasks:")
    for task in board.get_done_tasks():
        print(f"  {task}")


if __name__ == "__main__":
    main()