$(document).ready(function() {
    function fetchGreeting() {
        const languageCode = $('#language_code').val();
        $.get(`https://fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(fetchGreeting);
    $('#language_code').keypress(function(event) {
        if (event.which === 13) { // Enter key
            fetchGreeting();
        }
    });
});
