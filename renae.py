import shutil,os,re
a = 1
datePattern = re.compile(r"""((0|1|2|3)?\d)_((0|1)?\d)(.*?)$""",re.VERBOSE)
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    if mo ==None:
        continue
    monthPart = mo.group(3)
    dayPart = mo.group(1)
    afterPart = mo.group(5)

    euroFilename = str(a)+'.png'

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir,amerFilename)
    euroFilename = os.path.join(absWorkingDir,euroFilename)

    print('Renaming "%s" to "%s".....'%(amerFilename,euroFilename))
    shutil.move(amerFilename, euroFilename)
    a = a+1
