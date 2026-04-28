import os
import pytest
from unittest.mock import patch, MagicMock
from src.sandbox import validar_archivo, crear_estructura_directorios, ejecutar_comando, CONFIG

# Mocking os.path.exists for file validation tests
@pytest.mark.parametrize("path,exists,isfile,expected", [
    ("exists.exe", True, True, True),
    ("missing.exe", False, False, False),
    ("directory/", True, False, False),
    ("", False, False, False),
])
def test_validar_archivo(path, exists, isfile, expected):
    with patch("os.path.exists", return_value=exists), \
         patch("os.path.isfile", return_value=isfile):
        assert validar_archivo(path) == expected

def test_crear_estructura_directorios(tmp_path):
    # Change working directory to a temp path for this test
    with patch("os.makedirs") as mock_makedirs, \
         patch("os.path.exists", return_value=False):
        crear_estructura_directorios()
        assert mock_makedirs.call_count >= 2
        # Verify it attempts to create 'results' and 'results/PDF'
        mock_makedirs.assert_any_call("results")
        mock_makedirs.assert_any_call("results/PDF")

@patch("subprocess.run")
@patch("os.chdir")
@patch("os.getcwd", return_value="/fake/dir")
def test_ejecutar_comando_success(mock_getcwd, mock_chdir, mock_run, tmp_path):
    # Setup mock subprocess result
    mock_res = MagicMock()
    mock_res.stdout = "Analysis results"
    mock_res.stderr = ""
    mock_run.return_value = mock_res
    
    # Mock open to avoid actual file writing
    with patch("builtins.open", MagicMock()):
        result = ejecutar_comando("mock_tool file.exe", "report.txt")
        
    assert result is True
    mock_run.assert_called_once()
    # Verify it uses shlex.split correctly
    args, kwargs = mock_run.call_args
    assert args[0] == ["mock_tool", "file.exe"]

@patch("subprocess.run")
def test_ejecutar_comando_timeout(mock_run):
    import subprocess
    mock_run.side_effect = subprocess.TimeoutExpired(cmd="test", timeout=300)
    
    with patch("os.chdir"), patch("os.getcwd", return_value="/fake/dir"):
        result = ejecutar_comando("slow_tool file.exe", "report.txt")
        
    assert result is False

def test_config_loading():
    assert "general" in CONFIG
    assert "tools" in CONFIG
    assert CONFIG["general"]["timeout_seconds"] == 300
    assert "manalyze" in CONFIG["tools"]
