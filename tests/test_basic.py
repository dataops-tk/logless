from logless import logged, logged_block


@logged("test", success_detail="FOOBAR={result}")
def test_logged():
    return "FOOBAR"
