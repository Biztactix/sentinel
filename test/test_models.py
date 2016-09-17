import pytest
import os
import sys
sys.path.append( os.path.join( os.path.dirname(__file__), '..', 'lib' ) )

# setup/teardown?

# Proposal model
@pytest.fixture
def proposal():
    from models import Proposal
    return Proposal()

def test_proposal(proposal):
    d = proposal.get_dict()
    assert type(d) == type({})

    fields = [
        'name',
        'url',
        'start_epoch',
        'end_epoch',
        'payment_address',
        'payment_amount',
    ]
    fields.sort()
    sorted_keys = d.keys()
    sorted_keys.sort()
    assert sorted_keys == fields


# GovernanceObject model
@pytest.fixture
def governance_object():
    from models import GovernanceObject
    return GovernanceObject()

def test_governance_object(governance_object):
    d = governance_object.get_dict()
    assert type(d) == type({})

    fields = [
        'parent_id',
        'object_creation_time',
        'object_hash',
        'object_parent_hash',
        'object_type',
        'object_revision',
        'object_fee_tx',
        'yes_count',
        'no_count',
        'abstain_count',
        'absolute_yes_count',
    ]

    fields.sort()
    sorted_keys = d.keys()
    sorted_keys.sort()
    assert sorted_keys == fields
