document.getElementById('contactForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    const response = await fetch(form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
        },
        body: formData,
    });

    const messageDiv = document.getElementById('message');

    if (response.ok) {
        const data = await response.json();
        messageDiv.textContent = data.message;
        messageDiv.className = 'alert alert-success';
        form.reset();
    } else {
        const errorData = await response.json();
        messageDiv.textContent = 'Error: ' + JSON.stringify(errorData.errors);
        messageDiv.className = 'alert alert-danger';
    }
});



document.querySelectorAll('.rating input').forEach(radio => {
    radio.addEventListener('change', () => {
        const rating = parseInt(radio.value);
        // alert("rating is " + rating)
        if (rating == 5) 
        {
            document.getElementById('improve-message').style.display = 'none';
            document.getElementById('thank-you-message').style.display = 'none';
            document.getElementById('delighted').style.display = 'block';
        } 
        else if (rating < 3) 
        {
            document.getElementById('thank-you-message').style.display = 'none';
            document.getElementById('improve-message').style.display = 'block';
            document.getElementById('delighted').style.display = 'none';
        } 
        else 
        {
            document.getElementById('improve-message').style.display = 'none';
            document.getElementById('thank-you-message').style.display = 'block';
            document.getElementById('delighted').style.display = 'none';
        }
    });
});