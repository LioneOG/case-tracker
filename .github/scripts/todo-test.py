import sys
import unittest

from todo import CaseBoard, CaseTask


class TestCaseBoard(unittest.TestCase):

    def setUp(self):
        self.board = CaseBoard()

    def test_add_task(self):
        self.board.add_task(CaseTask("Request bank records"))
        self.assertEqual(len(self.board.tasks), 1)
        self.assertEqual(self.board.tasks[0].status, "ToDo")

    def test_mark_completed(self):
        task = CaseTask("Photograph the evidence")
        task.mark_completed()
        self.assertTrue(task.completed)
        self.assertEqual(task.status, "Done")

    def test_get_open_tasks(self):
        self.board.populate()
        open_tasks = self.board.get_open_tasks()
        expected = sum(1 for _, done in CaseBoard.SAMPLE_TASKS if not done)
        self.assertEqual(len(open_tasks), expected)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self):
        self.board.populate()
        done_tasks = self.board.get_done_tasks()
        expected = sum(1 for _, done in CaseBoard.SAMPLE_TASKS if done)
        self.assertEqual(len(done_tasks), expected)
        self.assertTrue(all(task.completed for task in done_tasks))

    def test_no_task_is_lost(self):
        self.board.populate()
        total = len(self.board.get_open_tasks()) + len(self.board.get_done_tasks())
        self.assertEqual(total, len(CaseBoard.SAMPLE_TASKS))


if __name__ == "__main__":
    tests = unittest.TestLoader().loadTestsFromTestCase(TestCaseBoard)
    passed = 0
    for test in tests:
        result = unittest.TestResult()
        test.run(result)
        ok = result.wasSuccessful()
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {test._testMethodName}")

    total = tests.countTestCases()
    print(f"\n{passed}/{total} tests passed")
    sys.exit(0 if passed == total else 1)