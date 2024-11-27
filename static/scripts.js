$(document).ready(function() {
    // Detecta el cambio de archivo y actualiza la etiqueta
    $('#fileInput').on('change', function() {
        var fileName = $(this).val().split('\\').pop();
        $(this).next('.custom-file-label').html(fileName);
    });

    // Mapa
    var colorClassMap = {
        'battery': 'battery',
        'biological': 'biological',
        'brown-glass': 'brown-glass',
        'cardboard': 'cardboard',
        'clothes': 'clothes',
        'green-glass': 'green-glass',
        'metal': 'metal',
        'paper': 'paper',
        'plastic': 'plastic',
        'shoes': 'shoes',
        'trash': 'trash',
        'white-glass': 'white-glass'
    };

    // Si hay un resultado de clasificación, aplica la clase correspondiente
    var result = "{{ result }}";  

    // Remueve todas las clases anteriores y aplica la nueva
    if (result && colorClassMap[result]) {
        $('.card-header, .card-footer').removeClass(Object.values(colorClassMap).join(' '));
        $('.card-header, .card-footer').addClass(colorClassMap[result]);
    }

    if (result) {
        // Cambiar el color del botón
        var button = $('.btn-info');
        button.removeClass(Object.keys(colorClassMap).join(' '));
        button.addClass(colorClassMap[result]);
    }
});
