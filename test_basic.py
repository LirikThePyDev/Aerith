import pytest
from aerith import execute_script

def test_let_and_print(tmp_path):
    # Create a temporary script file
    script_file = tmp_path / "test_script.aerith"
    script_file.write_text("let x = 42\nshout x")

    # Run the Aerith interpreter on the script
    execute_script(str(script_file))
    # Here you could capture stdout if needed to assert the output
    # For now, just making sure no exceptions are thrown
