import pytest
from models.thoughtmodel import ThoughtModel
from resources.thoughtprocess import ThoughtProcess
from app import db

# Serves as an "init" function
@pytest.fixture(autouse=True)
def thought_id():
    # Create new thought
    thought_id = 67

    return thought_id

def test_can_create_thought():
    ThoughtProcess.createThought('Test1', False)
    
    assert ThoughtModel.find_by_content('Test1')

def test_can_edit_thought(thought_id):
    # Edit thought contents
    ThoughtProcess.editThought(thought_id, 'Editted')
    check = ThoughtModel.find_by_id(thought_id)

    assert check.thought_content == 'Editted'

    # Mark as done
    ThoughtProcess.editThought(thought_id, is_done=True)
    check2 = ThoughtModel.find_by_id(thought_id)

    assert check2.is_done == True


def test_can_delete_thought(thought_id):
    toDelete = ThoughtModel.find_by_id(thought_id)
    ThoughtProcess.deleteThought(toDelete.thought_id)

    assert(ThoughtModel.find_by_id(thought_id)) is None