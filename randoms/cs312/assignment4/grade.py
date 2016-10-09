import os
import re
import subprocess
import difflib


JAVA_FILE = "RockPaperScissors"
SUBMISSIONS = os.path.join(os.getcwd(), "submissions")
TESTS = os.path.join(os.getcwd(), "tests")
TMP = os.path.join(os.getcwd(), "tmp")
SUMMARY = os.path.join(os.getcwd(), "summary")


def file_input(filename, strip=True):
    result = ""
    with open(filename) as file_obj:
        result = file_obj.read()
    if strip:
        return result.rstrip()
    return result


def get_basename_no_extension(filename):
    return os.path.splitext(os.path.basename(filename))[-2]


def grade(submission_filename, test_in_out):
    submission_text = file_input(os.path.join(SUBMISSIONS, submission_filename))

    with open(os.path.join(TMP, "%s.java" % JAVA_FILE), "w+") as tower:
        tower.write(submission_text)

    name = re.search(r"([a-z]*)_", submission_filename).group(1)
    print(name)

    try:
        compile_message = subprocess.check_output(
                "javac %s.java" % os.path.join(TMP, JAVA_FILE),
                shell=True,
                stderr=subprocess.STDOUT).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print("compile failed")
        with open(os.path.join(SUMMARY, name + ".txt"), "a+") as summary:
            summary.write(str(e.output))
        return

    test_num = 0
    for test_in, test_out in test_in_out:
        test_num += 1
        with open(os.path.join(SUMMARY, name + ".txt"), "a+") as summary:
            summary.write("TEST %s\n" % test_num)
        stdout = subprocess.check_output(
                "java -cp %s %s < %s" % (TMP, JAVA_FILE, test_in),
                shell=True).decode("utf-8").rstrip() 
        diff = difflib.unified_diff(
                stdout.splitlines(stdout.count("\n")),
                test_out.splitlines(test_out.count("\n")),
                fromfile="student", tofile="solution")
        diff_str = "".join(diff)
        if diff_str:
            with open(os.path.join(SUMMARY, name + ".txt"), "a+") as summary:
                summary.write(diff_str)
            print("fail")
        else:
            print("pass")


if __name__ == "__main__":
    # Create a tmp directory to put all submissions in.
    if not os.path.exists(TMP):
        os.mkdir(TMP)

    if not os.path.exists(SUMMARY):
        os.mkdir(SUMMARY)

    inputs = dict()
    outputs = dict()
    for filename in os.listdir(TESTS):
        full_path = os.path.join(os.getcwd(), TESTS, filename)
        basename = get_basename_no_extension(filename)
        # Is input file
        if ".in" in filename:
            inputs[basename] = full_path
        else:
            outputs[basename] = file_input(full_path)

    test_in_out = list()
    for filename in (inputs.keys() & outputs.keys()):
        test_in_out.append((inputs[filename], outputs[filename]))

    # Iterate and grade.
    for submission_filename in os.listdir(SUBMISSIONS):
        grade(submission_filename, test_in_out)
