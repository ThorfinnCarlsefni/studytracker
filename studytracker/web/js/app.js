(function() {
    'use strict';

    const STORAGE_KEY = 'studytracker_tasks';
    let tasks = [];
    let currentFilter = 'all';

    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');
    const emptyState = document.getElementById('empty-state');
    const filterButtons = document.querySelectorAll('.filter-btn');

    function init() {
        loadTasks();
        renderTasks();
        attachEventListeners();
    }

    function loadTasks() {
        try {
            const storedTasks = localStorage.getItem(STORAGE_KEY);
            if (storedTasks) {
                tasks = JSON.parse(storedTasks);
                if (!Array.isArray(tasks)) {
                    throw new Error('Некорректные данные');
                }
            }
        } catch (error) {
            console.warn('Ошибка загрузки:', error);
            tasks = [];
            localStorage.removeItem(STORAGE_KEY);
        }
    }

    function saveTasks() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
        } catch (error) {
            console.error('Ошибка сохранения:', error);
        }
    }

    function sanitizeInput(input) {
        const tempDiv = document.createElement('div');
        tempDiv.textContent = input;
        return tempDiv.textContent.trim();
    }

    function createTaskElement(task) {
        const li = document.createElement('li');
        li.className = `task-item ${task.completed ? 'completed' : ''}`;
        li.dataset.id = task.id;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'task-content';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'task-checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('change', () => toggleTaskStatus(task.id));

        const textSpan = document.createElement('span');
        textSpan.className = 'task-text';
        textSpan.textContent = task.text;

        contentDiv.appendChild(checkbox);
        contentDiv.appendChild(textSpan);

        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'btn-delete';
        deleteBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>';
        deleteBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            deleteTask(task.id);
        });

        li.appendChild(contentDiv);
        li.appendChild(deleteBtn);

        return li;
    }

    function addTask(text) {
        const sanitizedText = sanitizeInput(text);
        if (!sanitizedText) return;

        const newTask = {
            id: Date.now().toString(),
            text: sanitizedText,
            completed: false,
            createdAt: new Date().toISOString()
        };

        tasks.unshift(newTask);
        saveTasks();
        renderTasks();
    }

    function toggleTaskStatus(id) {
        const task = tasks.find(t => t.id === id);
        if (task) {
            task.completed = !task.completed;
            saveTasks();
            renderTasks();
        }
    }

    function deleteTask(id) {
        tasks = tasks.filter(t => t.id !== id);
        saveTasks();
        renderTasks();
    }

    function getFilteredTasks() {
        switch (currentFilter) {
            case 'active':
                return tasks.filter(t => !t.completed);
            case 'completed':
                return tasks.filter(t => t.completed);
            default:
                return tasks;
        }
    }

    function renderTasks() {
        taskList.innerHTML = '';
        const filteredTasks = getFilteredTasks();

        if (filteredTasks.length === 0) {
            taskList.style.display = 'none';
            emptyState.hidden = false;
        } else {
            taskList.style.display = 'flex';
            emptyState.hidden = true;
            filteredTasks.forEach(task => {
                taskList.appendChild(createTaskElement(task));
            });
        }
    }

    function setFilter(filter) {
        currentFilter = filter;
        filterButtons.forEach(btn => {
            const isActive = btn.dataset.filter === filter;
            btn.classList.toggle('active', isActive);
        });
        renderTasks();
    }

    function attachEventListeners() {
        taskForm.addEventListener('submit', (e) => {
            e.preventDefault();
            addTask(taskInput.value);
            taskInput.value = '';
            taskInput.focus();
        });

        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                setFilter(btn.dataset.filter);
            });
        });
    }

    init();
})();