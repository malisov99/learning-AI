from aiogram import types, Router, F
from aiogram.filters.command import Command
from service import get_question, new_quiz, get_quiz_state, update_quiz_state
from database import get_all_questions
from aiogram.utils.keyboard import ReplyKeyboardBuilder


router = Router()


def start_quiz_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    return builder.as_markup(resize_keyboard=True)


@router.callback_query(F.data.startswith("answer:"))
async def process_answer(callback: types.CallbackQuery):
    _, q_index, is_right = callback.data.split(":")
    q_index = int(q_index)
    is_right = int(is_right)

    await callback.bot.edit_message_reply_markup(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        reply_markup=None
    )

    current_index, score = await get_quiz_state(callback.from_user.id)
    
    if q_index != current_index:
        await callback.answer("Этот вопрос уже обработан")
        return

    if is_right:
        score += 1
        await callback.message.answer("✅ Верно!")
    else:
        quiz_data = get_all_questions()
        correct = quiz_data[q_index]["correct_option"]
        correct_text = quiz_data[q_index]["options"][correct]
        await callback.message.answer(f"❌ Неверно. Правильный ответ: {correct_text}")

    current_index += 1
    await update_quiz_state(callback.from_user.id, current_index, score)

    await get_question(callback.message, callback.from_user.id)


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Добро пожаловать в квиз!\nНажмите кнопку «Начать игру» 👇",
        reply_markup=start_quiz_keyboard()
    )


@router.message(F.text == "Начать игру")
@router.message(Command("quiz"))
async def cmd_quiz(message: types.Message):
    await message.answer(
        "Давайте начнем квиз!",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await new_quiz(message)