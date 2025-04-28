function crearGraficaEstatus(pendientes, resueltos) {
    const ctx = document.getElementById('estatusChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Pendientes', 'Resueltos'],
            datasets: [{
                data: [pendientes, resueltos],
                backgroundColor: ['#f39c12', '#2ecc71'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                },
            }
        }
    });
}
