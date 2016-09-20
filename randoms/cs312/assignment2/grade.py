import os
import re
import subprocess
import tempfile
import difflib

SUBMISSIONS = "./submissions/"
SOLUTION_PATH = "./tower.txt"


def file_input(filename):
    result = ""
    with open(filename) as file_obj:
        result = file_obj.read()
    return result


def grade(submission_filename, solution_output):
    submission_text = file_input(os.path.join(SUBMISSIONS, submission_filename))

    with open(os.path.join("tmp", "Tower.java"), "w+") as tower:
        tower.write(submission_text)

    compile_message = subprocess.check_output(
            "javac tmp/Tower.java", shell=True).decode("utf-8")
    stdout = subprocess.check_output(
            "java -cp tmp Tower", shell=True).decode("utf-8").rstrip()

    name = re.search(r"([a-z]*)_", submission_filename).group(1)
    diff = difflib.unified_diff(
            stdout.splitlines(stdout.count("\n")),
            solution_output.splitlines(solution_output.count("\n")),
            fromfile="student", tofile="solution")
    diff_str = "".join(diff)

    if diff_str:
        with open(os.path.join(os.getcwd(), "out", name + ".txt"), "w+") as diff_file:
            diff_file.write(diff_str)
    else:
        print(name)


if __name__ == "__main__":
    # Create a tmp directory to put all submissions in.
    if "tmp" not in os.listdir(os.getcwd()):
        os.mkdir(os.path.join(os.getcwd(), "tmp"))

    if "out" not in os.listdir(os.getcwd()):
        os.mkdir(os.path.join(os.getcwd(), "out"))

    # Get solution output.
    solution_output = file_input(SOLUTION_PATH).rstrip()

    # Iterate and grade.
    for submission_filename in os.listdir(SUBMISSIONS):
        grade(submission_filename, solution_output)
