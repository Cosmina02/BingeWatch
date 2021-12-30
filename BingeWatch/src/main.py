from src.db.session import session_scope
from src.db_interaction.interaction import *
from src.utils.commands import pick_command


if __name__ == '__main__':

    with session_scope() as crt_session:
        repo = Interaction(crt_session)

        pick_command(repo)
