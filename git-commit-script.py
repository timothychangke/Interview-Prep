import os
import subprocess

file_path = 'interview_questions.txt'

def commit_question_answer(question, answer):
    if not question or not answer:
        print(f"Skipping empty question or answer:\n{question}\n{answer}")
        return

    # Write the answer to a temporary file
    with open('answer.txt', 'w') as f:
        f.write(answer)

    # Stage and commit the changes with the question as the commit message
    subprocess.run(['git', 'add', 'answer.txt'])
    subprocess.run(['git', 'commit', '-m', question])

    # Remove the temporary answer file after commit
    os.remove('answer.txt')

def main():
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return

    # Add all untracked files to git before proceeding
    subprocess.run(['git', 'add', '.'])

    with open(file_path, 'r') as file:
        content = file.read().strip()

    pairs = content.split('\n\n')  # Split by two new lines to separate question-answer pairs

    if not pairs:
        print("No question-answer pairs found in the file.")
        return

    for pair in pairs:
        try:
            question, answer = pair.split('\n', 1)  # Split by a single new line to get question and answer
            commit_question_answer(question, answer)
        except ValueError:
            print(f"Skipping invalid question-answer pair:\n{pair}\n")
            continue

    print("All question-answer pairs have been committed.")

if __name__ == '__main__':
    main()
