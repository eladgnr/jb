import pytest
from src.dal.vacations_dao import create_vacation, get_all_vacations
from src.dal.db_conn import get_connection
from decimal import Decimal
import datetime


def test_get_all_vacations():
    """Positive Test: Check if vacations are retrieved correctly."""
    print("Running positive test: test_get_all_vacations")

    # Reset the vacations table before running this test
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM vacations")  # Clear all existing data
    conn.commit()

    # Recreate sample data
    from src.dal.vacations_dao import create_vacations_table
    create_vacations_table()

    vacations = get_all_vacations()
    assert isinstance(vacations, list)
    assert len(vacations) > 0  # Should return pre-inserted data

    for vacation in vacations:
        assert len(vacation) == 7  # Ensure correct number of columns
        assert isinstance(vacation[0], int)  # vacation_id
        assert isinstance(vacation[1], int)  # country_id
        assert isinstance(vacation[2], str)  # description
        assert isinstance(vacation[3], (str, datetime.date))  # start_date
        assert isinstance(vacation[4], (str, datetime.date))  # end_date
        assert isinstance(vacation[5], (int, float, Decimal))  # price
        assert isinstance(vacation[6], str)  # image_name

    cur.close()
    conn.close()


def test_create_vacation():
    """Positive Test: Insert a vacation and verify it's added."""
    print("Running positive test: test_create_vacation")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM vacations")
    before_count = cur.fetchone()[0]
    cur.close()
    conn.close()

    new_vacation_id = create_vacation(
        2, 'Test Destination', '2025-06-01', '2025-06-10', 1500, 'test.png')
    assert new_vacation_id is not None
    assert isinstance(new_vacation_id, int)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM vacations")
    after_count = cur.fetchone()[0]
    cur.close()
    conn.close()

    assert after_count == before_count + 1


def test_create_vacation_invalid_data():
    """Negative Test: Insert vacation with invalid data and check for failure."""
    print("Running negative test: test_create_vacation_invalid_data")
    with pytest.raises(Exception):
        create_vacation(None, 'Invalid Date', 'Invalid Date',
                        'Invalid Price', 'Invalid Image')


def test_create_vacation_missing_fields():
    """Negative Test: Insert vacation with missing fields."""
    print("Running negative test: test_create_vacation_missing_fields")
    with pytest.raises(Exception):
        create_vacation(2, None, None, None, None)


def test_get_all_vacations_empty():
    """Negative Test: Ensure no vacations exist after table reset."""
    print("Running negative test: test_get_all_vacations_empty")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM vacations")
    conn.commit()
    cur.close()
    conn.close()

    vacations = get_all_vacations()
    assert vacations == []
