import pytest
from src.operation import show_all , tasks

def test_show_all(capsys : pytest.CaptureFixture[str]): #capsys fixture - stdout/stderr output ကို capture လုပ်ဖို့ pytest feature
    global tasks 
    tasks = {}
    show_all()
    sysout = capsys.readouterr()
    assert sysout.out == "Task List\n------------------------\nThere is no tasks\n------------------------\n"
