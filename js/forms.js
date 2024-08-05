import { displayMessage, showHome } from './ui.js';
import { createEntry } from './api.js';

const formFields = {
    account: [
        { name: 'name', type: 'text', label: 'Name', required: true },
        { name: 'description', type: 'text', label: 'Description (optional)' },
        { name: 'type', type: 'text', label: 'Type', required: true }
    ],
    saving: [
        { name: 'name', type: 'text', label: 'Name', required: true },
        { name: 'date', type: 'date', label: 'Date', required: true },
        { name: 'amount', type: 'number', label: 'Amount', step: '0.01', required: true },
        { name: 'account', type: 'number', label: 'Account ID', required: true },
        { name: 'category', type: 'text', label: 'Category', required: true },
        { name: 'currency', type: 'text', label: 'Currency', required: true }
    ],
    income: [
        { name: 'name', type: 'text', label: 'Name', required: true },
        { name: 'date', type: 'date', label: 'Date', required: true },
        { name: 'amount', type: 'number', label: 'Amount', step: '0.01', required: true },
        { name: 'account', type: 'number', label: 'Account ID', required: true },
        { name: 'category', type: 'text', label: 'Category', required: true },
        { name: 'currency', type: 'text', label: 'Currency', required: true }
    ],
    expense: [
        { name: 'name', type: 'text', label: 'Name', required: true },
        { name: 'date', type: 'date', label: 'Date', required: true },
        { name: 'amount', type: 'number', label: 'Amount', step: '0.01', required: true },
        { name: 'account', type: 'number', label: 'Account ID', required: true },
        { name: 'category', type: 'text', label: 'Category', required: true },
        { name: 'currency', type: 'text', label: 'Currency', required: true },
        { name: 'is_credit', type: 'select', label: 'Is Credit', options: ['Yes', 'No'], required: true },
        { name: 'installments', type: 'number', label: 'Installments', required: false },
        { name: 'status', type: 'select', label: 'Status', options: ['Paid', 'Pending'], required: true }
    ]
};

function createFormField(field) {
    const wrapper = document.createElement('div');
    const label = document.createElement('label');
    label.setAttribute('for', field.name);
    label.textContent = field.label;
    wrapper.appendChild(label);

    let input;
    if (field.type === 'select') {
        input = document.createElement('select');
        field.options.forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.textContent = option;
            input.appendChild(optionElement);
        });
    } else {
        input = document.createElement('input');
        input.setAttribute('type', field.type);
        if (field.step) input.setAttribute('step', field.step);
    }

    input.setAttribute('id', field.name);
    input.setAttribute('name', field.name);
    if (field.required) input.setAttribute('required', '');

    wrapper.appendChild(input);
    return wrapper;
}

export function createFormFields(type) {
    const formFieldsContainer = document.getElementById('formFields');
    formFieldsContainer.innerHTML = '';
    formFields[type].forEach(field => {
        const fieldElement = createFormField(field);
        formFieldsContainer.appendChild(fieldElement);
    });
}

function convertFormValues(formValues, formType) {
    const convertedValues = { ...formValues };

    if (formType === 'saving' || formType === 'income' || formType === 'expense') {
        const date = new Date(formValues.date);
        date.setHours(0, 0, 0, 0); // Set the time to 00:00:00
        convertedValues.date = date.toISOString(); // Ensures the date is in the correct format
        convertedValues.amount = parseFloat(formValues.amount);
        convertedValues.account = parseInt(formValues.account, 10);
    }

    if (formType === 'expense') {
        convertedValues.is_credit = formValues.is_credit === 'Yes';
        if (formValues.installments) {
            convertedValues.installments = parseInt(formValues.installments, 10);
        }
    }

    return convertedValues;
}

export async function handleFormSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const formValues = Object.fromEntries(formData.entries());

    // Determine the form type
    const formType = document.getElementById('formTitle').textContent.toLowerCase().split(' ')[1];

    try {
        const convertedValues = convertFormValues(formValues, formType);
        const result = await createEntry(formType, convertedValues);
        displayMessage(`${formType.charAt(0).toUpperCase() + formType.slice(1)} created successfully!`);
        setTimeout(showHome, 2000); // Return to home after 2 seconds
    } catch (error) {
        displayMessage(error.message, true);
    }
}
