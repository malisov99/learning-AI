from database import pool, execute_update_query, execute_select_query, get_all_questions
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

QUIZ_IMAGE_URL = "https://storage.yandexcloud.net/imagebot/quizimage.png"
quiz_data = get_all_questions()


def generate_options_keyboard(answer_options, correct_index, question_index):
    builder = InlineKeyboardBuilder()

    for idx, option in enumerate(answer_options):
        is_right = 1 if idx == correct_index else 0
        builder.add(
            types.InlineKeyboardButton(
                text=option,
                callback_data=f"answer:{question_index}:{is_right}"
            )
        )

    builder.adjust(1)
    return builder.as_markup()


async def get_question(message, user_id):
    quiz_data = get_all_questions()
    question_index, score = await get_quiz_state(user_id)

    if question_index >= len(quiz_data):
        await message.answer(
            f"Квиз завершен! Ваш результат: {score} / {len(quiz_data)}"
        )
        return

    q = quiz_data[question_index]

    kb = generate_options_keyboard(
        q["options"],
        q["correct_option"],
        question_index
    )

    await message.answer(q["question"], reply_markup=kb)


async def new_quiz(message):
    user_id = message.from_user.id

    await update_quiz_state(user_id, 0, 0)

    try:
        await message.answer_photo(
            photo=QUIZ_IMAGE_URL,
            caption="🎉 Добро пожаловать в квиз!\nГотов проверить свои знания?"
        )
    except Exception as e:
        print("Ошибка отправки обложки:", e)

    await get_question(message, user_id)

async def get_quiz_state(user_id):
    query = """
        DECLARE $user_id AS Uint64;

        SELECT question_index, score
        FROM quiz_state
        WHERE user_id == $user_id;
    """
    results = execute_select_query(pool, query, user_id=user_id)

    if len(results) == 0:
        return 0, 0

    return results[0]["question_index"], results[0]["score"]


async def update_quiz_state(user_id, question_index, score):
    query = """
        DECLARE $user_id AS Uint64;
        DECLARE $question_index AS Uint64;
        DECLARE $score AS Uint64;

        UPSERT INTO quiz_state (user_id, question_index, score)
        VALUES ($user_id, $question_index, $score);
    """
    execute_update_query(
        pool,
        query,
        user_id=user_id,
        question_index=question_index,
        score=score
    )