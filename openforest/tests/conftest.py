def pytest_addoption(parser):
    parser.addoption(
        "--dataset_file",
        action="append",
        default=[],
        help="list of dataset_files to pass to test functions",
    )
    parser.addoption(
        "--dataset_name",
        action="append",
        default=[],
        help="list of dataset_names to pass to test functions",
    )

def pytest_generate_tests(metafunc):
    if "dataset_file" in metafunc.fixturenames:
        metafunc.parametrize("dataset_file", metafunc.config.getoption("dataset_file"))
    if "dataset_name" in metafunc.fixturenames:
        metafunc.parametrize("dataset_name", metafunc.config.getoption("dataset_name"))
