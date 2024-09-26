#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function() {
    fetch('/menu')
        .then(response => response.json())
        .then(data => {
            const menuList = document.getElementById('menu-list');
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item.name} - $${item.price.toFixed(2)}`;
                menuList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching menu:', error));
});

document.getElementById('reservation-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    fetch('/reservation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, date, time })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('reservation-message').textContent = data.message;
        // Clear form
        document.getElementById('reservation-form').reset();
    })
    .catch(error => console.error('Error creating reservation:', error));
});