from api.deps import get_db
from models import Prompt


PROMPTS = [
    Prompt(
        id=1,
        title="Hello!",
        template="Hello!",
        description="Just a prompt that says hello to ChatGPT.",
        examples=[
            {
                "user_message": "Hello!",
                "system_message": "Hello! How can I assist you today?"
            }
        ]
    ),
    Prompt(
        id=4,
        title="Calculator!",
        template="<your mathematical expression>",
        description="ChatGPT can calculate things.",
        examples=[
            {
                "user_message": "2 + 2",
                "system_message": "2 + 2 = 4"
            },
            {
                "user_message": "13 * 8",
                "system_message": "13 * 8 = 104"
            }
        ]
    ),
    Prompt(
        id=12,
        title="What is the capital of the country?",
        description="ChatGPT knows the capitals of countries.",
        template="What\'s the capital of <country>?",
        examples=[
            {
                "user_message": 'What is the capital of Norway?',
                "system_message": 'The capital of Norway is Oslo.'
            },
            {
                "user_message": 'What is the capital of Belarus?',
                "system_message": 'The capital of Belarus is Minsk.'
            }
        ]
    )
]


def init_db():
    session = next(get_db())
    session.bulk_save_objects(PROMPTS)
    session.commit()


if __name__ == '__main__':
    init_db()
