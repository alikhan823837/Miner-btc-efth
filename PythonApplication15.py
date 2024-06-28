def main():
    num1 = 7  
    num2 = 5  

    # Выводим задачу
    print(f"еки саннын косындысын табыныз: {num1} + {num2} = ", end='')

    # Считываем ответ пользователя
    user_answer = int(input())

    # Проверяем ответ
    correct_answer = num1 + num2
    if user_answer == correct_answer:
        print("дурыс")
    else:
        print(f"дурыс емес. Дурыс жауып: {correct_answer}")

if __name__ == "__main__":
    main()
