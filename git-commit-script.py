import subprocess

file_path = 'interview_questions.txt'

def get_commit_message(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    paragraphs = ''.join(lines).split('\n\n')

    if len(paragraphs) < 2:
        raise Exception("Not enough paragraphs found to create a commit message.")

    last_paragraph = paragraphs[-2]  
    commit_message = last_paragraph.strip().split('\n')[-1]  
    
    return commit_message

def git_commit_push(file_path):
    commit_message = get_commit_message(file_path)

    subprocess.run(['git', 'add', file_path])
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

if __name__ == '__main__':
    git_commit_push(file_path)
