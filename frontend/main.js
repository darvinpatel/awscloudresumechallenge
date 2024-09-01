// Replace this with your actual API Gateway endpoint
const apiUrl = 'https://8hvxck6m48.execute-api.ap-southeast-2.amazonaws.com/visitorcountapi';

// Function to fetch the visitor count
async function getVisitorCount() {
    try {
        const response = await fetch(apiUrl);
        if (response.ok) {
            const data = await response.json();
            document.getElementById('visitor-count').innerText = `${data.body}`;
        } else {
            console.error('Error fetching visitor count:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching visitor count:', error);
    }
}

// Call the function to get the visitor count when the page loads
window.onload = getVisitorCount;
