import argparse
import fnmatch
import os
import subprocess
import time

def get_args():
    parser = argparse.ArgumentParser(
        description="watch the project directory and run specified tests")
    
    parser.add_argument('--tests', action='store', required=True,
                        help='path to the tests')

    parser.add_argument('--project', nargs='+', action='store', required=False,
                        help='path to watch for changes')

    parser.add_argument('--pattern', action='store', required=False,
                        help='pattern to match inside the test directory')

    return parser.parse_args()


def get_matching_files(project_path, pattern=None):

    files = os.listdir(project_path)

    if not pattern:
        return files

    matching_files = []

    for f in files:
        if fnmatch.fnmatch(f, pattern):
            matching_files.append(f)

    return matching_files


def run_tests(test_path, test_pattern='Test_*.py'):

    cmd = [ 'python3', '-m', 'unittest', 'discover',
            '-s', test_path, '-p', test_pattern]

    subprocess.call(cmd)


def get_fullpath_listing(search_path, search_pattern=None):

    filelist = os.listdir(search_path)
    fullpath_filelist = []

    if not search_pattern:
        search_pattern = '*'

    for f in filelist:
        if fnmatch.fnmatch(f, search_pattern):        
            fullpath_filelist.append(search_path + '/' + f)

    return fullpath_filelist


def get_modtime(filepath):

    try:
        modtime = os.stat(filepath).st_mtime
    except:
        modtime = None
    
    return modtime


def watcher(test_path, watch_paths=None, test_pattern=None):

    filemod_lookup = {}
    while True:

        test_files = get_fullpath_listing(test_path,
                                          test_pattern)

        watch_files = []
        for p in watch_paths:
            watch_files = watch_files + get_fullpath_listing(p)

        for f in watch_files:
            mod_time = get_modtime(f)

            if f not in filemod_lookup:
                filemod_lookup[f] = mod_time

            elif mod_time != filemod_lookup[f]:
                filemod_lookup[f] = mod_time
                run_tests(test_path, test_pattern=test_pattern)


        time.sleep(1)


if __name__ == '__main__':
    args = get_args()
    w = watcher(args.tests, args.project, args.pattern)
