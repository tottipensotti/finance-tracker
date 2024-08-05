const API_BASE_URL = 'http://localhost:8000';

const ENDPOINTS = {
    account: '/accounts/',
    income: '/incomes/',
    expense: '/expenses/',
    saving: '/savings/'
};

export async function createEntry(type, data) {
    const url = `${API_BASE_URL}${ENDPOINTS[type]}`;
    console.log(JSON.stringify(data));
    console.log(data);
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'An error occurred');
        }
        console.log(JSON.stringify(data));
        return await response.json();
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }

    
}