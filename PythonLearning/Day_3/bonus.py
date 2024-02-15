fileNames = ["1.hello.txt", "2.report.txt", "3.presentation.txt"]

for name in fileNames:
    newName = name.replace('.', '-', 1)
    print(newName)
