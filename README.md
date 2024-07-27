# vscode-extensions
This repository manages vscode extensions.<br><br>

All extensions are listed in the link below.<br>
https://gist.github.com/tutti-hobbyist/70fbb47b4774ee1c334df9e6d626f474

## How to use
- Fork this repo and clone it.
- Edit `extension-ids.txt` as you want.
- Make and register personal access token (PAT) on GitHub to make use of GitHub Actions.
    > **Explain about PAT** <br>
    > https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- Edit `ACTIONS_PAT` in `generate.yaml` to fit your PAT setting.
- Push the modified codes and check the result of actions, you will see `install-vscode-extensions.ps1` is generated in your repo.