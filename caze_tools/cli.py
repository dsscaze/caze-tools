import click
from caze_tools.commands.mkstruct import mkstruct_command
from caze_tools.commands.lsstruct import ls_struct_command
from caze_tools.commands.merge import merge_command

@click.group()
def main():
    """caze-tools — Dev CLI by dsscaze"""
    pass

main.add_command(mkstruct_command)
main.add_command(ls_struct_command)
main.add_command(merge_command)

if __name__ == "__main__":
    main()
