$(document).ready(function() {
    $('INPUT#btn_translate').click(function() {
        const languageCode = $('INPUT#language_code').val();
        const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

        $.get(url, function(data) {
            $('DIV#hello').text(data.hello);
        });
    });

    $('INPUT#language_code').keypress(function(event) {
        if (event.which === 13) {
            $('INPUT#btn_translate').click();
        }
    });
});
