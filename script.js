console.log("Aplicación iniciada...");

let myChart; 
const apiUrl = 'http://127.0.0.1:8000/api/indicadores';

// Seleccionamos los botones 
const btnDolar = document.getElementById('btnDolar');
const btnUf = document.getElementById('btnUf');
const btnEuro = document.getElementById('btnEuro');

function updateChart(label, dataValues) {
    myChart.data.datasets[0].label = label;
    myChart.data.datasets[0].data = dataValues;
    myChart.update();
}

function setActiveButton(activeButton) {
    [btnDolar, btnUf, btnEuro].forEach(button => {
        button.classList.remove('active');
    });
    activeButton.classList.add('active');
}

fetch(apiUrl)
    .then(response => response.json())
    .then(fullData => {
        console.log("Datos recibidos. Preparando gráfico...");
        
        const labels = fullData.map(entry => entry.Fecha);
        const dolarValues = fullData.map(entry => entry.Dolar);
        const ufValues = fullData.map(entry => entry.UF);
        const euroValues = fullData.map(entry => entry.Euro);

        const ctx = document.getElementById('myChart').getContext('2d');

        myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Valor del Dólar Observado (CLP)',
                    data: dolarValues,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1,
                    spanGaps: true 
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' },
                    title: { display: true, text: 'Evolución de Indicadores Económicos' }
                },
                scales: { y: { beginAtZero: false } }
            }
        });
        
        setActiveButton(btnDolar);

        btnDolar.addEventListener('click', () => {
            updateChart('Valor del Dólar Observado (CLP)', dolarValues);
            setActiveButton(btnDolar);
        });

        btnUf.addEventListener('click', () => {
            updateChart('Valor de la UF (CLP)', ufValues);
            setActiveButton(btnUf);
        });

        btnEuro.addEventListener('click', () => {
            updateChart('Valor del Euro (CLP)', euroValues);
            setActiveButton(btnEuro);
        });

    })
    .catch(error => {
        console.error('Error al obtener los datos:', error);
    });