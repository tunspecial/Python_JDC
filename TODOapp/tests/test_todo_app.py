import pytest
import src.operation
# from src.operation import show_all , tasks

def test_show_all_notask(capsys : pytest.CaptureFixture[str]): #capsys fixture - stdout/stderr output ကို capture လုပ်ဖို့ pytest feature
    src.operation.tasks = {}
    src.operation.show_all()
    sysout = capsys.readouterr()
    assert sysout.out == "Task List\n------------------------\nThere is no tasks\n------------------------\n"


def test_show_all_withtask(capsys : pytest.CaptureFixture[str]):
    src.operation.tasks = {1 : "Hello"}
    src.operation.show_all()
    sysout = capsys.readouterr()
    assert sysout.out == "Task List\n------------------------\n1.Hello\n------------------------\n"
    
