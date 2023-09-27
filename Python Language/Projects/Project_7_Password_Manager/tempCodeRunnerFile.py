def clear_terminal():
    if platform.system() == "Windows":
        print("YES")
        # subprocess.run(["cls"], shell=True)
    else:
        # subprocess.run(["clear"], shell=True)
        print("NO")


clear_terminal()