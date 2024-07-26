
def main():
    # read extension lists
    with open("extension-ids.txt", "r") as rf:
        lines = rf.readlines()

    # write scripts following some rules
    with open("install-vscode-extensions.ps1", "w") as wf:
        for line in lines:
            # write line as it is which starts "#" or "\n"
            if line.startswith(("#", "\n")):
                wf.write(line)
            # write other lines with install command
            else:
                extension_id = line.strip()
                command = f"code --install-extension {extension_id}\n"
                wf.write(command)

if __name__ == "__main__":
    main()