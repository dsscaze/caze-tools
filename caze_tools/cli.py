import click
from caze_tools.commands.mkstruct import mkstruct_command
from caze_tools.commands.lsstruct import ls_struct_command
from caze_tools.commands.merge import merge_command
from caze_tools.commands.addprefix import addprefix
from caze_tools.commands.toroot import toroot
from caze_tools.commands.rename import rename
from caze_tools.commands.trimimg import trimimg

@click.group(no_args_is_help=True)
def main():
    """caze-tools — Dev CLI by dsscaze"""
    pass

main.add_command(mkstruct_command)
main.add_command(ls_struct_command)
main.add_command(merge_command)
main.add_command(addprefix)
main.add_command(toroot)
main.add_command(rename)
main.add_command(trimimg)

if __name__ == "__main__":
    main()
