# Todo List with Text File Storage

## Overview
A feature-rich Todo List Manager application built with Python's Tkinter library. This intermediate-level project provides a user-friendly graphical interface for managing daily tasks with persistent storage in text files.

## Features Added by Jaswanth

### 1. **Tkinter GUI Interface**
- Modern and intuitive graphical user interface
- Clean design with organized layout
- Color-coded elements for better user experience
- Responsive window sizing (600x500)

### 2. **Add Tasks**
- Simple text entry field for adding new tasks
- Add button with visual feedback
- Input validation to prevent empty tasks
- Clear input field after task addition

### 3. **Mark Tasks as Complete**
- Toggle completion status for any task
- Visual indicators (✓ for completed, ○ for pending)
- Completed tasks displayed in green color
- One-click status change

### 4. **Delete Tasks**
- Remove unwanted tasks from the list
- Confirmation dialog to prevent accidental deletion
- Instant UI update after deletion

### 5. **Edit Existing Tasks**
- Modify task descriptions without deletion
- Simple dialog box for editing
- Preserves task completion status
- Quick and easy task updates

### 6. **Text File Storage**
- Automatic save to `tasks.txt` file
- Persistent data storage between sessions
- Load tasks automatically on application start
- Simple file format: STATUS|TASK_DESCRIPTION
- Human-readable text file format

### 7. **Display Statistics**
- **Total Tasks**: Shows the total number of tasks
- **Completed Tasks**: Count of finished tasks
- **Pending Tasks**: Count of incomplete tasks
- Real-time statistics update
- Visual statistics panel with raised border

### 8. **Additional Features**
- Scrollable task list for handling many tasks
- Task selection highlighting
- Warning messages for invalid operations
- Professional color scheme
- Cross-platform compatibility

## Technical Implementation

### Technologies Used
- **Python 3.x**: Core programming language
- **Tkinter**: GUI framework (comes with Python)
- **os module**: File system operations
- **messagebox**: User notifications
- **simpledialog**: Task editing dialogs

### File Structure
```
Todo_List_Text_Storage/
├── todo_app.py          # Main application file
├── tasks.txt            # Auto-generated task storage file
└── README.md            # Project documentation
```

### Data Storage Format
Tasks are stored in `tasks.txt` with the following format:
```
TODO|Buy groceries
DONE|Complete Python project
TODO|Read a book
```

## Installation & Usage

### Prerequisites
- Python 3.x installed on your system
- Tkinter (usually comes pre-installed with Python)

### Running the Application

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/MEKALA-JASWANTH/Todo_List_Text_Storage.git
   cd Todo_List_Text_Storage
   ```

2. **Run the Application**
   ```bash
   python todo_app.py
   ```

3. **Using the Application**
   - **Add Task**: Type your task in the entry field and click "Add Task"
   - **Mark Complete**: Select a task and click "Mark Complete" to toggle its status
   - **Edit Task**: Select a task and click "Edit Task" to modify it
   - **Delete Task**: Select a task and click "Delete Task" to remove it
   - **View Statistics**: Check the bottom panel for task counts

## Application Features in Detail

### User Interface Components

1. **Title Bar**: "Todo List Manager - By Jaswanth"
2. **Input Section**: Text entry field with Add button
3. **Task List**: Scrollable listbox displaying all tasks
4. **Action Buttons**:
   - Mark Complete (Blue)
   - Edit Task (Orange)
   - Delete Task (Red)
5. **Statistics Panel**: Shows Total, Completed, and Pending tasks

### Color Scheme
- **Background**: Light gray (#f0f0f0)
- **Add Button**: Green (#4CAF50)
- **Mark Complete**: Blue (#2196F3)
- **Edit Button**: Orange (#FF9800)
- **Delete Button**: Red (#f44336)
- **Completed Tasks**: Green text
- **Statistics Panel**: Light gray (#e0e0e0) with raised border

## Code Structure

### Main Class: TodoApp

**Key Methods:**
- `__init__()`: Initialize the application
- `create_widgets()`: Build the GUI components
- `add_task()`: Add new task to the list
- `mark_complete()`: Toggle task completion status
- `edit_task()`: Modify existing task
- `delete_task()`: Remove task from list
- `update_listbox()`: Refresh the task display
- `save_tasks()`: Write tasks to text file
- `load_tasks()`: Read tasks from text file
- `update_statistics()`: Update task count display

## Key Learning Outcomes

1. **GUI Development**: Building interactive interfaces with Tkinter
2. **File I/O Operations**: Reading and writing to text files
3. **Data Persistence**: Maintaining data between application sessions
4. **Event Handling**: Managing user interactions
5. **Data Structures**: Working with lists and dictionaries
6. **User Experience**: Creating intuitive interfaces
7. **Error Handling**: Input validation and user feedback

## Future Enhancements

- Add task priority levels
- Implement due dates for tasks
- Add search and filter functionality
- Support for task categories
- Export tasks to different formats (CSV, JSON)
- Task reminders and notifications
- Undo/Redo functionality
- Dark mode theme option

## Project Level
**Intermediate Python Project**

This project is suitable for those who:
- Have basic Python knowledge
- Want to learn GUI programming
- Need to understand file handling
- Are building their project portfolio

## Author
**Jaswanth MEKALA**

GitHub: [MEKALA-JASWANTH](https://github.com/MEKALA-JASWANTH)

## License
Free to use for educational purposes.

## Contributing
Feel free to fork this project and add your own enhancements!

## Acknowledgments
- Python Software Foundation for Python and Tkinter
- GitHub for hosting this repository

---

**Happy Task Managing! 📝✅**
