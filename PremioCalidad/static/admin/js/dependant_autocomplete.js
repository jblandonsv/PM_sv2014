$(document).ready(function() {
   
    //$('body').on('change', '.autocomplete-light-widget select[name$=dependencia-autocomplete]', function() {
        $('body').on('change', '#id_dependencia', function() {
        
        /* TODO ESTE CODIGO FUNCIONA CUANDO SON DOS AUTOCOMPLETES, SOLO ES DE TENER CUIDADO
        DEL PARAMETRO QUE SE ENVIA COMO DATA DEL SEGUNDO AUTOCOMPLETE

        var countrySelectElement = $(this);
        //console.log(countrySelectElement);

        var regionSelectElement = $('#' + $(this).attr('id').replace('dependencia', 'unidad_superior'));
        var regionWidgetElement = regionSelectElement.parents('.autocomplete-light-widget');

        // When the country select changes
        value = $(this).val();

        console.log($('#id_dependencia-deck'));
        */
        
        //var regionSelectElement = $('#' + $(this).attr('id').replace('dependencia', 'unidad_superior'));
        var regionSelectElement = $('#id_unidad_superior');
        var regionWidgetElement = regionSelectElement.parents('.autocomplete-light-widget');
	console.log(regionWidgetElement );
        value = $(this).val();

        if (value) {
            // If value is contains something, add it to autocomplete.data
            regionWidgetElement.yourlabsWidget().autocomplete.data = {
                'dependencia_id': value,
            };
            //regionWidgetElement.yourlabsWidget().autocomplete.data = {
            //   'dependencia_id': $('#id_dependencia_text').val(),
            //};
        } else {
            // If value is empty, empty autocomplete.data
            regionWidgetElement.yourlabsWidget().autocomplete.data = {}
        }

        // example debug statements, that does not replace using breakbpoints and a proper debugger but can hel
        // console.log($(this), 'changed to', value);
        // console.log(regionWidgetElement, 'data is', regionWidgetElement.yourlabsWidget().autocomplete.data)
    })
});