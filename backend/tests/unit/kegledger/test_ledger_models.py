from django.core.exceptions import ValidationError
import pytest

from ...factories.django_factories import UserFactory
from ...factories.kegledger.ledger_factories import (
    LedgerFactory, LedgerEntryFactoryGuest, LedgerEntryFactoryRegistered)


@pytest.mark.django_db
def test_ledger_total():
    ledger = LedgerFactory()
    entry_a = LedgerEntryFactoryGuest(ledger=ledger)
    entry_b = LedgerEntryFactoryGuest(ledger=ledger)
    assert ledger.total == entry_a.amount + entry_b.amount


@pytest.mark.django_db
def test_ledger_entry_from_registered_user_cannot_have_guest_name():
    with pytest.raises(ValidationError):
        LedgerEntryFactoryRegistered(guest_name='definitely a name')


@pytest.mark.django_db
def test_ledger_entry_from_guest_user_cannot_have_user_fk():
    with pytest.raises(ValidationError):
        LedgerEntryFactoryGuest(user=UserFactory())


@pytest.mark.django_db
def test_ledger_entry_must_have_either_user_fk_or_guest_name():
    with pytest.raises(ValidationError):
        LedgerEntryFactoryGuest(user=None, guest_name='')
