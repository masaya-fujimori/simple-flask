function getGreeting() {
    fetch('http://localhost:5000/api/greet')
        .then(response => response.json())
        .then(data => {
            document.getElementById('greeting').textContent = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
