import { showForm, showHome } from './ui.js';
import { handleFormSubmit } from './forms.js';

document.getElementById('addExpense').addEventListener('click', () => showForm('expense'));
document.getElementById('addIncome').addEventListener('click', () => showForm('income'));
document.getElementById('addSaving').addEventListener('click', () => showForm('saving'));
document.getElementById('addAccount').addEventListener('click', () => showForm('account'));
document.getElementById('backToHome').addEventListener('click', showHome);

document.getElementById('financialForm').addEventListener('submit', handleFormSubmit);