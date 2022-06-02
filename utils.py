from subprocess import Popen, PIPE, run


def run_script(proc, script):
    p = Popen([proc, '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(script)
    return stdout, stderr


def run_cmd(cmd, as_list=False):
    """ Runs a bash command.

    Args:
        cmd: A string that represents the command.
    Returns:
        stdout from bash command
    """

    return run(cmd.split()if not as_list else cmd, check=True, encoding='utf-8', capture_output=True).stdout
