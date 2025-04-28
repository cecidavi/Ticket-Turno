document.addEventListener('DOMContentLoaded', function() {
    const flashData = document.getElementById('flash-data');

    if (flashData) {
        const message = flashData.getAttribute('data-message');
        const category = flashData.getAttribute('data-category');

        if (message && category) {
            Swal.fire({
                text: message,
                icon: category,
                confirmButtonText: 'OK',
                timer: 3000,
                timerProgressBar: true
            });
        }
    }
});
