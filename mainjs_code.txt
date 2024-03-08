let nameInput = document.getElementById('name');
let weightInput = document.getElementById('weight'); 
let repsInput = document.getElementById('reps');
let setsInput = document.getElementById('sets');
let difficultySelect = document.getElementById('difficulty');
let detailsInput = document.getElementById('details');
let exerciseId = document.getElementById('exercise-id');
let nameEditInput = document.getElementById('name-edit');
let weightEditInput = document.getElementById('weight-edit'); 
let repsEditInput = document.getElementById('reps-edit');
let setsEditInput = document.getElementById('sets-edit');
let difficultyEditSelect = document.getElementById('difficulty-edit');
let detailsEditInput = document.getElementById('details-edit');
let exercises = document.getElementById('exercises');
let data = [];
let selectedExercise = {};
const api = 'http://127.0.0.1:8000';

document.getElementById('form-add').addEventListener('submit', (e) => {
    e.preventDefault();
    addExercise(nameInput.value, weightInput.value, repsInput.value, setsInput.value, difficultySelect.value, detailsInput.value);
});

let addExercise = (name, weight, reps, sets, difficulty, details) => {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 201) {
            const newExercise = JSON.parse(xhr.responseText);
            data.push(newExercise);
            refreshExercises();
            document.getElementById('form-add').reset();
        }
    };
    xhr.open('POST', `${api}/exercises`, true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({ name, weight, reps, sets, difficulty, details }));
};

let refreshExercises = () => {
    exercises.innerHTML = '';
    data.sort((a, b) => b.id - a.id).forEach((exercise) => {
        exercises.innerHTML += `
            <div id="exercise-${exercise.id}" class="exercise-card">
                <h3>${exercise.name}</h3>
                <p>Weight: ${exercise.weight} lbs - Reps: ${exercise.reps} - Sets: ${exercise.sets} - Difficulty: ${exercise.difficulty}</p>
                <p>Details: ${exercise.details}</p>
                <div class="options">
                    <button onclick="tryEditExercise(${exercise.id})" class="btn-edit">Edit</button>
                    <button onclick="deleteExercise(${exercise.id})" class="btn-delete">Delete</button>
                </div>
            </div>
        `;
    });
};

let tryEditExercise = (id) => {
    const exercise = data.find((exercise) => exercise.id === id);
    selectedExercise = exercise;
    exerciseId.value = exercise.id;
    nameEditInput.value = exercise.name;
    weightEditInput.value = exercise.weight; 
    repsEditInput.value = exercise.reps;
    setsEditInput.value = exercise.sets;
    difficultyEditSelect.value = exercise.difficulty;
    detailsEditInput.value = exercise.details;
    new bootstrap.Modal(document.getElementById('modal-edit')).show();
};

document.getElementById('form-edit').addEventListener('submit', (e) => {
    e.preventDefault();
    editExercise(selectedExercise.id, nameEditInput.value, weightEditInput.value, repsEditInput.value, setsEditInput.value, difficultyEditSelect.value, detailsEditInput.value);
});

let editExercise = (id, name, weight, reps, sets, difficulty, details) => {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            Object.assign(selectedExercise, { name, weight, reps, sets, difficulty, details });
            refreshExercises();
        }
    };
    xhr.open('PUT', `${api}/exercises/${id}`, true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({ name, weight, reps, sets, difficulty, details }));
};

let deleteExercise = (id) => {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            data = data.filter((exercise) => exercise.id !== id);
            refreshExercises();
        }
    };
    xhr.open('DELETE', `${api}/exercises/${id}`, true);
    xhr.send();
};

let getExercises = () => {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            data = JSON.parse(xhr.responseText) || [];
            refreshExercises();
        }
    };
    xhr.open('GET', `${api}/exercises`, true);
    xhr.send();
};

getExercises(); 
