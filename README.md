# English Dictionary & Quiz App

#### Video Demo: <https://youtu.be/4Gwle3xzwIk>
#### Description:
A Python application that helps users learn English vocabulary through definitions and synonym quizzes. Perfect for language learners at intermediate levels (B1-B2).

### Features
- **Word Search**: Instant definitions and synonyms lookup
- **Interactive Quiz**: Test your knowledge of word relationships
- **JSON Database**: Easy-to-modify vocabulary storage
- **Error Handling**: Robust input validation and file management

This application was developed as my final project for CS50's Introduction to Programming with Python course, demonstrating mastery of file I/O, data structures, and test-driven development.

### File Structure
1. **project.py** - Main application logic containing:
   - `main()`: Controls program flow and menu system
   - `load_data()`: Reads JSON vocabulary file
   - `quiz()`: Manages interactive testing system
   - `search_word()`: Implements lookup functionality

2. **test_project.py** - Unit tests verifying:
   - Data loading reliability
   - Search function accuracy
   - Synonym validation logic
   - Edge case handling

3. **data.json** - Vocabulary database containing:
   - 100+ common English words
   - Dictionary-formatted entries with:
     - Word spelling
     - Simple definitions
     - Contextual synonyms

4. **requirements.txt** - Dependency list ensuring:
   - pytest framework for testing
   - Python 3.10+ compatibility

### Design Choices
1. **JSON Data Storage**
Chose JSON over SQLite for:
   - Human-readable format
   - Easy manual editing
   - Native Python support

2. **Linear Search Algorithm**
Implemented simple search rather than binary because:
   - Dataset size (<500 items) makes efficiency negligible
   - Simplifies code maintenance
   - Allows direct synonym access during quizzes

3. **Randomized Quiz Selection**
Used `random.sample()` to:
   - Prevent question repetition
   - Ensure varied practice sessions
   - Maintain engagement through unpredictability

4. **Input Sanitization**
Added `.lower().strip()` to handle:
   - Case-sensitive typos
   - Accidental whitespace
   - Inconsistent formatting

### Installation
1. Clone repository:
```bash
git clone https://github.com/your-username/english-dictionary-app.git