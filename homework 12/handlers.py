from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from bot import dp
from quiz_data import quiz_data
from database import get_quiz_index, update_quiz_index
from database import save_result, get_stats

user_scores = {}
user_lock = {}


def generate_options_keyboard(options):
    builder = InlineKeyboardBuilder()
    for index, option in enumerate(options):
        builder.add(
            types.InlineKeyboardButton(
                text=option,
                callback_data=f"answer:{index}"
            )
        )
    builder.adjust(1)
    return builder.as_markup()

# хендлеры
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(Command("stats"))
async def cmd_stats(message: types.Message):
    stats = await get_stats()

    if not stats:
        await message.answer("Статистика пока пуста.")
        return

    text = "🏆 Статистика игроков:\n\n"

    for i, (user_id, score, total) in enumerate(stats, start=1):
        text += f"{i}. ID {user_id}: {score}/{total}\n"

    await message.answer(text)

@dp.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    await message.answer("Давайте начнем квиз!")
    await new_quiz(message)

@dp.message(F.text == "Начать игру")
async def cmd_start_game(message: types.Message):
    await message.answer("Давайте начнем квиз!")
    await new_quiz(message)

# логика квиза
async def get_question(message, user_id):
    index = await get_quiz_index(user_id)
    question = quiz_data[index]

    kb = generate_options_keyboard(question["options"])
    await message.answer(question["question"], reply_markup=kb)

async def new_quiz(message):
    user_id = message.from_user.id

    # Сбрасываем очки
    user_scores[user_id] = 0

    current_question_index = 0
    await update_quiz_index(user_id, current_question_index)
    await get_question(message, user_id)

# Callback ответы
@dp.callback_query(F.data.startswith("answer:"))
async def process_answer(callback: types.CallbackQuery):
    user_id = callback.from_user.id

    await callback.answer()

    if user_lock.get(user_id):
        return

    user_lock[user_id] = True
    try:
        try:
            await callback.message.edit_reply_markup(None)
        except Exception:
            pass

        answer_index = int(callback.data.split(":")[1])
        question_index = await get_quiz_index(user_id)

        question = quiz_data[question_index]
        correct_index = question["correct_option"]
        user_answer_text = question["options"][answer_index]

        await callback.message.answer(f"Ваш ответ: {user_answer_text}")

        if answer_index == correct_index:
            user_scores[user_id] += 1
            await callback.message.answer("✅ Верно!")
        else:
            await callback.message.answer(
                f"❌ Неверно.\nПравильный ответ: {question['options'][correct_index]}"
            )

        question_index += 1
        await update_quiz_index(user_id, question_index)

        if question_index < len(quiz_data):
            await get_question(callback.message, user_id)
        else:
            score = user_scores.get(user_id, 0)
            total = len(quiz_data)
            await save_result(user_id, score, total)

            await callback.message.answer(
                f"🏁 Квиз завершён!\n"
                f"Ваш результат: {score} из {total}"
            )
            user_scores.pop(user_id, None)

    finally:
        user_lock[user_id] = False