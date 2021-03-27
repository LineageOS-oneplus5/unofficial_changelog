from datetime import datetime
import subprocess
import os

CHANGELOG_FILENAME = "changelog_{}.txt".format(datetime.today().strftime("%Y%m%d"))
print("Changelog to file {}".format(CHANGELOG_FILENAME))

# Write changelog
changelog_file = open(CHANGELOG_FILENAME, "w+")
log = subprocess.Popen("repo forall -pvc 'git log --after=\"2021-03-21\" --pretty=\"format:%<(12)%h %<(20)%an %s\"'", shell=True, cwd='./', stdout=subprocess.PIPE)
output = log.stdout.read().decode('utf-8')
if output != "":
    print(output)
    changelog_file.write(output)
