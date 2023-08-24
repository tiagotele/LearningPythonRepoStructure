
from delete.delete import rm
import os
import mock

# Testing with real code
def test_delete() -> None:
    file_name="file.txt"
    with open(file_name, "w") as file:
        file.write("Some content")
    rm(file_name)
    assert False == os.path.exists(file_name)
    

# Testing with mock
@mock.patch('delete.delete.os')
def test_delete_with_mock(mock_os) -> None:
    file_name="file.txt"
    rm(file_name)
    mock_os.remove.assert_called_with(file_name)
    rm("arquivo.txt")
    mock_os.remove.assert_called_with("arquivo.txt")


@mock.patch('delete.delete.os')
@mock.patch('delete.delete.os.path')
def test_with_no_file(mock_os, mock_os_path):
    filename="any.txt"
    mock_os_path.isfile.return_value = False
    
    rm (filename)
    
    mock_os.remove.assert_not_called()