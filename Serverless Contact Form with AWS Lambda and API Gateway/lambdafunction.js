function submitForm() {
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value,
    };

    fetch('API_GATEWAY_URL', {
        method: 'POST',
        body: JSON.stringify(formData),
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Message sent successfully!');
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to send message. Please try again.');
        });
}
