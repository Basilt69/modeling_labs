import streamlit as st

from lab_01 import lab1


def header():
    author = '''
    made by [Basil Tkachenko](https://github.com/Basilt69)
    in [BMSTU](https://bmstu.ru)
    '''

    st.header('МГТУ им. Баумана, Кафедра ИУ7')
    st.markdown("**Курс:**Моделирование")
    st.markdown("**Преподаватель:**Градов В.М.")
    st.markdown("**Студент:** Ткаченко В.М.")
    st.sidebar.markdown(author)

def main():
    header()
    lab = st.sidebar.radio(
        "Выберите лабораторную работу:", (
            "1. Полиномиальная интерполяция табличных функций(Полином Ньютона).",
            "2. Полиномиальная интерполяция табличных функций(Полином Эрмита).",
        ),
        index=4
    )

    if lab[:1] == "1":
        lab1.main()

if __name__ == "__main__":
    main()