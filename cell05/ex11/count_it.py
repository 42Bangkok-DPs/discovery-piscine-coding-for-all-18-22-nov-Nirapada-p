import sys
if len(sys.argv) == 1:
    print("none")
else:
    print("fparameter: {len(sys.argv) -1}")
    for arg in sys.argv[1:]:
        print(f"{arg}: {len(arg)}")