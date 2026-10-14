import subprocess
import  sys

program=sys.argv[1]
# arguments, expected status, expected stdout, expected stderr fragment
cases = [
    (["count", "ERROR"], 0, "count=3\n", ""),
    (["count", "INFO"], 0, "count=1\n", ""),
    (["count", "WARN"], 0, "count=1\n", ""),
    ([], 1, "", "usage"),
    (["count"], 1, "", "usage"),
    (["unknown", "ERROR"], 1, "", "unsupported command"),
    (["count", "DEBUG"], 1, "", "unsupported level"),
    (["count", "ERROR", "extra"], 1, "", "usage"),
]
for args,expected_code,expected_stdout,expected_error in cases:
    completed=subprocess.run([program]+args , capture_output=True,text=True,timeout=5,)
    if expected_error:
        stderr_ok = expected_error in completed.stderr
    else:
        stderr_ok = completed.stderr == ""

    if (completed.returncode != expected_code or completed.stdout != expected_stdout or not stderr_ok):
        print("Failed arguments:", args)
        print("Expected exit status:", expected_code)
        print("Actual exit status:", completed.returncode)
        print("Expected stdout:", repr(expected_stdout))
        print("Actual stdout:", repr(completed.stdout))
        print("Expected stderr fragment:", repr(expected_error))
        print("Actual stderr:", repr(completed.stderr))
        sys.exit(1)
print("All test cases worked")

