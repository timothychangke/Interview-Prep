#!/bin/bash

# Specify the file to commit
FILE="concepts.txt"

# Check if the file has any unstaged changes
echo "Checking for changes in $FILE..."
if ! git diff --quiet "$FILE"; then
    echo "Changes detected. Proceeding with commits."

    # Get all sections (split by double newlines, which separate paragraphs)
    sections=$(awk -v RS= '{print $0}' "$FILE")

    # Iterate over each section and commit them individually
    count=1
    while IFS= read -r section; do
        # Extract the first line of the section to use as the commit message
        commit_msg=$(echo "$section" | head -n 1)

        # Add changes to staging area for the current section
        echo "$section" > "$FILE"  # Update the file with the current section
        
        git add "$FILE"  # Stage the changes for this section

        # Debugging output to show what is happening
        echo "Staging and committing section: $commit_msg"

        # Commit the staged changes with the first line as the commit message
        git commit -m "Commit for: $commit_msg"

        # Proceed to the next section
        count=$((count + 1))
    done <<< "$sections"
else
    echo "No changes detected in $FILE."
fi
