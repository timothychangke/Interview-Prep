import os
import subprocess

file_path = 'interview_questions.txt'

def commit_question_answer(question, answer):
    if not question or not answer:
        print(f"Skipping empty question or answer:\n{question}\n{answer}")
        return

    with open('answer.txt', 'w') as f:
        f.write(answer)

    subprocess.run(['git', 'add', 'answer.txt'])
    subprocess.run(['git', 'commit', '-m', question])


    os.remove('answer.txt')

def main():
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return


    subprocess.run(['git', 'add', '.'])

    with open(file_path, 'r') as file:
        content = file.read().strip()

    pairs = content.split('\n\n') 

    if not pairs:
        print("No question-answer pairs found in the file.")
        return

    for pair in pairs:
        try:
            question, answer = pair.split('\n', 1)  
            commit_question_answer(question, answer)
        except ValueError:
            print(f"Skipping invalid question-answer pair:\n{pair}\n")
            continue

    print("All question-answer pairs have been committed.")

if __name__ == '__main__':
    main()
