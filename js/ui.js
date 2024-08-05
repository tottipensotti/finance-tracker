import { createFormFields } from './forms.js';

export function showForm(type) {
    const buttonContainer = document.getElementById('buttonContainer');
    const formContainer = document.getElementById('formContainer');
    const formTitle = document.getElementById('formTitle');
    
    buttonContainer.style.display = 'none';
    createFormFields(type);
    formTitle.textContent = `Add ${type.charAt(0).toUpperCase() + type.slice(1)}`;
    formContainer.style.display = 'block';
}

export function showHome() {
    document.getElementById('buttonContainer').style.display = 'flex';
    document.getElementById('formContainer').style.display = 'none';
    document.getElementById('financialForm').reset();
    clearMessage();
}

export function displayMessage(message, isError = false) {
    const messageContainer = document.getElementById('messageContainer');
    messageContainer.textContent = message;
    messageContainer.style.color = isError ? 'red' : 'green';
}

export function clearMessage() {
    const messageContainer = document.getElementById('messageContainer');
    messageContainer.textContent = '';
}