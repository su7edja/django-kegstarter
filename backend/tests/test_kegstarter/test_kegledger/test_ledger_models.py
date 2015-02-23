import pytest

from django.core.exceptions import ValidationError

from . import factories
from .. import django_factories


@pytest.mark.django_db
def test_ledger_total():
    ledger = factories.LedgerFactory()
    entry_a = factories.LedgerEntryFactoryGuest(ledger=ledger)
    entry_b = factories.LedgerEntryFactoryGuest(ledger=ledger)
    assert ledger.total == entry_a.amount + entry_b.amount


@pytest.mark.django_db
def test_ledger_entry_from_registered_user_cannot_have_guest_name():
    with pytest.raises(ValidationError):
        factories.LedgerEntryFactoryRegistered(guest_name='definitely a name')


@pytest.mark.django_db
def test_ledger_entry_from_guest_user_cannot_have_user_fk():
    with pytest.raises(ValidationError):
        factories.LedgerEntryFactoryGuest(user=django_factories.UserFactory())


@pytest.mark.django_db
def test_ledger_entry_must_have_either_user_fk_or_guest_name():
    with pytest.raises(ValidationError):
        factories.LedgerEntryFactoryGuest(user=None, guest_name='')
