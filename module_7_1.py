import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()

                    # Удаляем пунктуацию
                    for punct in punctuation_to_remove:
                        content = content.replace(punct, '')

                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            try:
                position = words.index(word)+1
            except ValueError:
                position = -1
            positions[file_name] = position

        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            counts[file_name] = count

        return counts

# Пример использования:
if __name__ == '__main__':
   # text = "It's a text for task Найти везде, Используйте его для самопроверки. Успехов в решении задачи! text text text"
   # file = open('test_file.txt','w')
   # file.write(text)
   # file.close()

    finder2 = WordsFinder('test_file.txt')

    print(finder2.get_all_words())  # Все слова

    print(finder2.find('TEXT'))  # Позиция первого вхождения слова

    print(finder2.count('teXT'))  # Количество вхождений слова

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
