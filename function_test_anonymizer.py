from anonymize_csv import hash_field


def test_hash_field():
    field = "test string"
    same_value = "test string"
    hashed_field = hash_field(field)
    hashed_value = hash_field(same_value)

    assert hashed_field == hashed_value