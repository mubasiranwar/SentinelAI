import csv
import os

def clean_text(text: str):
    return text.strip()

def load_posts_from_csv(file_path: str):
    posts = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                posts.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return posts

if __name__ == "__main__":
    # Test with the sample file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'data', 'sample_posts.csv')
    
    print(f"Attempting to load from: {data_path}")
    loaded_posts = load_posts_from_csv(data_path)
    print(f"Loaded {len(loaded_posts)} posts.")
    if loaded_posts:
        print("First 3 posts:")
        for post in loaded_posts[:3]:
            print(post)
