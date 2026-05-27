import streamlit as st

st.title("Привіт це опитування!")


test1 = st.radio("Ви считаете Ярика богом:", ["Вибирите ответ", "Да", "Да"])
if test1 == "Да":
    st.success("Правильно")
if test1 == "Да":
    st.success("Правильно")

test2 = st.radio("Начало войны второй мировой войны:", ["Вибирите ответ","1 сентября 1939 г.", "5 сентября 1939 г.", "8 сентября 1939 г."])
if test2 == "1 сентября 1939 г.":
    st.success("Правильно")
else:
    st.error("Неправильно")

test3 = st.radio("Вторжение в СССР мировой войны:", ["Вибирите ответ","22 июня 1941 г.", "20 июня 1941 г.", "16 июня 1941 г."])
if test3 == "22 июня 1941 г.":
    st.success("Правильно")
else:
    st.error("Неправильно")

test4 = st.radio("Какое событие заставило США официально вступить во Вторую мировую войну?", ["Вибирите ответ", "Высадка в Нормандии", "Нападение на Пёрл-Харбор", "Битва за Алеутские острова"],)

if test4 == "Нападение на Пёрл-Харбор":
    st.success("Правильно")
else:
    st.error("Неправильно")

test5 = st.radio("Капитуляция Германии:", ["Вибирите ответ", "16 мая 1945 г.", "9 мая 1945 г.", "19 мая 1945 г."])
if test5 == "9 мая 1945 г.":
    st.success("Правильно")
else:
    st.error("Неправильно")

test6 = st.radio("Капитуляция Японии:", ["Вибирите ответ", "8 сентября 1945 г.", "9 сентября 1945 г.", "2 сентября 1945 г."])
if test6 == "2 сентября 1945 г.":
    st.success("Правильно")
else:
    st.error("Неправильно")

if st.button("Завершить опрос"):
    correct_answers = 0

    if 'test2' in locals() and test2 == "1 сентября 1939 г.":
        correct_answers += 1
    if 'test3' in locals() and test3 == "22 июня 1941 г.":
        correct_answers += 1
    if 'test4' in locals() and test4 == "Нападение на Пёрл-Харбор":
        correct_answers += 1
    if 'test5' in locals() and test5 == "9 мая 1945 г.":
        correct_answers += 1
    if 'test6' in locals() and test6 == "2 сентября 1945 г.":
        correct_answers += 1
    
    total_questions = 5
    choto = (correct_answers / total_questions) * 100
    
    st.write(f"Ваш результат: {choto:.1f}%")
    st.write(f"Правильных ответов: {correct_answers} из {total_questions}")
