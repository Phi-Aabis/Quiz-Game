import pytest
import sys
from unittest.mock import patch
import project


def test_selection():
    # valid cases
    args = ["project.py", "-d", "Easy", "-n", "5"]
    project.selection(args)

    args = ["project.py", "-n", "5", "-d", "Medium"]
    project.selection(args)

    # invalid difficulty
    args = ["project.py", "-d", "Impossible", "-n", "5"]
    with pytest.raises(SystemExit):
        project.selection(args)

    # invalid number range
    args = ["project.py", "-n", "999"]
    with pytest.raises(SystemExit):
        project.selection(args)


def test_questioning():
    project.SCORE = 0

    mock_question = {
        "question": "Q?",
        "options": ["A) 1", "B) 2", "C) 3", "D) 4"],
        "answer": "A"
    }

    # EASY (-d first) correct
    with patch("project.random.sample", return_value=[mock_question]), \
         patch("project.input", return_value="A"):

        project.sys.argv = ["project.py", "-d", "Easy", "-n", "1"]
        project.questioning()

    assert project.SCORE == 1

    # reset
    project.SCORE = 0

    # EASY (-d first) wrong
    with patch("project.random.sample", return_value=[mock_question]), \
         patch("project.input", return_value="B"):

        project.sys.argv = ["project.py", "-d", "Easy", "-n", "1"]
        project.questioning()

    assert project.SCORE == 0

    # reset
    project.SCORE = 0

    # EASY (-n first) correct
    with patch("project.random.sample", return_value=[mock_question]), \
         patch("project.input", return_value="A"):

        project.sys.argv = ["project.py", "-n", "1", "-d", "Easy"]
        project.questioning()

    assert project.SCORE == 1

    # reset
    project.SCORE = 0

    # MEDIUM path
    project.MediumQuestions = [mock_question]

    with patch("project.random.sample", return_value=[mock_question]), \
         patch("project.input", return_value="A"):

        project.sys.argv = ["project.py", "-d", "Medium", "-n", "1"]
        project.questioning()

    assert project.SCORE == 1

    # reset
    project.SCORE = 0

    # HARD path
    project.HardQuestions = [mock_question]

    with patch("project.random.sample", return_value=[mock_question]), \
         patch("project.input", return_value="A"):

        project.sys.argv = ["project.py", "-d", "Hard", "-n", "1"]
        project.questioning()

    assert project.SCORE == 1


def test_totalScore():
    # test -d format
    project.SCORE = 3
    project.sys.argv = ["project.py", "-d", "Easy", "-n", "5"]

    result = project.totalScore()
    assert result == "You scored 3 out of 5. "

    # test -n format
    project.SCORE = 2
    project.sys.argv = ["project.py", "-n", "4", "-d", "Easy"]

    result = project.totalScore()
    assert result == "You scored 2 out of 4. "
