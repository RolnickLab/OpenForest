def pytest_addoption(parser):
    parser.addoption(
        "--dataset_name",
        action="append",
        default=[],
        help="list of dataset_names to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "dataset_name" in metafunc.fixturenames:
        metafunc.parametrize("dataset_name", metafunc.config.getoption("dataset_name"))
