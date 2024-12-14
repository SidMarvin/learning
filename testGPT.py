#нужно понять, какой версией питона пользоваться - python или python3. 
#python3 -m pip install --upgrade pip
#pip install openai

from openai import OpenAI

#Инициализация
client = OpenAI(
    api_key="sk-YpYQwVvo4khO6pSxrL5YDS7XvHUGCUaK",
    base_url="https://api.proxyapi.ru/openai/v1",
)

while True:
    #Запрос
    user_input = input("Введите ваш вопрос (или 'выход' для завершения): ")
    
    #Условие выхода из цикла
    if user_input.lower() == 'выход':
        print("До свидания!")
        break
    
    #Отправка вопроса
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    
    #ответ
    response = chat_completion.choices[0].message.content
    print("Ответ ChatGPT:", response)
