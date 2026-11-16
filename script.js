document.getElementById('crouton').addEventListener('click', function() {
    // Create jumpscare overlay
    const overlay = document.createElement('div');
    overlay.id = 'jumpscare';
    overlay.innerHTML = '<img src="thorn.png" alt="Jumpscare!">';
    document.body.appendChild(overlay);
    
    // After a short delay, remove the overlay
    setTimeout(() => {
        overlay.remove();
    }, 3000);
});