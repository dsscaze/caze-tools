Before responding to any request:

- Treat all rules in that file as mandatory
- Do NOT create documentation unless explicitly requested
- Do NOT create more than one markdown document per request
- If there is any doubt, STOP and ask before proceeding
- ALL answers MUST be written in pt-br
- ALL commit messages MUST be written in pt-br
- ALL pull request descriptions MUST be written in pt-br
- all documentation MUST be created ONLY inside the `/docs` directory

Violating any rule in this section MUST be treated as an error.

## CLI Commands Naming Convention

When creating new CLI commands:
- Command names should be **short and concise** (e.g., `addprefix` instead of `adicionar-prefixo`)
- The Python **file name MUST match the command name exactly** (e.g., a command named `addprefix` must be in `addprefix.py`)
- The command function should be named the same as the file name
- Register the command in `cli.py` with `main.add_command(command_function)`